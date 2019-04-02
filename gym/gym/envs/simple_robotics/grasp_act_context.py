import numpy as np
from gym import utils
from gym.envs.simple_robotics import simple_robotics_context
from gym.envs.simple_robotics import rotations

RELATIVE_UPPER = 1.0 * np.pi / 180.0 
RELATIVE_LOWER = -RELATIVE_UPPER

class GraspActContextEnv(simple_robotics_context.SimpleRoboticsEnv, utils.EzPickle):
    def __init__(self, model_path, frame_skip):
        self.prev_cmd = np.zeros(4) #np.zeros(self.sim.model.actuator_ctrlrange.shape[0])
        self.finger_loc = 0.051
        self.finger_length = 0.145
        print ("finger loc:", self.finger_loc)
        simple_robotics_context.SimpleRoboticsEnv.__init__(self, model_path, frame_skip)  # frameskip = 1
        utils.EzPickle.__init__(self)
        self.init_config = {'qpos':[],'qvel':[]}

    def getcontext(self):
        actions = [[],[],[],[],[]]
        context = np.zeros((len(actions[0]), 4+12, len(actions)))
        for i in range(len(actions)):
            context[:,:,i] = self.openloop(actions[i])
        context = np.zeros([40,40,3])
        return context

    def openloop(self, acts):
        single_context = np.zeros((len(acts), 4+12))
        self.reset2init()
        for i in range(len(acts)):
            act = np.clip(acts[i], self.action_space.low, self.action_space.high)
            self._set_action(act)
            self.sim.step()
            obs = self._get_obs()
            single_context[i,:] = np.concatenate((act, obs))
        return single_context
 
    def reset2init(self):
        qpos = self.init_config['qpos']
        qvel = self.init_config['qvel']
        self.set_state(qpos, qvel)

    def step(self, action, render=False):
        action = action.flatten()
        # assert np.shape(a) == (4,)
        # reward = 0  # yet to specify
        # self.do_simulation(a, self.frame_skip)
        # done = False
        # ob = self._get_obs()
        action = np.clip(action, self.action_space.low, self.action_space.high)
        self._set_action(action)
        self.sim.step()
        obs = self._get_obs()
        # reward = self.compute_reward()
        if not render:
            done =  not self.in_reach() or not self.safe_torques()
        else:
            done = False # do not terminate early if render
        info = {}
        reward = self.compute_reward(version='strict_tips')
        obs = (obs, self.context)
        return obs, reward, done, info

    def _get_obs(self):
        handpos = self.sim.data.sensordata[:4]
        if self.prev_cmd is None:
            motorpos = handpos
        else:
            motorpos = self.prev_cmd
        torques = self.compute_torques()
        # print ("all shapes:", motorpos.size, handpos.size, torques.size)
        state = np.concatenate((motorpos, handpos, torques))

        return state

    def _set_action(self, action):
        assert action.shape == (4,)
        ctrlrange = self.sim.model.actuator_ctrlrange
        # action transform
        actuation_range = (RELATIVE_UPPER - RELATIVE_LOWER) / 2.
        actuation_center = (RELATIVE_UPPER + RELATIVE_LOWER) / 2.
        relative_cmd = actuation_center + action * actuation_range        
        # add 
        new_cmd = self.prev_cmd + relative_cmd
        # clip
        self.sim.data.ctrl[:] = new_cmd
        self.sim.data.ctrl[:] = np.clip(self.sim.data.ctrl, ctrlrange[:, 0], ctrlrange[:, 1])
        self.prev_cmd = self.sim.data.ctrl.copy()

    def reset_model(self):
        # qpos = self.init_qpos + self.np_random.uniform(size=self.model.nq, low=-.01, high=.01)
        failed = True
        while failed:
            # randomizing object size
            LOW = np.array([0.02, 0.02, 0.1])
            HIGH = np.array([0.03, 0.03, 0.1])
            #LOW = np.array([0.01, 0.01, 0.1])
            #HIGH = np.array([0.02, 0.02, 0.1])
            #LOW = np.array([0.01, 0.01, 0.1])
            #HIGH = np.array([0.008, 0.008, 0.1])
            self.sim.model.geom_size[-2, :] = np.random.rand(3) * (HIGH - LOW) + LOW
            self.sim.model.geom_size[-1, :] = self.sim.model.geom_size[-2, :] - 0.005
            # randomizing pos and orientations
            qvel = self.init_qvel # + self.np_random.randn(self.model.nv) * .01
            # random object com
            initial_obj_com = self.init_objpos[:3] + self.np_random.uniform(size=3, low=-.01, high=.01)
            # random object z rotation
            angle = self.np_random.uniform(-np.pi, np.pi)
            axis = np.array([0., 0., 1.])
            offset_quat = rotations.quat_from_angle_and_axis(angle, axis)
            initial_obj_quat = self.init_objpos[3:].copy()
            initial_obj_quat = rotations.quat_mul(initial_obj_quat, offset_quat)
            initial_obj_quat /= np.linalg.norm(initial_obj_quat)
            qpos = np.concatenate((self.init_handpos, initial_obj_com, initial_obj_quat))
            # set state
            self.init_config['qpos'] = qpos
            self.init_config['qvel'] = qvel
            self.set_state(qpos, qvel)
            failed = not self.in_reach()
            # set previous cmds
            self.prev_cmd = np.zeros(4)
        self.context = self.getcontext()
        return (self._get_obs(), self.context)

    def viewer_setup(self):
        self.viewer.cam.distance = self.model.stat.extent * 0.5

    def compute_torques(self):
        torques = self.sim.data.sensordata[4:]
        torques = np.array([np.linalg.norm(torques[:3]), np.linalg.norm(torques[3:6]), np.linalg.norm(torques[6:9]), np.linalg.norm(torques[9:12])])
        return torques

    def compute_reward(self, version='naive'):
        # print(version)
        sum_torques = sum(self.compute_torques())
        if version is 'naive':
            # print ("naive")
            return sum_torques
        elif version is 'strict_tips':
            if self.distal_contact() and self.fingers_contact():
                return sum_torques
            else:
                return 0

    def distal_contact(self):
        # require that obj is in contact with distal fingers
        geom_name = ['C_fd1', 'C_fd2']
        geom_name = ['robot0:' + name for name in geom_name] 
        obj_id = self.model.geom_name2id('object')
        distal_id = [0] # obj_id is always contact with 0
        two_distal_id = []
        fdcontact = {}
        for name in geom_name:
            distal_id.append(self.model.geom_name2id(name))
            two_distal_id.append(self.model.geom_name2id(name))
            fdcontact[self.model.geom_name2id(name)] = False
        ncon = self.sim.data.ncon
        contacts = self.sim.data.contact[:ncon]
        for contact in contacts:
            # if geom1 is obj_id
            if contact.geom1 == obj_id:
                if contact.geom2 not in distal_id:
                    return False #which means obj is contacting with sth else, not only with distal fingers and floor
            # if geom2 is obj_id
            if contact.geom2 == obj_id:
                if contact.geom1 not in distal_id:
                    return False #which means obj is contacting with sth else, not only with distal fingers and floor
        for contact in contacts:
            # if geom1 is obj_id
            if contact.geom1 == obj_id:
                if contact.geom2 in two_distal_id:
                    fdcontact[contact.geom2] = True
                    #return True #which means obj is contacting with distal fingers 
            # if geom2 is obj_id
            if contact.geom2 == obj_id:
                if contact.geom1 in two_distal_id:
                    fdcontact[contact.geom2] = True
                    #return True
        return fdcontact[two_distal_id[0]]&fdcontact[two_distal_id[1]]
        #print(contact.geom1,contact.geom2,contact.pos)

    def fingers_contact(self):
        # require that two fingers do not touch
        geom_name1 = ['C_fd1', 'C_fp1']
        geom_name2 = ['C_fd2', 'C_fp2']
        geom_name1 = ['robot0:' + name for name in geom_name1]
        geom_name2 = ['robot0:' + name for name in geom_name2]
        fingers_id1 = [self.model.geom_name2id(name) for name in geom_name1]
        fingers_id2 = [self.model.geom_name2id(name) for name in geom_name2]
        ncon = self.sim.data.ncon
        contacts = self.sim.data.contact[:ncon]
        for contact in contacts:
            if contact.geom1 in fingers_id1 and contact.geom2 in fingers_id2:
                return False
            if contact.geom2 in fingers_id1 and contact.geom1 in fingers_id2:
                return False
        return True

    def safe_torques(self):
        TORQUE_LIMIT = 0.35  # used to be 0.6
        if np.sum(self.compute_torques() >= TORQUE_LIMIT) >= 1:
            return False
        else:
            return True

    def in_reach(self):
        objpos = self.sim.data.get_body_xpos("object")
        palmpos = self.sim.data.get_body_xpos("robot0:palm")
        center = np.zeros(3)
        center[0] = objpos[1] - palmpos[1]
        center[1] = objpos[0] - palmpos[0]
        center[2] = objpos[2]
        return self._in_reach(center[0], center[1], center[2])

    # TODO: discuss the correct way to tell if in reach
    def _in_reach(self, x, y, z):
        in_angle = self._in_right_angle(x, y) or self._in_left_angle(x, y)
        in_circle = self._in_left_circle(x, y) or self._in_right_circle(x, y)
        not_behind = y > 0
        # print "in_angle:", in_angle, "in_circle:", in_circle, "not_behind:", not_behind, "height:", height, z
        # return in_angle and in_circle and not_behind and height
        return in_angle and in_circle and not_behind

    def _in_left_circle(self, x, y):
        limit = self.finger_length + 0.003
        return (x + self.finger_loc) ** 2 + y * y < limit ** 2

    def _in_right_circle(self, x, y):
        limit = self.finger_length + 0.003
        return (x - self.finger_loc) ** 2 + y * y < limit ** 2

    def _in_left_angle(self, x, y):
        return y > x + self.finger_loc

    def _in_right_angle(self, x, y):
        return y > x - self.finger_loc
            


class GraspCubeActContextEnv(GraspActContextEnv):
    def __init__(self):
        GraspActContextEnv.__init__(self, 'seahand/manipulate_block.xml', 1)


class GraspEggActContextEnv(GraspActContextEnv):
    def __init__(self):
        GraspActContextEnv.__init__(self, 'seahand/manipulate_egg.xml', 1)


class GraspPenActContextEnv(GraspActContextEnv):
    def __init__(self):
        GraspActContextEnv.__init__(self, 'seahand/manipulate_pen.xml', 1)


class GraspBallActContextEnv(GraspActContextEnv):
    def __init__(self):
        GraspActContextEnv.__init__(self, 'seahand/manipulate_ball.xml', 1)


class GraspCylinderActContextEnv(GraspActContextEnv):
    def __init__(self):
        GraspActContextEnv.__init__(self, 'seahand/manipulate_cylinder.xml', 1)

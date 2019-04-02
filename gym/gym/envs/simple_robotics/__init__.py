from gym.envs.simple_robotics.simple_robotics_env import SimpleRoboticsEnv
from gym.envs.simple_robotics.roam_simple_robotics_env import ROAMSimpleRoboticsEnv
# ^^^^^ so that user gets the correct error
# message if mujoco is not installed correctly
from gym.envs.simple_robotics.grasp import GraspEnv
from gym.envs.simple_robotics.grasp import GraspCubeEnv
from gym.envs.simple_robotics.grasp import GraspEggEnv
from gym.envs.simple_robotics.grasp import GraspPenEnv
from gym.envs.simple_robotics.grasp import GraspBallEnv
from gym.envs.simple_robotics.grasp import GraspCylinderEnv
from gym.envs.simple_robotics.roam_grasp import ROAMGraspEnv
from gym.envs.simple_robotics.roam_grasp import ROAM_GraspCubeEnv


from gym.envs.simple_robotics.grasp2 import Grasp2Env
from gym.envs.simple_robotics.grasp2 import GraspCube2Env
from gym.envs.simple_robotics.grasp2 import GraspEgg2Env
from gym.envs.simple_robotics.grasp2 import GraspPen2Env
from gym.envs.simple_robotics.grasp2 import GraspBall2Env
from gym.envs.simple_robotics.grasp2 import GraspCylinder2Env

from gym.envs.simple_robotics.grasp3 import Grasp3Env
from gym.envs.simple_robotics.grasp3 import GraspCube3Env
from gym.envs.simple_robotics.grasp3 import GraspEgg3Env
from gym.envs.simple_robotics.grasp3 import GraspPen3Env
from gym.envs.simple_robotics.grasp3 import GraspBall3Env
from gym.envs.simple_robotics.grasp3 import GraspCylinder3Env

from gym.envs.simple_robotics.grasp_relative import GraspRelativeEnv
from gym.envs.simple_robotics.grasp_relative import GraspCubeRelativeEnv
from gym.envs.simple_robotics.grasp_relative import GraspEggRelativeEnv
from gym.envs.simple_robotics.grasp_relative import GraspPenRelativeEnv
from gym.envs.simple_robotics.grasp_relative import GraspBallRelativeEnv
from gym.envs.simple_robotics.grasp_relative import GraspCylinderRelativeEnv

from gym.envs.simple_robotics.grasp_safe import GraspRelativeSafeEnv
from gym.envs.simple_robotics.grasp_safe import GraspCubeRelativeSafeEnv
from gym.envs.simple_robotics.grasp_safe import GraspEggRelativeSafeEnv
from gym.envs.simple_robotics.grasp_safe import GraspPenRelativeSafeEnv
from gym.envs.simple_robotics.grasp_safe import GraspBallRelativeSafeEnv
from gym.envs.simple_robotics.grasp_safe import GraspCylinderRelativeSafeEnv

from gym.envs.simple_robotics.grasp_safe_render import GraspCubeRelativeSafeRenderEnv
from gym.envs.simple_robotics.grasp_safe_render_big import GraspCubeRelativeSafeRenderBigEnv

from gym.envs.simple_robotics.grasp_safe_smallobject import GraspCubeRelativeSafeSmallObjectEnv
from gym.envs.simple_robotics.grasp_safe_Time_Small import GraspCubeRelativeSafeTimeSmallEnv

from gym.envs.simple_robotics.grasp_single import GraspSingleCubeEnv

from gym.envs.simple_robotics.grasp_smooth import GraspCubeSmoothEnv

from gym.envs.simple_robotics.grasp_easy import GraspCubeRelativeSafeEasyEnv

from gym.envs.simple_robotics.grasp_act_context import GraspCubeActContextEnv

from gym.envs.simple_robotics.grasp_image_context import GraspCubeImageContextEnv

from gym.envs.simple_robotics.grasp_three import GraspCubeRelativeSafeThreeEnv

from gym.envs.simple_robotics.grasp_lift import GraspCubeLiftEnv

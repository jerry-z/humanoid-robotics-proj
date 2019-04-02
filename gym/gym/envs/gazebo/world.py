import rospy
from gazebo_msgs.srv import SpawnModel
from geometry_msgs.msg import Pose

print ("first")
rospy.init_node('insert_object',log_level=rospy.INFO)
print ("sed")
initial_pose = Pose()
initial_pose.position.x = 1
initial_pose.position.y = 10
initial_pose.position.z = 1
print ('thi')
f = open('/home/xiya/.gazebo/models/jersey_barrier/model.sdf','r')
sdff = f.read()
print ('fou')
rospy.wait_for_service('gazebo/spawn_sdf_model')
spawn_model_prox = rospy.ServiceProxy('gazebo/spawn_sdf_model', SpawnModel)
spawn_model_prox("some_robo_name", sdff, "robotos_name_space", initial_pose, "world")
initial_pose = Pose()
initial_pose.position.x = 1
initial_pose.position.y = 1
initial_pose.position.z = 1
print ("five")
rospy.wait_for_service('gazebo/spawn_sdf_model')
spawn_model_prox = rospy.ServiceProxy('gazebo/spawn_sdf_model', SpawnModel)
print ("six")
spawn_model_prox("some_robo_name2", sdff, "robotos_name_space2", initial_pose, "world")
f.close()
print ("seven")

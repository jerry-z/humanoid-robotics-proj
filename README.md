# humanoid-robotics-proj

our project has results as follow:

1) Fetch Robot reach simulation with her algorithm(DDPG)

2) Fetch Robot push simulation with her algorithm(DDPG)

3) Fetch Robot pick and place simulation with her algorithm(DDPG)

4) Fetch Robot reach simulation with her algorithm(DDPG) using CNN image network


there are some descriptions for the files in the folder:

1. training and testing files:(baselines2/baselines)

	run.py is used to train all the models for fetch
	run_test_pap.py is used to test the pick and place model with camera vision
	run_test_reach_pap.py is used to test the reach model with camera vision
	run_data.py is dsed to collect the training image data and label for the CNN image network
2. robot environment files:(gym2/gym/env/hunanoid_robots)
	fetch_env.py and robot_env.py is used to generate simulation environment
	our robot environment is as follow:
		FetchReach-v1
		FetchPush-v1
		FetchPickAndPlace-v1
		H_FetchReach-v1(with camera)
		H_FetchPush-v1(with camera)
		H_FetchPickAndPlace-v1(with camera)
		H_FetchReachObstacle(with camera and obstacle)
3. image training data:(Document/cnn_data/camera_data)
	all the image data and label are list in the folder
	there are also CNN model creating(training) python file and CNN model evaluating python file with the training acc/loss image.png
4. training log files:(Document/log)
	some of the training record are saved in the log folder as txt and csv file
	the success rate plot are saved in the image folder as png images
5. trained policies:(Document/policies)
	all the trained policies are saved in this folder
	inside, cuda folder contains all the well trained normal fetch simulation policies
	and vision folder contains all the trained vision-fetch simuation policies
6. ROS related files(proj_ros_ws + ros_ws)
	all teh ROS-gazebo implementaion files can be found here
7. algorith files:(baselines)
	her algorithm related files can be found in baselines2/baselines/her

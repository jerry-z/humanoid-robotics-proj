import os
import subprocess


def launch_ros():
	# os.system("source ~/virtualenvs/ros/bin/activate")
	print ("launch in")
	subprocess.Popen('bash /home/xiya/ROAR/code/rlrobotics/gym-fetch/gym/gym/envs/gazebo/launch.sh', shell=True) 
	print ("Launched")



if __name__=='__main__':
	launch_ros()
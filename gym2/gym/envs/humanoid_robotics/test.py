from mujoco_py import load_model_from_path, MjSim, MjViewer
import os
import sys 
import ipdb
import numpy as np
from PIL import Image
sys.path.append("..")

model = load_model_from_path('assets/fetch/reach.xml')	
sim = MjSim(model)
viewer = MjViewer(sim)
sim.data.set_joint_qpos('robot0:head_tilt_joint', 0.3)
camera_image = sim.render(width=256,height=256,camera_name='head_camera_rgb')
print(type(camera_image))
# img = Image.fromarray(camera_image, 'RGB')
# img.save('my.png')
# img.show()

#ipdb.set_trace()
# while True:
# 	viewer.render()
# 	sim.step()
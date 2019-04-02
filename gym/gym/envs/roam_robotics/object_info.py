import numpy as np 

class objInfo:
	def __init__(self, info=[0.02, 0.02, 0.1, 0]):
		LOW = np.array([0.03, 0.03, 0.1])
		HIGH = np.array([0.04, 0.04, 0.1])
		self.size = np.random.rand(3) * (HIGH - LOW) + LOW
		self.angle = np.random.uniform(-np.pi, np.pi)
		# self.size = np.array(info[:3])
		# self.angle = info[3]
		print ("obj size:", self.size)
		print ("obj angle", self.angle)

import numpy 
import math

class Factory(object):
	"""docstring for Factory"""
	def __init__(self, width, length, center_x, center_y):
		self.width = width
		self.length = length
		self.center_point = numpy.array([center_x,center_x])
		self.area = numpy.ndarray(shape = (length, width), dtype = float)

		
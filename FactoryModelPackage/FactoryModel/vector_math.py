import math
import numpy

class VectorMath(object):
	"""docstring for VectorMath"""
	
	def __init__(self):
		pass

	@staticmethod
	def get_magnitude(vector1, vector2):
		# vector1 is the initial point
		# vector2 is the point you want to reach
		difference = numpy.subtract(vector2, vector1)
		magnitude = numpy.linalg.norm(difference)

		return magnitude

	@staticmethod
	def get_single_magnitude(vector):
		magnitude = numpy.linalg.norm(vector)

		return magnitude 
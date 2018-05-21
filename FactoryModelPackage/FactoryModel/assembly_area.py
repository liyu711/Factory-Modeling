import numpy

class AssemblyArea(object):

	def __init__(self, length, width, center_x, center_y):
		self.length = length
		self.width = width
		self.center_point = numpy.array([center_x, center_y])
		self.area = numpy.ndarray(shape = (length, width), dtype = float)
		
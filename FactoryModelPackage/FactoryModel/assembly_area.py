import numpy

class AssemblyArea(object):
	"""docstring for AssemblyArea"""
	def __init__(self, length, width):
		self.length = length
		self.width = width
		self.area = numpy.ndarray(shape = (length, width), dtype = float)
		
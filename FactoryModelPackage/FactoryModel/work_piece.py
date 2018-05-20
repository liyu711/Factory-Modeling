import numpy
class WorkPiece(object):
	"""docstring for WorkPiece"""
	def __init__(self, length, width, ini_x, ini_y, fin_x, fin_y):
		self.length = length
		self.width = width
		self.ini_point = numpy.array([ini_x, ini_y])
		self.fin_point = numpy.array([fin_x, fin_y])

		
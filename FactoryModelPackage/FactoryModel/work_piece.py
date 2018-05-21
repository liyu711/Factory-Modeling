import numpy

class WorkPiece(object):
	"""docstring for WorkPiece"""
	def __init__(self, length, width, ini_x, ini_y, fin_x, fin_y):
		self.length = length
		self.width = width
		self.ini_point = numpy.array([ini_x, ini_y])
		self.current_point = numpy.array([ini_x, ini_y])
		self.fin_point = numpy.array([fin_x, fin_y])

	def get_current_point(self):
		return self.current_point

	def set_current_point(self, new_point):
		self.current_point = new_point

	def reset_position(self):
		self.current_point = self.ini_point

	def move(self):
		current_x = self.current_point[0]
		current_y = self.current_point[1]
		where_should_i_go = [
			numpy.array([current_x -1, current_y +1])
			numpy.array([current_x -1, current_y])
			numpy.array([current_x -1, current_y -1])
			numpy.array([current_x, current_y +1])
			numpy.array([current_x, current_y -1])
			numpy.array([current_x +1, current_y +1])
			numpy.array([current_x +1, current_y])
			numpy.array([current_x +1, current_y -1])
		]
		
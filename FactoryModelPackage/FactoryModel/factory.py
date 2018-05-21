import numpy 
import math
from FactoryModel import *

class Factory(object):
	"""docstring for Factory"""
	def __init__(self, width, length, center_x, center_y):
		self.width = width
		self.length = length
		self.center_point = numpy.array([center_x,center_x])
		self.area = numpy.ndarray(shape = (length, width), dtype = float)
		self.work_pieces = numpy.array([])

	def add_work_piece(self, work_piece):
		self.work_pieces = numpy.hstack(self.work_pieces, work_piece)

	def reset_work_pieces(self):
		self.work_pieces = numpy.array([])

	def arrange(self):
		cost = 0
		for work_piece in work_pieces:
			while work_piece.get_current_point() != work_piece.get_final_position():
				work_piece.move()
				cost += 1

		return cost	

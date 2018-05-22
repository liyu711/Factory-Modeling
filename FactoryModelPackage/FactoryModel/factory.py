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

	def add_workpiece(self, work_piece):
		self.work_pieces = numpy.hstack([self.work_pieces, work_piece])

	def add_workpieces(self, work_pieces):
		for work_piece in work_pieces:
			self.add_workpiece(work_piece)

	def reset_work_pieces(self):
		self.work_pieces = numpy.array([])

	def arrange(self):
		cost = 0
		for work_piece1 in self.work_pieces:
			while work_piece1.current_point[0] != work_piece1.fin_point[0] and work_piece1.current_point[1] != work_piece1.fin_point[1]:
				for work_piece2 in self.work_pieces:
					if work_piece2.ini_point[0] == work_piece1.ini_point[0] and work_piece2.ini_point[1] == work_piece2.ini_point[1]:
						continue
					else:
						work_piece1.find_path(work_piece2)
				work_piece1.move()
				cost += 1
			

		return cost	

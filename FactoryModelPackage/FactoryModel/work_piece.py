import numpy
import math
from FactoryModel import VectorMath

class WorkPiece(object):
	"""docstring for WorkPiece"""
	def __init__(self, length, width, ini_x, ini_y, fin_x, fin_y):
		# I assume length is on x-axis and width is on y-axis
		self.length = length
		self.width = width
		self.ini_point = numpy.array([ini_x, ini_y])
		self.current_point = numpy.array([ini_x, ini_y])
		self.fin_point = numpy.array([fin_x, fin_y])
		self.boundary_points = [
			numpy.array([self.current_point[0] - length/2, self.current_point[1] - width/2]),
			numpy.array([self.current_point[0] - length/2, self.current_point[1] + width/2]),
			numpy.array([self.current_point[0] + length/2, self.current_point[1] - width/2]),
			numpy.array([self.current_point[0] + length/2, self.current_point[1] + width/2])
		]
		self.where_should_i_go = [
			numpy.array([self.current_point[0] -1, self.current_point[1] -1]),
			numpy.array([self.current_point[0] -1, self.current_point[1]]),
			numpy.array([self.current_point[0] -1, self.current_point[1] +1]),
			numpy.array([self.current_point[0], self.current_point[1] +1]),
			numpy.array([self.current_point[0], self.current_point[1] -1]),
			numpy.array([self.current_point[0] +1, self.current_point[1] -1]),
			numpy.array([self.current_point[0] +1, self.current_point[1]]),
			numpy.array([self.current_point[0] +1, self.current_point[1] +1])
		]

	def get_current_point(self):
		return self.current_point

	def reset_path(self):
		self.where_should_i_go = [
			numpy.array([self.ini_point[0] -1, self.ini_point[1] -1]),
			numpy.array([self.ini_point[0] -1, self.ini_point[1]]),
			numpy.array([self.ini_point[0] -1, self.ini_point[1] +1]),
			numpy.array([self.ini_point[0], self.ini_point[1] +1]),
			numpy.array([self.ini_point[0], self.ini_point[1] -1]),
			numpy.array([self.ini_point[0] +1, self.ini_point[1] -1]),
			numpy.array([self.ini_point[0] +1, self.ini_point[1]]),
			numpy.array([self.ini_point[0] +1, self.ini_point[1] +1])
		]

	def set_current_point(self, new_point):
		self.current_point = new_point

	def reset_position(self):
		self.current_point = self.ini_point

	def get_final_position(self):
		return self.fin_point

	def check_if_point_is_overlapping_with_workpiece(self, point_to_check):
		status = False
		check_x = self.boundary_points[0][0] <= point_to_check[0] and point_to_check[0] <= self.boundary_points[3][0]
		check_y = self.boundary_points[0][1] <= point_to_check[1] and point_to_check[1] <= self.boundary_points[3][1]
		if check_x and check_y:
			status = True

		return status

	def check_if_workpiece_reaches_its_destination(self):
		return self.current_point[0] == self.fin_point[0] and self.current_point[1] == self.fin_point[1]

	def find_path(self, another_workpiece):
		i = 0
		while i < len(self.where_should_i_go)-1:
			check_if_x_in_range = (another_workpiece.boundary_points[0][0] - self.length/2) < self.where_should_i_go[i][0] and self.where_should_i_go[i][0] < (another_workpiece.boundary_points[3][0] + self.length/2)
			# print(another_workpiece.boundary_points[0][0] - self.length/2)
			# print(another_workpiece.boundary_points[0][1] - self.length/2)
			# print(self.where_should_i_go[i][0])
			# print(another_workpiece.boundary_points[3][0] - self.length/2)
			# print(another_workpiece.boundary_points[3][1] - self.length/2)
			# print(self.where_should_i_go[i][1])
			check_if_y_in_range = (another_workpiece.boundary_points[0][1] - self.width/2) < self.where_should_i_go[i][1] and self.where_should_i_go[i][1] < (another_workpiece.boundary_points[3][1] + self.width/2)
			if check_if_x_in_range and check_if_y_in_range:
				del self.where_should_i_go[i]
				i -= 1
			i+=1
		# for point in self.where_should_i_go:
		# 	check_if_x_in_range = (another_workpiece.boundary_points[0][0] - self.length/2) < point[0] and point[0] < (another_workpiece.boundary_points[3][0] + self.length/2)
		# 	check_if_y_in_range = (another_workpiece.boundary_points[0][1] - self.width/2) < point[0] and point[0] < (another_workpiece.boundary_points[3][1] + self.width/2)
		# 	if check_if_y_in_range and check_if_y_in_range:
		# 		self.where_should_i_go.remove(point)

	def move(self):
		min_magnitude = 10000000000000
		point_to_go = self.current_point

		for point in self.where_should_i_go:
			distance_magnitude_to_the_end = VectorMath.get_magnitude(self.fin_point, point)
			if distance_magnitude_to_the_end < min_magnitude:
				min_magnitude = distance_magnitude_to_the_end
				point_to_go = point

		self.current_point = point_to_go
		self.where_should_i_go = [
			numpy.array([self.current_point[0] -1, self.current_point[1] -1]),
			numpy.array([self.current_point[0] -1, self.current_point[1]]),
			numpy.array([self.current_point[0] -1, self.current_point[1] +1]),
			numpy.array([self.current_point[0], self.current_point[1] +1]),
			numpy.array([self.current_point[0], self.current_point[1] -1]),
			numpy.array([self.current_point[0] +1, self.current_point[1] -1]),
			numpy.array([self.current_point[0] +1, self.current_point[1]]),
			numpy.array([self.current_point[0] +1, self.current_point[1] +1])
		]

	# def move(self):
	# 	current_x = self.current_point[0]
	# 	current_y = self.current_point[1]
	# 	min_magnitude = 10000000000000
	# 	point_to_go = self.current_point
	# 	where_should_i_go = [
	# 		numpy.array([current_x -1, current_y +1]),
	# 		numpy.array([current_x -1, current_y]),
	# 		numpy.array([current_x -1, current_y -1]),
	# 		numpy.array([current_x, current_y +1]),
	# 		numpy.array([current_x, current_y -1]),
	# 		numpy.array([current_x +1, current_y +1]),
	# 		numpy.array([current_x +1, current_y]),
	# 		numpy.array([current_x +1, current_y -1])
	# 	]
	# 	for point in where_should_i_go:
	# 		distance_magnitude_to_the_end = VectorMath.get_magnitude(self.fin_point, point)
	# 		print(distance_magnitude_to_the_end)
	# 		if distance_magnitude_to_the_end < min_magnitude:
	# 			min_magnitude = distance_magnitude_to_the_end
	# 			point_to_go = point

	# 	self.current_point = point_to_go


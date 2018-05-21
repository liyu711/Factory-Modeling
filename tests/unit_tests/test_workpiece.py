import unittest
import numpy
from FactoryModel import *

class WorkPieceTestCase(unittest.TestCase):
	"""docstring for WorkPieceTestCase"""
	def setUp(self):
		self.workpiece1 = WorkPiece(5, 50, 90, 30, 50, 110)
		self.length1 = 5
		self.width1 = 50
		self.init_point1 = numpy.array([90,30])
		self.fin_point1 = numpy.array([50,110])
		self.workpiece2 = WorkPiece(2, 1, 0, 0, 3, 3)
	
	def test_init(self):
		self.assertEqual(self.workpiece1.length, self.length1)
		self.assertEqual(self.workpiece1.width, self.width1)
		self.assertEqual(self.workpiece1.ini_point[0], self.init_point1[0])
		self.assertEqual(self.workpiece1.ini_point[1], self.init_point1[1])

	def test_move(self):
		self.workpiece2.reset_position()
		self.workpiece2.move()
		self.workpiece2.move()
		self.workpiece2.move()
		print(self.workpiece2.get_current_point())
		self.assertEqual(self.workpiece2.get_current_point()[0], 3)
		self.assertEqual(self.workpiece2.get_current_point()[1], 3)

	def test_if_reaches_destination(self):
		self.workpiece1.reset_position()
		false = self.workpiece1.check_if_workpiece_reaches_its_destination()
		self.workpiece2.reset_position()
		self.workpiece2.set_current_point(numpy.array([3,3,3]))
		true = self.workpiece2.check_if_workpiece_reaches_its_destination()

		self.assertEqual(false, False)
		self.assertEqual(true, True)
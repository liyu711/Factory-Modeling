import unittest
import numpy
from FactoryModel import *

class FactoryTestCase(unittest.TestCase):
	def setUp(self):
		self.factory = Factory(240, 200, 105, 100)
		self.work_pieces = [
			WorkPiece(2, 2, 0, 0, 3, 3),
			WorkPiece(2, 2, -2, 0, 5, 0)
		]

	def test_arrange(self):
		self.factory.add_workpieces(self.work_pieces)
		cost = self.factory.arrange()
		print(cost)
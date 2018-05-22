from FactoryModel import *
import numpy
import itertools

factory = Factory(240, 200, 105, 100)
assembly_area = AssemblyArea(80,  80,  70, 110)
costs = numpy.array([])
min_cost = 999999999999
min_index = 0
original_work_pieces = [
	WorkPiece(10,   2, 133, 130,  83,  81),
	WorkPiece(10,   2, 143, 130,  48,  81),
	WorkPiece(10,   2, 153, 130,  48, 139),
	WorkPiece(20,  10,  69,  29,  72, 108),
	WorkPiece( 5,  50,  90,  30,  50, 110),
	WorkPiece( 5,  50,  95,  30,  56, 110),
	WorkPiece(20,  20,  60, 170,  95, 112),
	WorkPiece(10,  10,   0, 110, 100, 140),
	WorkPiece(10,  10,   0, 120,  90, 140),
	WorkPiece(10,  10,   0, 130,  80, 140),
	WorkPiece(40,   2, 180, 170,  83,  99),
	WorkPiece(40,   2, 180, 165,  83,  96),
	WorkPiece(40,   2, 180, 160,  83,  93),
	WorkPiece(40,   2, 180, 155,  83,  90),
	WorkPiece(40,   2, 180, 150,  83, 130)
]

work_pieces_combinations = itertools.permutations(original_work_pieces, 15)


for work_pieces in work_pieces_combinations:
	print("processing")
	factory.reset_work_pieces()
	factory.add_workpieces(work_pieces)
	cost = factory.arrange()
	costs = numpy.hstack([costs, cost])

for i in range(len(costs)):
	print("sorting")
	if costs[i] < min_cost:
		min_cost = costs[i]
		min_index = i

print("order =" + work_pieces_combinations[i])
print("least cost =" + min_cost)

factory.reset_work_pieces()
factory.add_workpieces(work_pieces_combinations[i])
factory.sort()
print("Path for every single workpiece")
for work_piece in factory.work_pieces:
	print work_piece.actual_path
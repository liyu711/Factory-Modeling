import numpy
import itertools

stuff = [1,2,3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
items = itertools.permutations(stuff, 15)
for item in items:
	print(item)
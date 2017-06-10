from pareto import point_value_sorter
from random import choice

points = []
for i in range(20):
	x1 = choice(range(10))
	x2 = choice(range(10))
	y1 = choice(range(10))
	y2 = choice(range(10))
	points.append(((x1,x2),(y1,y2)))

#points.sort(point_value_sorter)
sp = sorted(points, cmp=point_value_sorter)
for p in sp:
	print p
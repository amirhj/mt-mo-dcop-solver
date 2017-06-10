# functions work with points with this patern: (values)
def get_pareto_frontier(points):
	return get_pareto_weak_dominators(points)
	
def get_pareto_weak_dominators(points):
	points = sorted(points)
	pareto_frontier = [points[0]]
	for i in range(1, len(points)):
		if is_non_weakly_dominated(pareto_frontier, points[i]):
			pareto_frontier.append(points[i])
	return pareto_frontier

def get_pareto_strict_dominators(points):
	points = sorted(points)
	pareto_frontier = [points[0]]
	for i in range(1, len(points)):
		if is_non_strictly_dominated(pareto_frontier, points[i]):
			pareto_frontier.append(points[i])
	return pareto_frontier

def is_non_weakly_dominated(pareto_frontier, point):
	all_non_dominator = True
	for p in pareto_frontier:
		dominator = True
		for i in range(len(p)):
			if not (p[i] < point[i]):
				dominator = False
				break
		if dominator:
			all_non_dominator = False
			break

	return all_non_dominator
	
def is_non_strictly_dominated(pareto_frontier, point):
	all_non_dominator = True
	for p in pareto_frontier:
		dominator = True
		for i in range(len(p)):
			if not (p[i] <= point[i]):
				dominator = False
				break
		if dominator:
			all_non_dominator = False
			break

	return all_non_dominator

# functions work with points with this patern: ((arguments), (values))
def get_pareto_frontier_by_point(points):
	return get_pareto_weak_dominators_by_point(points)
	
def get_pareto_weak_dominators_by_point(points):
	points = sorted(points, cmp=point_value_sorter)
	pareto_frontier = [points[0]]
	for i in range(1, len(points)):
		if is_non_weakly_dominated_by_point(pareto_frontier, points[i]):
			pareto_frontier.append(points[i])
	return pareto_frontier

def get_pareto_strict_dominators_by_point(points):
	points = sorted(points, cmp=point_value_sorter)
	pareto_frontier = [points[0]]
	for i in range(1, len(points)):
		if is_non_strictly_dominated_by_point(pareto_frontier, points[i]):
			pareto_frontier.append(points[i])
	return pareto_frontier

def is_non_weakly_dominated_by_point(pareto_frontier, point):
	all_non_dominator = True
	for p in pareto_frontier:
		dominator = True
		for i in range(len(p[1])):
			if not (p[1][i] < point[1][i]):
				dominator = False
				break
		if dominator:
			all_non_dominator = False
			break

	return all_non_dominator
	
def is_non_strictly_dominated_by_point(pareto_frontier, point):
	all_non_dominator = True
	for p in pareto_frontier:
		dominator = True
		for i in range(len(p[1])):
			if not (p[1][i] <= point[1][i]):
				dominator = False
				break
		if dominator:
			all_non_dominator = False
			break

	return all_non_dominator

def point_value_sorter(a, b):
	for i in range(len(a[1])):
		if a[1][i] > b[1][i]:
			return 1
		elif a[1][i] < b[1][i]:
			return -1
	return 0
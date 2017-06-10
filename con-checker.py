from functionssg import Functions
from factor_graph import FactorGraph
import sys, json

fg = FactorGraph({'global_state': False})
fg.load('fgsg.json')

func = Functions(fg)

log = json.loads(open(sys.argv[1], 'r').read())

for p in log['path_log'][-1]['pareto']:
	values = {}
	i = 0
	for v in fg.variables:
		values[v] = p[0][i]
		i += 1

	zero = 0
	fv = []
	for i in range(20):
		v = func.calculate('v%d' % i, values)
		if v == 0:
			zero += 1
		fv.append(str(v))

	print 'zeros: %d' % zero
	print ', '.join(fv)
	print
import json
from factor_graph import FactorGraph

r = json.loads(open('results/t0/results.json', 'r').read())

fg = FactorGraph({'global_state':False})

fg.load('fg.json')

co = Constraints(fg)
values = r['path_log'][-1]['variables']

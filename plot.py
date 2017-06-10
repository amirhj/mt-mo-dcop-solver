import matplotlib.pyplot as plt
from math import exp, sqrt
import sys, json
from functions import Functions
from pareto import get_pareto_frontier_by_point
from factor_graph import FactorGraph
import numpy as np
import matplotlib.cm as cm


log = json.loads(open(sys.argv[1], 'r').read())
fg = FactorGraph(log['opt'])
fg.load('fg.json')
func = Functions(fg)
"""
points = []
x = []
y = []

for x0 in fg.variables['v0'].domain:
	for x1 in fg.variables['v1'].domain:
		for x2 in fg.variables['v2'].domain:
			for x3 in fg.variables['v3'].domain:
				for x4 in fg.variables['v4'].domain:
					vars = {'v0':x0, 'v1':x1, 'v2':x2, 'v3':x3, 'v4':x4}
					f1 = func.calculate('f1', vars)
					f2 = func.calculate('f2', vars)
					
					points.append((tuple(vars.values()), (f1, f2)))

					x.append(f1)
					y.append(f2)
 
pareto_frontier = get_pareto_frontier_by_point(points)
xf = []
yf = []
for p in pareto_frontier:
	xf.append(p[1][0])
	yf.append(p[1][1])"""

xp = []
yp = []
colors = []
for p in log['path_log']:
	xp.append(p['functions']['f1'])
	yp.append(p['functions']['f2'])
	#colors.append(p['color'])


#colors = cm.rainbow(np.linspace(0, 1, len(yp)))

#plt.plot(x, y, 'bo')
#plt.plot(xf, yf, 'rs')
fig, ax = plt.subplots()

ax.scatter(xp, yp, c="r", s=450)

#for i in range(len(yp)):
	#ax.annotate(i, (xp[i],yp[i]), size=15, xytext=(1.3, 1.3), textcoords="offset points")
#plt.axis([0,18,0,1.5])
plt.show()

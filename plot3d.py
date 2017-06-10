import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from math import exp, sqrt
import sys, json
from functions import Functions
from pareto import get_pareto_frontier_by_point
from factor_graph import FactorGraph


log = json.loads(open(sys.argv[1], 'r').read())
fg = FactorGraph(log['opt'])
fg.load('fg.json')
func = Functions(fg)

xp = []
yp = []
zp = []
for p in log['path_log']:
	xp.append(p['functions']['f1'])
	yp.append(p['functions']['f2'])
	zp.append(p['functions']['f3'])



fig = plt.figure()
ax = Axes3D(fig)

ax.scatter(xp, yp, zp, c="r", s=30)

for i in range(len(yp)):
	ax.text(xp[i], yp[i], zp[i], '%s' % (str(i)))
#plt.axis([0,18,0,1.5])
plt.show()

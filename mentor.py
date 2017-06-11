from functions import Functions
from random import choice
import sys, os, json
from datetime import datetime
import numpy as np
import matplotlib.cm as cm
from pareto import get_pareto_frontier_by_point

class Mentor:
	def __init__(self, agents, fg, ms, opt):
		self.agents = agents
		self.fg = fg
		self.ms = ms
		self.opt = opt

		self.convergenc_count = 0

		self.path_log = []
		self.pareto_frontier = []

		self.folder = None

		self.start_time = datetime.now()

	def initialize(self):
		self.ms.load(self.agents)


	def run(self):
		# initalizing starting point for agnets
		initial_value_indecies = None
		if self.opt['pf'] is not None: #loading from file
			initial_value_indecies = self.read_pareto_front()
		else:	# choosing ranodm
			initial_value_indecies = {a:choice(range(self.fg.variables[a].domain_size)) for a in self.fg.variables}
		for a in self.agents:
			self.agents[a].set_neighbours_values(initial_value_indecies)

		value_indecies = {k:initial_value_indecies[k] for k in initial_value_indecies}

		for a in self.agents:
			agent = self.agents[a]
			agent.start()
			break

		# running learning episodes
		for e in range(self.opt['learning_episodes']):
			steps = 0
			converged = False
			start_time = datetime.now()
			while not converged:
				# checking convergnece of agents
				converged = True
				for a in self.agents:
					converged &= self.agents[a].is_terminated
					if not converged:
						break
			
			max_clock = 0
			is_overdue = False
			overdue = ''
			for a in self.agents:
				if self.agents[a].clock > max_clock:
					max_clock = self.agents[a].clock
				is_overdue |= self.agents[a].is_overdue
			if is_overdue:
				overdue = '(overdue)'
			print 'Episode %d converged in %d clocks%s.' % (e+1, max_clock, overdue)

			end_time = datetime.now()
			print "The run finished in ", self.duration(start_time, end_time)

			self.write_results()
						

	def apply_actions(self, value_indecies, choosen_actions):
		for v in value_indecies:
			if choosen_actions[v] == 'inc':
				if value_indecies[v] < self.fg.variables[v].domain_size-1:
					value_indecies[v] += 1
			elif choosen_actions[v] == 'dec':
				if value_indecies[v] > 0:
					value_indecies[v] -= 1
		return value_indecies

	def get_values(self, value_indecies):
		values = {}
		for v in value_indecies:
			values[v] = self.fg.variables[v].domain[value_indecies[v]]
		return values

	def get_function_values(self, variables_values):
		values = {}
		calculator = Functions(self.fg)
		for f in self.fg.functions:
			values[f] = calculator.calculate(f, variables_values)
		return values

	def converged(self, new_frontier, old_frontier):
		if set(self.pareto_frontier) == set(new_frontier):
			self.convergenc_count += 1
			if self.convergenc_count == self.opt['convergence']:
				converged = True
				print 'Episode %d converged in %d steps.' % (e, step)
		else:
			self.convergenc_count = 0

	def write_results(self):
		sys.stdout.flush()
		sys.stderr.flush()

		if self.folder is None:
			self.folder = 'results/'+datetime.now().strftime("%Y-%m-%d %H:%M:%S")
			if self.opt['output'] is not None:
				self.folder = 'results/'+self.opt['output']
			os.mkdir(self.folder)

		res = open(self.folder+'/results.json', 'w')
		res.write(json.dumps({'opt':self.opt, 'path_log': self.path_log}))
		res.close()

	def terminate(self):
		for a in self.agents:
			agent = self.agents[a]
			agent.join()

		

		end_time = datetime.now()
		print "The run finished in ", self.duration(self.start_time, end_time)


	def read_pareto_front(self):
		pff = json.loads(open('./'+self.opt['pf'], 'r').read())
		points = []

		variable_indecies = {}
		i = 0
		for v in self.fg.variables.keys():
			variable_indecies[v] = i
			i += 1

		function_indecies = {}
		i = 0
		for f in self.fg.functions.keys():
			function_indecies[f] = i
			i += 1

		for p in pff['path_log'][-1]['pareto']:
			values = {}
			for v in variable_indecies:
				values[v] = p[0][variable_indecies[v]]

			function_values = self.get_function_values(values)

			points.append((tuple(p[0]),tuple(function_values.values())))

		pf = get_pareto_frontier_by_point(points)

		for a in self.agents:
			agent = self.agents[a]
			apf = []
			for p in pf:
				values = {}
				for v in variable_indecies:
					values[v] = p[0][variable_indecies[v]]

				state = [values[a]]
				for n in agent.variable.neighbours:
					state.append(values[n])
				state = tuple(state)

				apf.append((state, agent.get_function_values(state)))

			agent.pareto_frontier = get_pareto_frontier_by_point(apf)

		self.pareto_frontier = pf

		point = {}
		for v in variable_indecies:
			point[v] = pf[0][0][variable_indecies[v]]

		return point

	def duration(self, start_time, end_time):
		time_delta = end_time - start_time
		seconds = time_delta.seconds % 60
		minutes = time_delta.seconds / 60
		hours = minutes / 60
		return "%d days & %d:%d:%d.%d" % (time_delta.days, hours, minutes, seconds, time_delta.microseconds)
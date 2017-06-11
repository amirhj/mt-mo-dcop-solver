import sys, json
from argparser import ArgParser
from factor_graph import FactorGraph
from mentor import Mentor
from agent import Agent
from messageserver import MessageServer

"""opt_pattern = { '--temperature': {'name': 'temperature', 'type': 'float', 'default': 1.0},
				'--test-temperature': {'name': 'test-temperature', 'type': 'float', 'default': 3.0},
				'--decay': {'name': 'decay', 'type': 'float', 'default': 1.0009},
				'--alpha': {'name': 'alpha', 'type': 'float', 'default': 0.9},
				'--gamma': {'name': 'gamma', 'type': 'float', 'default': 0.8},
				'-t': {'name': 'tests', 'type': 'int', 'default': 10},
				'-l': {'name': 'trains', 'type': 'int', 'default': 50},
				'-c': {'name': 'convergence_size', 'type': 'int', 'default': 30},
				'-s': {'name': 'standard_deviation', 'type': 'float', 'default': 1.0},
				'--beta': {'name': 'beta', 'type': 'float', 'default': 0.8},
				}"""
opt_pattern = { '-l': {'name': 'learning_episodes', 'type': 'int', 'default': 1}, 
				'-c': {'name': 'convergence', 'type': 'int', 'default': 5},
				'-m': {'name': 'max_iteration', 'type': 'int', 'default': 0},
				'-g': {'name': 'global_state', 'type': 'bool', 'default': False}, 
				'-o': {'name': 'output', 'type': 'str', 'default': None},
				'-r': {'name': 'log_messages', 'type': 'bool', 'default': False},
				'-p': {'name': 'pf', 'type': 'str', 'default': None}, }

arg = ArgParser(sys.argv[2:], opt_pattern)
opt = arg.read()

fg = FactorGraph(opt)

fg.load(sys.argv[1])

ms = MessageServer(opt)

agents = {}
for v in fg.variables:
	agent = Agent(v, fg, ms, opt)
	agents[v] = agent

ms.load(agents)

mentor = Mentor(agents, fg, ms, opt)

mentor.initialize()
mentor.run()
mentor.terminate()
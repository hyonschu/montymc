### This is a brute force monte carlo simulation to validate the solution to the Monty Hall problem
class montymc(object):

	"""
	### VARIABLES ###
	defaults to:
	montymc(samples=100, simulations=5, doors=3, switch=1)
	
	samples = how many trials to run
	simulations = number of simulations of X samples
	doors = number of doors for the game (default: 3)
	switch dictates what the user does after monty opens the door:
	switch = 0, no switching
	switch = 1, always switch
	switch = 2, random

	### RETURNING RESULTS ###
	.wins returns a list of wins for every simulation
	.totals returns a list of total trials per simulation
	.percentage returns a list of wins/totals per simulation
	.results prints a list of wins, totals & win percentage of each simulation [[wins], [totals], [win percentages]]
	.averages returns a list of the averages of all simulations [ wins, total, win percentage ]


	"""
	
	def __init__(self, samples=100, simulations=5,doors=3, switch=1):
		# print "Ready to go! Run simulations using"
		# print ".simulation(samples, simulations, doors, switch)"
		if doors < 3:
			print "Monty Hall demands at least 3 doors!"
			return
		if switch > 2:
			print "error: switch=0: no switching; 1: always switch; 2: random switch"
			return
		self.samples = samples
		self.simulations = simulations
		self.doors = doors
		self.switch = switch
		self.simuran = 0
		self.run(samples, simulations, doors, switch)


	def run(self, samples, simulations, doors, switch):
		import numpy as np
		import random
		doors = self.doors
		simulations = self.simulations
		switch = self.switch
		simuresults = []#[['wins', 'played', 'win %']]
		for i in range(simulations):
			wins = 0
			total = 0
			for i in range(self.samples):
				alldoors = [ i for i in range(doors) ]
				car = random.randint(0,doors-1)
				guess = random.randint(0,doors-1)
				montydoor = random.randint(0,doors-1)
				while montydoor == car or montydoor == guess:
					montydoor = random.randint(0,doors-1)
					if montydoor > doors:
						return "something went wrong - monty can't open this door"
				alldoors.pop(montydoor)
				newguess = random.randint(0,doors-1)
				if self.switch == 0:
					newguess == guess
				elif self.switch == 1:
					while newguess==guess or newguess==montydoor:
						newguess = random.randint(0,doors-1)
				elif self.switch == 2:
					newguess = alldoors[random.randint(0,len(alldoors)-1)]
				if newguess == car:
					wins += 1
				total += 1

			
			simuresults.append([wins,total,wins*1.00/total])
		self.wins = [i[0] for i in simuresults]
		self.total = [i[1] for i in simuresults]
		self.percentage = [i[2] for i in simuresults]
		self.simuran=1
		self.averages = [np.mean(self.wins), np.mean(self.total), np.mean(self.percentage)]
		self.results = [self.wins, self.total, self.percentage]
		print '\nWin-Percentage of each trial:\n', self.results[2]
		print '\nOverall Win-Percentage:', np.mean(self.results[2])*100, "%"

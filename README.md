# montymc
Monty Hall Monte Carlo simulation

### This is a brute force monte carlo simulation to validate the solution to the Monty Hall problem

### VARIABLES ###
defaults to:
`montymc(samples=100, simulations=5, doors=3, switch=1)`

`samples` = how many trials to run
`simulations` = number of simulations of X samples
`doors` = number of doors for the game (default: 3)
`switch` dictates what the user does after monty opens the door:
switch = `0`, no switching
switch = `1`, always switch
switch = `2`, random

### RETURNING RESULTS ###
`.wins` returns a list of wins for every simulation
`.totals` returns a list of total trials per simulation
`.percentage` returns a list of wins/totals per simulation
`.results` prints a list of wins, totals & win percentage of each simulation [[wins], [totals], [win percentages]]
`.averages` returns a list of the averages of all simulations [ wins, total, win percentage ]

### Usage
`monty = montymc(samples, simulations, doors, switch=1)`

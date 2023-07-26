""" Importing required modules to solve the problem. """
from matplotlib import pyplot as plt
import mains

teams = mains.teams_list
# Calculating total runs scored by each team.
for delivery in mains.deliveries_reader:
    teams[delivery['batting_team']] += int(delivery['total_runs'])
# Plotting the calculated data.
plt.bar(list(teams.keys()), list(teams.values()))
plt.xlabel('Teams')
plt.ylabel('Total Runs')
plt.show()

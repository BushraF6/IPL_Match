#importing required modules.
import mains
from matplotlib import pyplot as plt
teams=mains.teams_list
#Calculating total runs of batting team.
for delivery in mains.deliveries_reader:
    teams[delivery['batting_team']]+= int(delivery['total_runs'])
#Plotting total runs scored by teams.
plt.bar(list(teams.keys()),list(teams.values()))
plt.xlabel=('Teams')
plt.ylabel=('Total Runs')
plt.show()

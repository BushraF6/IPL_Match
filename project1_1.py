import mains
from matplotlib import pyplot as plt
teams=mains.teams_list
for delivery in mains.deliveries_reader:
    teams[delivery['batting_team']]+= int(delivery['total_runs'])
plt.bar(list(teams.keys()),list(teams.values()))
plt.xlabel=('Teams')
plt.ylabel=('Total Runs')
plt.show()
""" Importing the required modules to solve the problem. """
from matplotlib import pyplot as plt
import mains

deliveries = mains.deliveries_reader
matches = mains.matches_reader
teams_extras = mains.teams_list
# Create list to store ids of matches.
ids = []
# Find the ids of matches played in the year 2016.
for match in matches:
    if match['season'] == '2016':
        ids.append(match['id'])
# Calculate extra_runs scored by each team.
for delivery in deliveries:
    if delivery['match_id'] in ids:
        teams_extras[delivery['bowling_team']] += int(delivery['extra_runs'])
# Plotting the calculated data.
plt.bar(list(teams_extras.keys()), list(teams_extras.values()))
plt.xlabel('Teams')
plt.ylabel('Extra_Runs')
plt.show()

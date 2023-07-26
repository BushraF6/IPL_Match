""" Importing the required modules to solve the problem. """
from matplotlib import pyplot as plt
import mains

deliveries = mains.deliveries_reader
matches = mains.matches_reader
# Creating dictionary to store bowlers and total runs.
bowlers = {}
# Creating dictionary to store bowlers and their total overs.
bowler_over = {}
# Creating list to store ids.
ids = []
# Finding ids of matches played in the year 2015.
for match in matches:
    if match['season'] == '2015':
        ids.append(match['id'])
# Calculating total runs, overs for each bowler.
for delivery in deliveries:
    if delivery['match_id'] in ids and delivery['bowler'] not in bowlers:
        bowlers[delivery['bowler']] = 0
        bowler_over[delivery['bowler']] = 0
    if delivery['match_id'] in ids:
        bowlers[delivery['bowler']] += int(delivery['total_runs'])
        bowler_over[delivery['bowler']] += 1
for bowler in bowler_over:
    bowler_over[bowler] = round(bowler_over[bowler]/6, 2)
# Calculating economy rate of each bowlers.
for bowler in bowlers:
    bowlers[bowler] = round(bowlers[bowler]/bowler_over[bowler], 2)
# Sorting bowlers dictionary according to their economy rate.
bowlers = dict(sorted(bowlers.items(), key=lambda x: x[1]))
# Plotting the calculated data of top 10 economical bowlers.
plt.bar(list(bowlers.keys())[:10], list(bowlers.values())[:10])
plt.show()

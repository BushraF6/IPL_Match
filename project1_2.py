""" Import required modules to solve the problem. """
import matplotlib.pyplot as plt
import mains

deliveries = mains.deliveries_reader
# Create dictionary of batsmans with their total runs as values.
batsman_runs = {}
# Calculating runs scored by batsmans of Royal Challengers Bangalore team.
for delivery in deliveries:
    if delivery['batting_team'] == 'Royal Challengers Bangalore':
        if delivery['batsman'] not in batsman_runs:
            batsman_runs[delivery['batsman']] = 0
        batsman_runs[delivery['batsman']] += int(delivery['total_runs'])
# Sorting batsman_runs dictionary according to the values i.e. runs.
batsman = dict(sorted(batsman_runs.items(), key=lambda x: x[1], reverse=True))
# Creating 2 lists of top 10 batsmans and their total runs.
top10_batsman = list(batsman)[:10]
top10_runs = list(batsman.values())[:10]
# PLotting the calculated data.
plt.barh(top10_batsman, top10_runs)
plt.ylabel('Top 10 Batsmans')
plt.xlabel('Runs_Scored')
plt.show()

""" Importing the required modules to solve the problem. """
from matplotlib import pyplot as plt
import mains

matches = mains.matches_reader
teams = list(mains.teams_list)
# Creating years list.
years = sorted([str(i) for i in range(2008, 2018)])
# Creating dictionary to store matches won by each team per year.
won_matches = {}
# Updating the won_matches dictionary with year and team dictionary.
for year in years:
    for team in teams:
        if year not in won_matches:
            won_matches.update({year: {team: 0}})
        else:
            won_matches[year].update({team: 0})
# Calculate matches won by each team per year.
for match in matches:
    if match['winner']:
        won_matches[match['season']][match['winner']] += 1
# Creating list of no: of matches won.
won_l = []
for team in teams:
    won = []
    for year in years:
        won.append(won_matches[year][team])
    won_l.append(won)
# Plotting the calculated data.
colour = ['r', 'b', 'g', 'y', 'm', 'c', 'pink', 'purple', 'grey', 'brown', 'y', 'm', 'r']
plt.bar(years, won_l[0], color='k')
for i in range(1, len(won_l)):
    plt.bar(years, won_l[i], bottom=won_l[i-1], color=colour[i-1])
plt.xlabel("Years")
plt.ylabel("No: of matches won")
plt.legend(teams)
plt.show()

""" Importing the required modules to solve the problem. """
from matplotlib import pyplot as plt
import mains

matches = mains.matches_reader
teams = list(mains.teams_list)
# Creating years list.
years = sorted([str(i) for i in range(2008, 2018)])
# Creating dictionary to store matches played by each team per year.
total_matches = {}
# Updating the total_matches dictionary with year and team dictionary.
for year in years:
    for team in teams:
        if year not in total_matches:
            total_matches.update({year: {team: 0}})
        else:
            total_matches[year].update({team: 0})
# Calculate matches played by each team per year.
for match in matches:

    total_matches[match['season']][match['team1']] += 1
    total_matches[match['season']][match['team2']] += 1
# Creating list of no: of matches played.
total_c = []
for team in teams:
    play = []
    for year in years:
        play.append(total_matches[year][team])
    total_c.append(play)
# Plotting the calculated data.
colour = ['r', 'b', 'g', 'y', 'm', 'c', 'pink', 'purple', 'grey', 'brown', 'y', 'm', 'r']
plt.bar(years, total_c[0], color='k')
count = total_c[0]
for i in range(1, len(total_c)):
    plt.bar(years, total_c[i], bottom=total_c[i-1], color=colour[i-1])
plt.xlabel("Years")
plt.ylabel("No: of matches")
plt.legend(teams)
plt.show()

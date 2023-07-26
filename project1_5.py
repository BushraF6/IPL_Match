""" Import the required modules to solve the problem. """
from matplotlib import pyplot as plt
import mains

matches = mains.matches_reader
# Creating dictionary of years with default value 0.
year_match_count = {str(i): 0 for i in range(2008, 2018)}
# Calculate total matches played per year.
for match in matches:
    year_match_count[match['season']] += 1
# Creating 2 lists for storing the years and matches_count.
matches_count = list(year_match_count.values())
years = list(year_match_count.keys())
# Plotting the calculated data.
plt.bar(years, matches_count)
plt.xlabel('Year')
plt.ylabel('No: of Matches played')
plt.show()

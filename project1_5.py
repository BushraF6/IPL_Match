import csv
from matplotlib import pyplot as plt

year_match_count={str(i):0 for i in range(2008,2018)}
with open('matches.csv','r') as matchesfile:
    mathches_reader= csv.DictReader(matchesfile) 
    for match in mathches_reader:
        year_match_count[match['season']]+=1
matches_count=list(year_match_count.values())
years=list(year_match_count.keys())

plt.bar(years,matches_count)
plt.xlabel('Year')
plt.ylabel('No: of Matches played')
plt.show()
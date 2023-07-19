import mains
from matplotlib import pyplot as plt

deliveries=mains.deliveries_reader
matches=mains.matches_reader
teams_extra_runs=mains.teams_list
ids=[]
for match in matches:
        if match['season']== '2016':
                ids.append(match['id'])
for delivery in deliveries:
        if delivery['match_id'] in ids:
                teams_extra_runs[delivery['batting_team']]+=int(delivery['extra_runs'])
plt.barh(list(teams_extra_runs.keys()),list(teams_extra_runs.values()))
plt.show()
import mains
from matplotlib import pyplot as plt

deliveries=mains.deliveries_reader
matches=mains.matches_reader
bowlers={}
ids=[]
for match in matches:
        if match['season']== '2015':
                ids.append(match['id'])
for delivery in deliveries:
   if delivery['match_id'] in ids and delivery['bowler'] not in bowlers:
        bowlers[delivery['bowler']]=0
   if delivery['match_id'] in ids:
        bowlers[delivery['bowler']]+=int(delivery['total_runs'])
for bowler in bowlers:
      bowlers[bowler]=round(bowlers[bowler]/6,2)
bowlers= dict(sorted(bowlers.items(), key=lambda x:x[1], reverse=True))
plt.bar(list(bowlers.keys())[:10],list(bowlers.values())[:10])
plt.show()
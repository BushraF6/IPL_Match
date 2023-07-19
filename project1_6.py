from matplotlib import pyplot as plt
import mains

matches=list(mains.matches_reader)
team=list(mains.teams_list)

years=sorted([str(i) for i in range(2008,2018)])
total_matches = {} 
for i in team:
    for j in years:
        if i not in total_matches.keys():
            total_matches.update({i: {j:0}})
        else:
            total_matches[i].update({j:0})

for i in range(len(matches)):
    if matches[i]['winner']:
        total_matches[matches[i]['winner']][matches[i]['season']]+= 1

won_l=[]
for j in years:
    won=[]
    for i in team:
        won.append(total_matches[i][j])
    won_l.append(won)
print(won_l)

colour=['r','b','g','y','m','c','pink','purple','grey','brown','y','m','r']

plt.bar(team,won_l[0],color='k')
for i in range(1,len(won_l)):
    plt.bar(team,won_l[i],bottom=won_l[i-1],color=colour[i-1])

plt.xlabel("Teams")
plt.ylabel("No: of matches won")
plt.legend(years)
plt.show()
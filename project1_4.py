from matplotlib import pyplot as plt
import mains

matches=mains.matches_reader
teams=list(mains.teams_list)

years=sorted([str(i) for i in range(2008,2018)])
total_matches = {} 
for team in teams:
    for year in years:
        if team not in total_matches.keys():
            total_matches.update({team: {year:0}})
        else:
            total_matches[team].update({year:0})

for match in matches:

    total_matches[match['team1']][match['season']]+= 1
    total_matches[match['team2']][match['season']]+= 1

total_c=[]
for year in years:
    play=[]
    for team in teams:
        play.append(total_matches[team][year])
    total_c.append(play)


colour=['r','b','g','y','m','c','pink','purple','grey','brown','y','m','r']

plt.bar(teams,total_c[0],color='k')
count=total_c[0]
for i in range(1,len(total_c)):
    plt.bar(teams,total_c[i],bottom=total_c[i-1],color=colour[i-1])

plt.xlabel("Teams")
plt.ylabel("No: of matches")
plt.legend(years)
plt.show() 

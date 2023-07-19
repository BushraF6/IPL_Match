import matplotlib.pyplot as plt
import csv

with open('deliveries.csv','r', encoding='utf-8') as deliveries_file:
    batsman_list=[]
    batsman_runs_list=[]
    batsman_runs=[]
    deliveries_reader= csv.DictReader(deliveries_file)
    for deliveries in deliveries_reader:
        if deliveries['batting_team']=='Royal Challengers Bangalore':
            if deliveries['batsman'] not in batsman_list :
                batsman_list.append(deliveries['batsman'])
            batsman_runs_list.append([deliveries['batsman'],deliveries['batsman_runs']])
    for batsman in batsman_list:
        sums=0
        for batsman1 in batsman_runs_list:
            if batsman1[0]==batsman:
                sums+=int(batsman1[1])
        batsman_runs.append(sums)
    batsman= {k: v for k, v in zip(batsman_list, batsman_runs)}
    batsman= dict(sorted(batsman.items(), key=lambda x:x[1], reverse=True))
    top10_batsman=list(batsman)[:10]
    top10_runs=list(batsman.values())[:10]
    print(top10_batsman)
    print(top10_runs)

plt.barh(top10_batsman,top10_runs)
plt.show()
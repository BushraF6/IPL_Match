import csv

deliveriesfile=open('deliveries.csv', 'r', encoding= 'utf8')
deliveries_reader= csv.DictReader(deliveriesfile)
teams_list={'Sunrisers Hyderabad': 0, 
            'Royal Challengers Bangalore': 0, 
            'Mumbai Indians': 0, 
            'Rising Pune Supergiant': 0, 
            'Gujarat Lions': 0, 
            'Kolkata Knight Riders': 0, 
            'Kings XI Punjab': 0, 
            'Delhi Daredevils': 0, 
            'Chennai Super Kings': 0, 
            'Rajasthan Royals': 0, 
            'Deccan Chargers': 0, 
            'Kochi Tuskers Kerala': 0, 
            'Pune Warriors': 0, 
            'Rising Pune Supergiants': 0}

matchesfile= open('matches.csv', 'r', encoding='utf8')
matches_reader=csv.DictReader(matchesfile)


import csv
from matplotlib import pyplot as plt

umpires_country={}
with open('umpires.csv','r') as umpiresfile:
    umpire_reader=csv.DictReader(umpiresfile)
    for umpire in umpire_reader:
        if umpire[' country'] not in umpires_country:
            umpires_country[umpire[' country']]=0
        umpires_country[umpire[' country']]+=1
    del(umpires_country[' India'])
plt.bar(list(umpires_country.keys()),list(umpires_country.values()))
plt.xlabel,plt.ylabel=('Countries'),('No: of umpires')
plt.show()
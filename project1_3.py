""" Importing required modules to solve the problem. """
import csv
from matplotlib import pyplot as plt

# Create dictionary to store no: of umpires from each country.
umpires_country = {}
# Extracting data from umpires.csv file.
with open('umpires.csv', 'r', encoding='utf-8') as umpiresfile:
    umpire_reader = csv.DictReader(umpiresfile)
    # Calculate no: of umpires from each country except India.
    for umpire in umpire_reader:
        if umpire[' country'] not in umpires_country:
            umpires_country[umpire[' country']] = 0
        umpires_country[umpire[' country']] += 1
    del umpires_country[' India']
# Plot the calculated data.
plt.bar(list(umpires_country.keys()), list(umpires_country.values()))
plt.xlabel('Countries')
plt.ylabel('No_of_Umpires')
plt.show()

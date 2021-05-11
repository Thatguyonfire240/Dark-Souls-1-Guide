import csv

filename="Sorceries_Wisdom_of_a_Sage.csv"
Sorceries_Wisdom_of_a_Sage = {}
with open(filename, 'r') as data:
    for line in csv.DictReader(data):
        Sorceries_Wisdom_of_a_Sage = line
        print(Sorceries_Wisdom_of_a_Sage)
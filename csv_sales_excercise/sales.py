import csv

line_counter = 1
counter_europe = 0
units_soldes = 0
"""Wue use a dictionary to colec the item type"""
unique_types = {}

with open ("Sales_Records.csv", 'rt') as f:
    reader = csv.reader(f)
    for row in reader:
        if line_counter == 1:
            pass
        else:
            units_soldes += int(row[8])
            unique_types[row[2]] = row[2]
            if row[0] == "Europe":
                counter_europe += 1
        line_counter += 1

print("Order records from Europe: {0}".format(counter_europe))
print("Total Units Sold: {0}".format(units_soldes))
print("The list of Types of Items is:")
for x in unique_types:
    print("- " + x)


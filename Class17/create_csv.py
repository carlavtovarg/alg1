import csv
#file
#create csv object (.writer)
csv_data = [["Student", "Grade"], [12245, "A"]]

csv.register_dialect('myDialect',
quoting=csv.QUOTE_NONNUMERIC,
skipinitialspace=True, lineterminator="\n")

with open('person.csv', 'w') as f:
    writer = csv.writer(f, dialect='myDialect')
    for row in csv_data:
        writer.writerow(row)


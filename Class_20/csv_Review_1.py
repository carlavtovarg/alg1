import csv

line_counter = 0
total_ages = 0
"""Wue use a set to colec the item type"""
Female = 0
Male = 0
average_age = 0
percent_f = 0
percent_m = 0

with open ("biostats.csv", 'rt') as f:
    reader = csv.reader(f)
    """The next line move the reader to the second register in the file"""
    next(reader)
    for row in reader:
        total_ages += int(row[2])
        if row[1] == "F":
            Female += 1
        else:
            Male += 1
        line_counter += 1
    average_age = total_ages/line_counter


print("The Average Age is: {0:.2f}".format(average_age))
print("The percent of Male is: {0:.2f}".format(Male*100/line_counter))
print("The percent of Female is: {0:.2f}".format(Female*100/line_counter))


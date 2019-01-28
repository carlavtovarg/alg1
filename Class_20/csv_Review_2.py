import csv
line_counter = 1
cm_convert = 2.54
Kg_convert = 0.453592
line = []
with open ("biostats.csv", 'rt') as f:
    reader = csv.reader(f)
    """The next line move the reader to the second register in the file"""
    next(reader)
    with open('biostats1.csv', 'w') as f:
        writer = csv.writer(f)
        for row in reader:
            line = []
            height = 0
            weight = 0
            if line_counter==1:
                header = "Name,Sex,Age,Height(cm),Weight(Kg)"
                #line.app "Name"

                #line[1] = "Sex"
                #line[2] = "Age"
                #line[3] = "Height(cm)"
                #line[4] = "Weight(Kg)"
            else:
                height = float(row[2]) * cm_convert
                weight = float(row[3]) * Kg_convert
                line.append(row[0])
                line.append(row[1])
                line.append(row[2])
                line.append(round(height, 2))
                line.append(round(weight, 2))

            line_counter += 1
            #for row in line:
             #   writer.writerow(row)
            writer.writerow(line)



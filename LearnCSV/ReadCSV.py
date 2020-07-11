import csv

with open('testleaf.csv') as fi:
    values= csv.reader(fi)
    print(type(values))

    # for row in values:
    #     for column in row:
    #         print(column)

    for row in values:
        print(row[0].ljust(3), row[1].ljust(10), row[2])
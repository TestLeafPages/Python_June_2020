import csv

with open('studentinfo.csv') as f:
    values = csv.DictReader(f)
    print(type(values))
    for key in values:
        print(key['R_no'].ljust(15), key['f_name'].ljust(10), key['l_name'])
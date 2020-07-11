import csv

with open("WriteCSV.csv", 'w') as f:
    write = csv.writer(f)

    header = [['S_NO', 'UserName', 'Email']]
    write.writerows(header)

    data = [
        ['001', 'Gopinath', 'Jayakumar'],
        ['002', 'Balaji', 'M'],
        ['003', 'Divya', 'Z']
    ]

    write.writerows(data)
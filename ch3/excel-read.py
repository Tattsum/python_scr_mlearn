import sys
sys.path.append('/usr/local/lib/python3.5/dist-packages')

import openpyxl

filename = "population.xlsx"
book = openpyxl.load_workbook(filename)

sheet = book.worksheets[0]

data = []

for row in sheet.rows:
    data.append([
        row[0].value,
        row[2].value
    ])

del data[0]

data = sorted(data, key=lambda x:x[1])

for i,a in enumerate(data):
    if(i>=5):
        break
    print(i+1,a[0],int(a[1]))

    

import sys
sys.path.append('/usr/local/lib/python3.5/dist-packages')

import openpyxl

filename = "population.xlsx"
book = openpyxl.load_workbook(filename)

sheet = book.active

total = 0
for i, row in enumerate(sheet.rows):
    if i == 0:
        continue
    po = int(row[2].value)
    total += po
print("total=",total)

sheet['A49'] = 'Total'
sheet['C49'] = total

c = sheet['C49']
c.font = openpyxl.style.Fonr(size=14,color="FF0000")
c.number_format = sheet['C48'].number_format

filename = "population-total.xlsx"
book.save(filename)
print("OK")

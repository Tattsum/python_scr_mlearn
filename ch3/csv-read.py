import sys
sys.path.append('/usr/local/lib/python3.5/dist-packages')

import codecs

filename = "list-sjis.csv"
csv = codecs.open(filename,"r","shift_jis").read()

data = []
rows = csv.split("\r\n")
for row in rows:
    if row == "":
        continue
    cells = row.split(",")
    data.append(cells)

for c in data:
    print (c[1],c[2])

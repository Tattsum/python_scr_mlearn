import sys
sys.path.append('/usr/local/lib/python3.5/dist-packages')

import csv, codecs

filename = "list-sjis.csv"
fp = codecs.open(filename,"r","shift_jis")

reader = csv.reader(fp, delimiter=",", qutechar='"')
for cells in reader:
    print(cells[1],cells[2])

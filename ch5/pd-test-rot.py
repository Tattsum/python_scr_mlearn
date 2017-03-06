import sys
sys.path.append('/usr/local/lib/python3.5/dist-packages')

import pandas as pd
tbl = pd.DataFrame([
    ["A", "B", "C"],
    ["D", "E", "F"],
    ["G", "H", "I"]
])
print(tbl)
print("---")
print(tbl.T)

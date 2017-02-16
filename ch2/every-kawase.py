import sys
sys.path.append('/usr/local/lib/python3.5/dist-packages')

import urllib.request as request
import datetime
import json

API = "http://api.aoikujira.com/kawase/get.php?code=USD&format=json"
json_str = request.urlopen(API).read().decode("utf-8")
data = json.loads(json_str)
print ("1USD="+data["JPY"]+"JPY")

t = datetime.date.today()

fname = t.strftime("%Y-%m-%d") + ".json"
with open(fname,"w",encoding="utf-8") as f:
    f.write(json_str)

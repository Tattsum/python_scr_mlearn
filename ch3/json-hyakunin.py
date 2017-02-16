import sys
sys.path.append('/usr/local/lib/python3.5/dist-packages')

import urllib.request as req
import os.path,random
import json

url = "http://api.aoikujira.com/hyakunin/get.php?fmt=json"
savename = "hyakunin.json"
if not os.path.exists(url):
    req.urlretrieve(url,savename)

data = json.load(open(savename,"r",encoding="utf-8"))

# s = open(savename,"r",encoding="utf-8").read()
# data = json.loads(s)

r = random.choice(data)
print(r['kami'],r['simo'])

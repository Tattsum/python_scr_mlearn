import sys
sys.path.append('/usr/local/lib/python3.5/dist-packages')

import json

price = {
    "data":"2017-05-10",
    "price":{
        "Apple": 80,
        "Orange":55,
        "Banana":40,
    }
}

s = json.dumps(price)
print(s) 

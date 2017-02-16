import sys
sys.path.append ('/usr/local/lib/python3.4/dist-packages')
import requests
r = requsets.get("http://uta.pw/shodou/img/3/3.png")

with open("test.png","wb") as f:
    f.write(r.content)

print("saved")

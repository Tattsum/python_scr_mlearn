import sys
sys.path.append ('/usr/local/lib/python3.4/dist-packages')
import requests
r = requsets.get("http://api.aoikujira.com/time/get.php")

text = r.text
print(text)

bin = r.content
print (bin)

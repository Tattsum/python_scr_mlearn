import sys
import urllib.request as req
import urllib.parse as parse

if len(sys.argv) <= 1:
        print("USAGE: hyakunin.py (keyword)")
        sys.exit()
keyword = sys.argv[1]

API = "http://api.aoikujira.com/hyakunin/get.php"
query = {
        "fmt": "ini",
        "key": keyword
}

parms = parse.urlencode(query)
url = API + "?" + parms
print("url=",url)

with req.urlopen(url) as r:
        b = r.read()
        data = b.decode("utf-8")
        print(data)

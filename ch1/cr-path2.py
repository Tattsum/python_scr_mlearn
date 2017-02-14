import sys
sys.path.append ('/usr/local/lib/python3.4/dist-packages')
from urllib.parse import urljoin

base = "http://example.com/html/a.html"

print( urljoin(base,"/hoge.html"))
print( urljoin(base,"http://kujirahand.com/wiki"))
print( urljoin(base,"//uta.pw/shodou"))

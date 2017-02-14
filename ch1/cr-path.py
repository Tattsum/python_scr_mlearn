import sys
sys.path.append ('/usr/local/lib/python3.4/dist-packages')
from urllib.parse import urljoin

base = "http://example.com/html/a.html"

print( urljoin(base,"b.html"))
print( urljoin(base,"sub/c.html"))
print( urljoin(base,"../index.html"))
print( urljoin(base,"../img/hoge.png"))
print( urljoin(base,"../css/hoge.css"))

import sys
sys.path.append ('/usr/local/lib/python3.4/dist-packages')
from bs4 import BeautifulSoup

html = """
<html>
  <body>
    <h1 id = 'title'>スクレイピングとは？</h1>
    <p id = 'body'>webページから任意のデータを抽出すること</p>
  </body>
</html>"""

soup = BeautifulSoup(html,'html.parser')

title = soup.find(id = 'title')
body = soup.find(id = 'body')
print ("#title="+title.string)

print ("#body="+body.string)

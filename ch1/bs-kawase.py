import sys
sys.path.append ('/usr/local/lib/python3.4/dist-packages')
from bs4 import BeautifulSoup
import urllib.request as req

url = "http://api.aoikujira.com/kawase/xml/usd"
res = req.urlopen(url)

soup = BeautifulSoup(res,'html.parser')

jpy = soup.select_one("jpy").string
print ("usd/jpy=",jpy)

import sys
sys.path.append ('/usr/local/lib/python3.4/dist-packages')
from bs4 import BeautifulSoup4
import urllib.request
import urllib.parse 
from os import makedirs
import os.path,time,re

proc_files = {}

def enum_links(html,base):
    soup = BeautifulSoup(html,"html.parser")
    links = soup.select("link[rel='stylesheet']")
    links += soup.select("a[href]")
    result = []

    for a in links:
        href = a.attrs['href']
        url = urljoin(base,href)
        result.append(url)
    return result

def download_file(url):
    o = urlparase(url)
    savepath = "./" + o.netloc +o.path
    if re.search(r"/$",savepath):
        savepath += "index.html"
    savedir = os.path.dirname(savepath)
    if os.path.exists(savepath):
        return savepath
    if not os.path.exists(savedir):
        print ("mkdir=",savedir)
        makedirs(savedir)

    try:
        print("download=",url)
        urlretrieve(url,savepath)
        time.sleep(1)
        return savepath
    except:
        print ("ダウンロード失敗：",url)
        return None

def analize_html(url,root_url):
    savepath = download_file(url)
    if savepath is None:
        return
    if savepath in proc_files:
        return
    proc_files[savepath] = True
    print ("analize_html=",url)

    html = open(savepath,"r",encoding="utf-8").read()
    links = enum_links(html,url)

    for link_url in links:
        if link_url.find(root_url) != 0:
            if not re.search(r".css$",link_url):
                continue
        if re.search(r".(html|htm)$",link_url):
            analize_html(link_url,root_url)
            continue
    download_file(link_url)

if __name__ == "__maim__":
    url = "http://docs.python.jp/3.5/library"
    analize_html(url,url)

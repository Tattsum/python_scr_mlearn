import sys
sys.path.append('/usr/local/lib/python3.5/dist-packages')

from selenium import webdriver

browser = webdriver.PhantomJS()
browser.implicitly_wait(3)

browser.get("https://google.com")

r = browser.execute_script("return 100 + 50")
print (r)

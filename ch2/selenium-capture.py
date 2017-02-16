import sys
sys.path.append('/usr/local/lib/python3.5/dist-packages')

from selenium import webdriver

url = "https://www.aozora.gr.jp/cards/000081/files/46268_23911.html"

browser = webdriver.PhantomJS()

browser.implicitly_wait

browser.save_screenshot("Website.png")

browser.quit()

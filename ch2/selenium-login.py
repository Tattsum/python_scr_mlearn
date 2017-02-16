import sys
sys.path.append('/usr/local/lib/python3.5/dist-packages')

from selenium import webdriver

USER = "JS-TESTER"
PASS = "ipCU12ySxI"

browser = webdriver.PhantomJS()
browser.implicitly_wait(3)

url_login = "http://uta.pw/sakusibbs/users.php?action=login"
browser.get(url_login)
print ("ログインページにアクセスしました")

e = browser.find_element_by_id("USER")
e.clear()
e.send_keys(USER)
e = browser.find_element_by_id("PASS")
e.clear()
e.send_keys(PASS)

frm = browser.find_element_by_css_selector("#loginForm form")
frm.submit()
print("情報を入力してログインボタンを押しました")

a = browser.find_element_by_css_selector(".islongin a")
url_mypage = a.get_attribute('href')
print ("マイページのURL=",url_mypage)

browser.get(url_mypage)

links = browser.find_element_by_css_selector("#favlist li > a")
for a in links:
    href = a.get_attribute('href')
    title = a.text
    print ("-",title,">",href)

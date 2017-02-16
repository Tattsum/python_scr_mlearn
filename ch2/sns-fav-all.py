import sys
sys.path.append('/usr/local/lib/python3.5/dist-packages')

from selenium import webdriver
import time

USER = "JS-TESTER"
PASS = "ipCU12ySxI"
FAV_USER_ID = 32
SNS_URL = "http://uta.pw/sakusibbs/"

browser = webdriver.PhantomJS()
browser.implicitly_wait(3)

url_login = SNS_URL + "users.php?action=login"
browser.get(url_login)

def form_post(frm,d):
    for field, value in d.items():
        e = frm.find_element_by_name(field)
        e.clear()
        e.send_keys(value)
    frm.submit

frm = browser.find_element_by_css_selector("#loginForm form")

form_post(frm,{
    "username_mmlbbs6":USER,
    "password_mmlbbs6":PASS
    })

browser.save_screenshot("sns-logined.png")

e = browser.find_element_by_id("bbsheader")
html = e.get_attribute("innerHTML")
if html.find("action=logout") < 0:
    print ("ログインできていません")
    quit()
print ("+ ログインできました")
time.sleep(1)

url = SNS_URL + "users.php?user_id=" + str(FAV_USER_ID)
browser.get(url)

sakuhin_list = []
links = browser.find_element_by_css_selector("ul#mmlist li a")
for a in links:
    href = a.get_attribute('href')
    title = a.text
    sakuhin_list.append((href,title))
print("+作品の一覧を{0}件取得しました".format(len(sakuhin_list)))

for href, title in sakuhin_list:
    print("- ",title)
    browser.get(href)
    try:
        e = browser.find_element_by_id("fav_add_btn")
        e.click()
        # e = browser.find_element_by_id("fav_remove_btn")
        # e.click()
        print("| お気にしました")
    except:
        print ("| すでにお気に入りでした")
    time.sleep(1)

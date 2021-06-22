from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import  By
import time
from bs4 import BeautifulSoup
import requests
import re
if __name__ == "__main__":
    account = input("Enter your account:") # 輸入帳號
    password = input("Enter your password") # 輸入密碼
    browser = webdriver.Chrome() # 使用套件
    url = 'https://chat.line.biz/Uaed3a1d4437043c1267820336b78d834' #line official account url
    browser.get(url)
    test = browser.find_element_by_css_selector('input.btn.btn-lg.btn-block.btn-primary') # 找到頁面的綠色按鈕
    test.click() # 點選按鈕
    time.sleep(2) #等待頁面跳轉
    user = browser.find_element_by_name('tid') #帳號欄位
    user.send_keys(account) #自動輸入帳號
    password = browser.find_element_by_name('tpasswd') #密碼欄位
    password.send_keys(password) #自動輸入密碼

    button = browser.find_element_by_css_selector('button.MdBtn01') #登入按鈕
    button.click() #按下按鈕

    time.sleep(8) #頁面跳轉
    response = requests.get(
        "https://chat.line.biz/Uaed3a1d4437043c1267820336b78d834/chat/Ua690a0a03266b696753db65462a64bfe") #跳轉頁面
    responseh = BeautifulSoup(browser.page_source, "html.parser") #排版問題
    if (browser.find_element_by_class_name('close')):  # 若跳出提示視窗就按關閉
        browser.find_element_by_class_name('close').click() #防止跳出不必要的視窗
    # 找到客戶要修改或擷取的元件 (可更改) 這裡以更改客戶標籤為例
    find = responseh.find_all('a',class_='list-group-item list-group-item-action d-flex flex-nowrap list-group-item-chat border-0')
    time.sleep(3)
    div_top = browser.find_element_by_css_selector('div.list-group.list-group-flush')
    all_chat_list = div_top.find_element_by_tag_name('a')
    count = 0
    for item in find: # 找出h6 並自動點選button
        name = item.find('h6')
        if name.text[0] != '0':
            a_btn = div_top.find_element_by_tag_name('a')
            a_btn[count].click()
            time.sleep(2)
            print(name.text)
        count += 1



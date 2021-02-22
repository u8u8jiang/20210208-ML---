# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 22:04:33 2021

@author: she84
"""

from igramscraper.instagram import Instagram 
import csv


proxies = {
    '192.168.43.249'
}

instagram = Instagram()
instagram.set_proxies(proxies)

account = instagram.get_account('jjr_yaya')

# # Available fields
# print('Account info:')
# print('Id: ', account.identifier)
# print('Username: ', account.username)
# print('Full name: ', account.full_name)
# print('Biography: ', account.biography)
# print('Profile pic url: ', account.get_profile_picture_url())
# print('External Url: ', account.external_url)
# print('Number of published posts: ', account.media_count)
# print('Number of followers: ', account.followed_by_count)
# print('Number of follows: ', account.follows_count)
# print('Is private: ', account.is_private)
# print('Is verified: ', account.is_verified)

# or simply for printing use 
print(account)


with open('Account info.csv', 'w', newline='',encoding="utf-8") as csvfile:
  writer = csv.writer(csvfile, delimiter=';')
  # writer.writerow([account])
  writer.writerow(['identifier','username','full_name',
                   'profile_picture_url',
                   'external_url','media_count',
                   'followed_by_count','follows_count',
                   'account.is_private','account.is_verified'])
  writer.writerow([account.identifier, account.username, account.full_name, 
                   account.get_profile_picture_url(),
                   account.external_url, account.media_count,
                   account.followed_by_count, account.follows_count,
                   account.is_private, account.is_verified])

#==========================================================#

from igramscraper.instagram import Instagram 

proxies = {
    '192.168.43.249'
}

instagram = Instagram()
instagram.set_proxies(proxies)

account = instagram.get_account('itsgeenatime')

# Available fields
print('Account info:')
print('Id: ', account.identifier)
print('Username: ', account.username)
print('Full name: ', account.full_name)
print('Biography: ', account.biography)
print('Profile pic url: ', account.get_profile_picture_url())
print('External Url: ', account.external_url)
print('Number of published posts: ', account.media_count)
print('Number of followers: ', account.followed_by_count)
print('Number of follows: ', account.follows_count)
print('Is private: ', account.is_private)
print('Is verified: ', account.is_verified)

# or simply for printing use 
print(account)



#==========================================================#



# 爬取IG貼文短連結
# https://medium.com/marketingdatascience/%E8%B7%9F%E8%91%97ig%E6%BD%AE%E6%B5%81%E4%BE%86%E7%88%AC%E8%9F%B2-%E5%A6%82%E4%BD%95%E7%88%AC%E5%8F%96ig%E8%B2%BC%E6%96%87%E7%9F%AD%E9%80%A3%E7%B5%90-%E7%B3%BB%E5%88%972-%E9%99%84python%E7%A8%8B%E5%BC%8F%E7%A2%BC-465b7f00eeee

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as Soup
import time


options = Options()
options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
browser = webdriver.Chrome(chrome_options = options, executable_path=r'C:\\Users\\she84\\anaconda3\\chromedriver.exe')
url = 'https://www.instagram.com/itsgeenatime/'
browser.get(url) # 前往該網址


# 往下滑並取得新的貼文連結
n_scroll = 5
post_url = []
for i in range(n_scroll):
    scroll = 'window.scrollTo(0, document.body.scrollHeight);'
    browser.execute_script(scroll)
    html = browser.page_source
    soup = Soup(html, 'lxml')

    # 尋找所有的貼文連結
    for elem in soup.select('article div div div div a'):
        # 如果新獲得的貼文連結不在列表裡，則加入
        if elem['href'] not in post_url:
            post_url.append(elem['href'])
    time.sleep(2) # 等待網頁加載

# 總共加載的貼文連結數
print("總共取得 " + str(len(post_url)) + " 篇貼文連結")


#==========================================================#



# 開始爬取貼文讚數及留言數
# https://aitmr1234567890.medium.com/%E8%B7%9F%E8%91%97ig%E6%BD%AE%E6%B5%81%E4%BE%86%E7%88%AC%E8%9F%B2-%E5%A6%82%E4%BD%95%E7%88%AC%E5%8F%96ig%E8%B2%BC%E6%96%87%E8%AE%9A%E6%95%B8-%E7%95%99%E8%A8%80%E6%95%B8-%E7%B3%BB%E5%88%973-%E9%99%84python%E7%A8%8B%E5%BC%8F%E7%A2%BC-4ac918b8fef4

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


# 進入到粉專的頁面

options = Options()
options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
browser = webdriver.Chrome(chrome_options = options, executable_path=r'C:\\Users\\she84\\anaconda3\\chromedriver.exe')
url = 'https://www.instagram.com/itsgeenatime/'
browser.get(url) # 前往該網址

post_url = 'p/CLPHcMqjv8j/'



find = False
# 不在目前的網頁元素裡，則往下滑，加載新貼文
while not find:
    try:
        # 找到對應的貼文，鼠標移入
        post_elem = browser.find_element_by_xpath('//a[@href="'+str(post_url)+'"]')
        action = ActionChains(browser)
        action.move_to_element(post_elem).perform()
        # 找到需要的網頁元素
        n_like_elem = browser.find_elements_by_class_name('-V_eO')
        # 取得讚數、留言數
        n_like = n_like_elem[0].text
        n_comment = n_like_elem[1].text
        # 找到之後就可以回傳‘找到了’
        find = True
    except:
        # 找不到就往下滑
        scroll = 'window.scrollBy(0,250)'
        browser.execute_script(scroll)
        continue
        



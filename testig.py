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


from selenium import webdriver
from bs4 import BeautifulSoup as Soup
import time

browser = webdriver.Chrome()  
url = 'https://www.instagram.com/jjr_yaya/'
browser.get(url) # 前往該網址










from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# 進入到粉專的頁面
# browser = webdriver.Chrome()  
url = 'https://www.instagram.com/jjr_yaya/'
browser.get(url) # 前往該網址

# post_url = '/p/CEriQnOMwW9/'
post_url = 'p/CJiw6v4MXTkuXmZthbXdXJRadDeG8NKhfg5-9k0/'
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
        

















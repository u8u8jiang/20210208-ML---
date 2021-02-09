# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 11:06:51 2021

@author: T30518
"""

#網路連線
import urllib .request as request

 #將首頁資料存入data(16進制) note.標籤、屬性
src="https://duckjiang.wordpress.com/"  
with request.urlopen(src)as response:
    data=response.read() 
    data=response.read().decode("utf-8") #utf-8解碼
print(data)

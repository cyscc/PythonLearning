# @createTime : 2022/3/17
# @authorName : cyss
# @fileName : beautifulSoupTest.py
# @description : beautifulsoup 测试
import urllib.request
from urllib import *
from bs4 import BeautifulSoup
import re

url = "http://www.baidu.com"
response = urllib.request.urlopen(url)
html = response.read().decode("utf-8")

bs = BeautifulSoup(html, "html.parser")

# find_all
# t_list = bs.find_all("a")
t_list = bs.find_all(re.compile("a"))
for a in t_list:
    print(a)


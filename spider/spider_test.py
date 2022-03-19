# @createTime : 2022/3/17
# @authorName : cyss
# @fileName : spider_test.py
# @description : 爬虫测试
import urllib.request

from bs4 import BeautifulSoup
import re
from urllib import *
import sqlite3
import xlwt

findlink = re.compile(r'<a href="(.*?)">')


# 得到一个指定网页的内容
def askUrl(url):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.39 "
    }
    request = urllib.request.Request(url=url, headers=headers)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


def gatData(baseurl):
    datalist = []
    for i in range(0, 1):
        url = baseurl + str(i * 25)
        html = askUrl(url)

        soup = BeautifulSoup(html, "html.parser")
        # print(soup)
        for item in soup.find_all("div", class_="item"):
            print(item)
            item = str(item)
            link = re.findall(findlink, item)[0]
            # print(link)

    return datalist


def main():
    baseurl = "https://movie.douban.com/top250?start="
    datalist = gatData(baseurl)
    savapath = ".\\doubanTop250.xls"


if __name__ == "__main__":
    main()

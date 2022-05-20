# @createTime : 2022/5/18 19:41
# @authorName : cyss
# @fileName : class.py
# @description : 爬虫练习，爬取计算机专业的专业课程

import re
import urllib.request

from bs4 import BeautifulSoup
from urllib import *
import sqlite3
import xlwt

findTitle = re.compile(r'target="_blank">(.*?)</a>')


def askUrl(url):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.39 "
    }
    request = urllib.request.Request(headers=headers, url=url)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


def getData(url):
    html = askUrl(url)
    soup = BeautifulSoup(html, "html.parser")
    item = soup.find_all("ul", class_="nav clearfix")
    item = str(item)
    titlelist = re.findall(findTitle, item)
    return titlelist


def saveData(savepath, titlelist):
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)
    sheet = book.add_sheet("XUST标题", cell_overwrite_ok=True)
    for i in range(len(titlelist)):
        sheet.write(i, 0, titlelist[i])
    book.save(savepath)


def main():
    url = "https://www.xust.edu.cn/"
    data = getData(url)
    savepath = "专业课名称.xls"
    saveData(savepath, data)


if __name__ == "__main__":
    main()

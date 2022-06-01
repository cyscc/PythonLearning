# @createTime : 2022/5/23 16:12
# @authorName : cyss
# @fileName : bilibiliComment.py
# @description : 爬取bilibili上尚硅谷spark视频下面的评论
import urllib.request
from urllib import request
from bs4 import BeautifulSoup
import re
import xlwt
import gzip


def ungZip(data):
    try:
        data = gzip.decompress(data)
    except errno:
        pass
    return data


def askUrl(url):
    heades = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.39 ",
        "accept-encoding": "gzip, deflate, br"
    }
    request = urllib.request.Request(url=url, headers=heades)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read()
        html = ungZip(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


def getData(baseUrl):
    html = askUrl(baseUrl)
    soup = BeautifulSoup(html, "html.parser")
    print(soup)
    return dataList


def main():
    url = "https://www.bilibili.com/video/BV11A411L7CK?p=31&spm_id_from=pageDriver"
    dataList = getData(url)


if __name__ == "__main__":
    main()

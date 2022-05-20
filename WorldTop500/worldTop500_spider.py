# @createTime : 2022/5/20 8:49
# @authorName : cyss
# @fileName : worldTop500_spider.py
# @description : 爬取世界500强企业相关信息

import urllib.request
from urllib import *
from bs4 import BeautifulSoup
import re
import xlwt

# 排名
findNum = re.compile(
    r"<td>(\d+|-\d+|\d+,\d+|\d+,\d+.\d+|-\d+,\d+|-\d+,\d+.\d+|\d+.\d+|-\d+.\d+|-)</td>")
findNameC = re.compile(r'target="_blank">(.*?)（')
findNameE = re.compile(r'[\u4e00-\u9fa5]*（(.*?)\)', re.X)
findCountry = re.compile(r"<td>([\u4e00-\u9fa5]*)</td>")


def askUrl(url):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.39 "
    }
    request = urllib.request.Request(url, headers=headers)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
    except urllib.error.URLError:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


def getUrl(baseUrl):
    html = askUrl(baseUrl)
    soup = BeautifulSoup(html, "html.parser")
    data = soup.find_all("table", class_="wt-table")
    dataStr = str(data)
    print(dataStr)
    dataList = []

    nameC = re.findall(findNameC, dataStr)
    dataList.append(nameC)

    nameE = re.findall(findNameE, dataStr)
    dataList.append(nameE)

    num = re.findall(findNum, dataStr)
    dataList.append(num)

    country = re.findall(findCountry, dataStr)
    dataList.append(country)

    return dataList


def saveData(savePath, dataList):
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)
    sheet = book.add_sheet("2021世界500强信息", cell_overwrite_ok=True)
    col = ["公司名称", "公司名称(英文)", "排名", "营业收入(百万美元)", "利润(百万美元)", "国家"]
    for i in range(6):
        sheet.write(0, i, col[i])
    for i in range(1, 501):
        sheet.write(i, 0, dataList[0][i - 1])
    for i in range(1, 501):
        sheet.write(i, 1, dataList[1][i - 1])
    for i in range(1, 501):
        for j in range(2, 5):
            sheet.write(i, j, dataList[2][(i - 1) * 3 + j - 2])
    for i in range(1, 501):
        sheet.write(i, 5, dataList[3][i - 1])
    book.save(savePath)


def main():
    baseUrl = "https://www.fortunechina.com/fortune500/c/2021-08/02/content_394571.htm"
    dataList = getUrl(baseUrl)
    savePath = "2021世界500强信息.xls"
    saveData(savePath, dataList)


if __name__ == "__main__":
    main()

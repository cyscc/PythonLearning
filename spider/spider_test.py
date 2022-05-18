# @createTime : 2022/5/18
# @authorName : cyss
# @fileName : spider_test.py
# @description : 爬虫测试
import urllib.request

from bs4 import BeautifulSoup
import re
from urllib import *
import sqlite3
import xlwt

# 利用正则表达式来获取字符串中匹配到的值
# 影片链接
findlink = re.compile(r'<a href="(.*?)">')
# 影片图片
findImgSrc = re.compile(r'<img.*src="(.*?)"', re.S)  # re.S: 忽视换行符
# 影片片名
findTitle = re.compile(r'<span class="title">(.*)</span>')
# 影片评分
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
# 评价人数
findJudge = re.compile(r'<span>(\d*)人评价</span>')
# 概况
findInq = re.compile(r'<span class="inq">(.*)</span>')
# 影片相关内容
findBD = re.compile(r'<p class="">(.*?)</p>', re.S)


# 得到一个指定网页的内容
def askUrl(url):
    # 模拟主机发出的请求头信息
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.39 "
    }
    # 发出请求得到服务器的响应
    request = urllib.request.Request(url=url, headers=headers)
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


def gatData(baseurl):
    datalist = []
    # 循环遍历 1 ~ 10 页，每页 25 条
    for i in range(0, 10):
        url = baseurl + str(i * 25)
        html = askUrl(url)
        # 解析数据: 利用 soup 来解析 html 网页
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all("div", class_="item"):
            item = str(item)
            data = []
            # 提取影片链接，加入data
            link = re.findall(findlink, item)[0]
            data.append(link)
            # 提取影片图片，加入data
            imgSrc = re.findall(findImgSrc, item)[0]
            data.append(imgSrc)
            # 提取影片片名，加入data
            titles = re.findall(findTitle, item)
            if len(titles) == 2:
                ctitle = titles[0]
                data.append(ctitle)
                otitle = titles[1].replace("/", "")
                data.append(otitle)
            else:
                data.append(titles[0])
                data.append("  ")
            # 提取影片评分，加入data
            rating = re.findall(findRating, item)[0]
            data.append(rating)
            # 提取影片评价人数，加入data
            judgeNum = re.findall(findJudge, item)[0]
            data.append(judgeNum)
            # 提取影片介绍，加入data
            inq = re.findall(findInq, item)
            if len(inq) == 0:
                data.append("  ")
            else:
                data.append(inq[0].replace("。", ""))
            # 提取影片相关内容，加入data
            bd = re.findall(findBD, item)[0]
            bd = re.sub('<br(\s+)?/>(\s+)?', " ", bd)
            bd = re.sub('/', " ", bd)
            data.append(bd.strip())
            # 将一个影片的data添加到datalist中
            datalist.append(data)
    return datalist


def saveData(datalist, savepath):
    print("save......")
    # 创建一个文件
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)
    # 创建一张表
    sheet = book.add_sheet("豆瓣电影250", cell_overwrite_ok=True)
    # 标题行写入
    col = ("电影详情链接", "图片链接", "影片中文名", "影片外文名", "评分", "评价数", "概况", "相关信息")
    for i in range(0, 8):
        sheet.write(0, i, col[i])
    # 信息写入
    for i in range(0, 250):
        print("第%d条" % (i + 1))
        data = datalist[i]
        for j in range(0, 8):
            sheet.write(i + 1, j, data[j])
    # 保存到指定目录
    book.save(savepath)


def main():
    baseurl = "https://movie.douban.com/top250?start="
    datalist = gatData(baseurl)
    savapath = "豆瓣电影Top250.xls"
    saveData(datalist, savapath)


if __name__ == "__main__":
    main()
    print("爬取成功!")

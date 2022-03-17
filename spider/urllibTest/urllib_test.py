# @createTime : 2022/3/17
# @authorName : cyss
# @fileName : urllib_test.py
# @description : 测试urllib
import urllib.request
import urllib.parse

# response = urllib.request.urlopen("http://www.baidu.com")
# print(response.read().decode("utf-8"))

# post请求
# data = bytes(urllib.parse.urlencode({"hello": "world"}), encoding="utf-8")
# response = urllib.request.urlopen("http://httpbin.org/post", data=data)
# print(response.read().decode("utf-8"))

# get请求
# try:
#     response = urllib.request.urlopen("http://httpbin.org/get", timeout=0.01)  # 用try...except... 来处理请求超时的问题
#     print(response.read().decode("utf-8"))
# except urllib.error.URLError as e:
#     print("time out!")

# 模拟用户向浏览器发送器请求
# url = "http://httpbin.org/post"
# data = bytes(urllib.parse.urlencode({"name": "cyss"}), encoding="utf-8")
# headers = {
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
#                   "Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.39 "
# }
# req = urllib.request.Request(url=url, data=data, headers=headers, method="POST")
# response = urllib.request.urlopen(req)
# print(response.read().decode("utf-8"))

# 模拟用户向豆瓣发送请求
url = "https://www.baidu.com"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.39 "
}
req = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))

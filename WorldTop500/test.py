# @createTime : 2022/5/20 9:22
# @authorName : cyss
# @fileName : test.py
# @description :
import re

findNum = re.compile(r"[0-9]+")
str1 = "erdsc3dsdc23423dv23e12"
print(re.findall(findNum, str1))

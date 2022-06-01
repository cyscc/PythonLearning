import requests
from lxml import etree

url = "https://xian.zbj.com/search/f/?type=new&kw=saas"
req = requests.get(url)

# 解析
html = etree.HTML(req.text)
divs = html.xpath("/html/body/div[6]/div/div/div[2]/div[5]/div[1]/div")
for div in divs:
    price = div.xpath("./div/div/a[2]/div[2]/div[1]/span[1]/text()")[0].strip("¥")
    print(price)
    title = "saas".join(div.xpath("./div/div/a[2]/div[2]/div[2]/p/text()"))
    print(title)
    company_name = div.xpath("./div/div/a[1]/div[1]/p/text()")[1].strip("\n")
    print(company_name)
    address = div.xpath("./div/div/a[1]/div[1]/div/span/text()")[0]
    print(address)

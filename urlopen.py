import urllib.request

response = urllib.request.urlopen("http://www.baidu.com")  # 返回一个bytes数据
html = response.read()  # 读取
html = html.decode("utf-8")  # 解码
print(html)

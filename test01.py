import random
import ssl
import urllib.request
import ExcitingDemo
from Crawler import Free_IP


def url_open(url):

    req = urllib.request.Request(url)
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36')
    try:
        response = urllib.request.urlopen(req)
        content = response.read()
        return content
    except urllib.error.HTTPError as reason:
        print('打开网址 %s 失败, 错误代码: ' % url + str(reason))


ssl._create_default_https_context = ssl._create_unverified_context
url = 'http://jandan.net/girl/MjAyMjAyMDgtMTAw#comments'

html = url_open(url).decode('utf-8')
print(html)

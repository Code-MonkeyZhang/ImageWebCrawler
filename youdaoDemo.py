import time
import urllib.request
import urllib.parse
import ssl
import json


ssl._create_default_https_context = ssl._create_unverified_context

while True:
    content = input('请输入要翻译的内容：')
    if content=='q':
        break

    # 从header中获取Request Url
    # 需要将原url中的_o删去，这是网站的反爬虫机制
    url = 'https://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    # 建立一个字典储存要发送的信息
    data = {}

    data['i'] = content
    data['from'] = 'AUTO'
    data['to'] = 'AUTO'
    data['smartresult'] = 'dict'
    data['client'] = 'fanyideskweb'
    data['salt'] = '16431880555037'
    data['sign'] = 'a1eed458e21b60c1c5fb1b7c931acab9'
    data['lts'] = '1643188055503'
    data['bv'] = '30202777336adaadd34a49a7c732df71'
    data['doctype'] = 'json'
    data['version'] = '2.1'
    data['keyfrom'] = 'fanyi.web'
    data['action'] = 'FY_BY_REALTlME'

    data = urllib.parse.urlencode(data).encode('utf-8')

    #创建Request类
    req = urllib.request.Request(url, data)
    #修改header
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36')
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')

    #
    target = json.loads(html)
    print('翻译结果： %s' % (target['translateResult'][0][0]['tgt']))

print('已退出翻译')
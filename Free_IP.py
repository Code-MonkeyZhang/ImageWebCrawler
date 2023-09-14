import random
import re
import ssl
import urllib.request


def url_open(url):
    proxy_list = ['60.170.204.30:8060', '152.136.62.181:9999', '106.15.197.250:8001']

    proxy_support = urllib.request.ProxyHandler({'http': random.choice(proxy_list)})
    opener = urllib.request.build_opener(proxy_support)
    opener.addheaders = [('User-Agent',
                          'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/94.0.4606.61 Safari/537.36')]
    urllib.request.install_opener(opener)

    response = urllib.request.urlopen(url)
    html = response.read()

    return html


def get_ip():
    url = 'https://www.kuaidaili.com/free/inha/1/'
    html = url_open(url).decode('utf-8')

    pt = r'(?:(?:[0,1]?\d?\d|2[0-4]\d|25[0-5])\.){3}(?:[0,1]?\d?\d|2[0-4]\d|25[0-5]])'
    ip_list = re.findall(pt, html)
    return ip_list


if __name__ == '__main__':
    ssl._create_default_https_context = ssl._create_unverified_context
    get_ip()

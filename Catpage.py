import ssl
import time
import urllib.request
import urllib.error
import os
import random



def url_open(url):
    # 设置代理:
    proxy_list = ['60.170.204.30:8060', '152.136.62.181:9999', '106.15.197.250:8001']

    proxy_support = urllib.request.ProxyHandler({'http': random.choice(proxy_list)})
    opener = urllib.request.build_opener(proxy_support)
    opener.addheaders = [('User-Agent',
                          'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36')]
    urllib.request.install_opener(opener)

    try:
        response = urllib.request.urlopen(url)
    except urllib.error.URLError:
        print('无法打开网页: ' + url+ '错误代码: ')
        pass
    else:
        content = response.read()
        return content


def find_img(cat_page):
    img_address = []
    # 头尾夹
    head = cat_page.find('<img')
    tail = cat_page.find('alt')
    while head != -1:
        if tail != -1:
            # if头和尾都找到,就append
            img_address.append('https://placekitten.com' + cat_page[head + 23:tail - 2])
            # 重置起始查找的位置
            head = cat_page.find('<img', tail)
            tail = cat_page.find('alt', tail + 9)

    for each in img_address:
        print(each)
    return img_address


def save_img(img_address):
    for each in img_address:
        filename = each.split('/')[-1] + '.jpg'
        cat_image = url_open(each)
        # urlopen返回的response对象 可以读取
        if cat_image != None:
            with open(filename, "wb") as f:
                f.write(cat_image)
                print(each)

        # rest = random.choice(range(1, 5))
        # print('间隔%d秒' % rest)
        # time.sleep(rest)


def download_cat(folder_name='cat_images'):
    # 创建路径
    os.chdir(folder_name)

    url = 'https://placekitten.com'
    try:
        cat_page = url_open(url).decode('utf-8')
    except AttributeError:
        print('无法解码网页')
    else:
        img_address = find_img(cat_page)
        save_img(img_address)
    print("爬取结束")


if __name__ == '__main__':
    ssl._create_default_https_context = ssl._create_unverified_context
    download_cat()

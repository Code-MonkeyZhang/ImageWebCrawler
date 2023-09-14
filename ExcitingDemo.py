import os
import random
import ssl
import time
import urllib.request
import urllib.error

import requests

from Crawler import Free_IP


def url_open(url):

    try:
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'}
        content = requests.get(url, headers=headers).content
        return content

    except urllib.error.HTTPError as reason:
        print('打开网址 %s 失败, 错误代码: ' % url + str(reason))


def download_images(page):
    img_address = []
    # 头尾夹
    head = page.find('<img')
    tail = page[head:].find('.jpg') + head
    while head != -1:
        if tail != -1:
            # if头和尾都找到,就append
            img_address.append('https:' + page[head + 10:tail + 4])
            # 重置起始查找的位置
            head = page.find('<img', tail)
            tail = page[head:].find('.jpg') + head

    print("成功获取页面图片地址........\n")

    for each in img_address:
        img = url_open(each)
        with open(each[-10:], 'wb') as f:
            f.write(img)
            print("成功下载第%d张图片(*_*)" % (img_address.index(each) + 1))

    print('=====成功下载本页面所有图片(^_^)=====\n')


def get_next(page):
    head = page.find("<a title=\"Older Comments\"")
    tail = page.find("class=\"previous-comment-page\">下一页</a>")
    old_comments = page[head + 32:tail - 2]
    next_url = 'http:' + old_comments
    print('获取到下一页')
    return next_url


def download_ooxx(url, limit=-1):
    '''
         需求：设置爬取的页数
         if页数是-1，爬完全部，if页数是n，页数是n时，爬完第n页之后停止

    if limit != -1:
        while limit > 0:
        1. 访问页面
        2. 下载页面图片
        3. 获取下一页url next_url
    '''
    index = limit
    count = 1
    if limit != -1:
        while limit > 0:
            if url == 'http:':
                print("已经爬取了 %d 页,找不到下一页(-_-')" % (index - limit))
                break

            print('=====正在爬取第%d页=====' % (index - limit + 1))
            html = url_open(url).decode('utf-8')
            download_images(html)
            url = get_next(html)
            limit -= 1
    else:
        while True:
            print('=====正在爬取第%d页=====' % count)
            html = url_open(url).decode('utf-8')
            download_images(html)
            url = get_next(html)
            if url == 'http:':
                print('=====已经爬取所有图片, 一共%d页======' % count)
                break

            count += 1


if __name__ == '__main__':
    url = 'http://jandan.net/girl/MjAyMjAyMTMtOTI=#comments'
    # 设置文件路径
    folder_name = 'ooxx_images'
    os.chdir('/Volumes/Portable/照片/ooxx_images')
    # 开始爬虫
    download_ooxx(url, -1)

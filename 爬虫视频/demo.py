import os

import requests
from urllib.request import urlretrieve
from lxml import etree
import re


# 1 获取页面源代码
# 2 获取视频ID
# 3 拼接完整的URL地址
# 4 获取视频的播放地址
# 5 下载视频

# 下载历史片
def download(url):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
    # 获取页面源代码
    # url =  "http://www.pearvideo.com/category_10"
    html = requests.get (url).text
    # 把文本文件处理成可解析对象
    html = etree.HTML (html)
    # xpath
    #
    video_id = html.xpath ("//div[@class='vervideo-bd']/a/@href")
    # print(video_id)
    # 拼接完整的url地址
    starturl = "http://www.pearvideo.com"
    video_url = []
    for id in video_id:
        newurl = starturl + '/' + id
        # print (newurl)
        video_url.append (newurl)
    for playurl in video_url:
        html = requests.get (playurl).text
        # 正则表达式
        req = 'srcUrl=".*?"'
        # 增加效率
        req = re.compile (req)
        # 视频播放地址
        purl = re.findall (req, html)
        # print (purl)
        req = '<h1 class="video-tt">(.*?)</h1>'
        video_name = re.findall (req, html)
        # %s 字符串格式化 format {} .format
        print ("正在下载视频：%s" % video_name[0])
        path = "video"
        if path not in os.listdir ():
            os.mkdir (path)
            # 视频下载的路径
            urlretrieve (purl[0], path + '/%s.mp4' % video_name[0])

    # download ()


# http://www.pearvideo.com/category_loading.jsp?reqType=5&categoryId=10&start=24&mrd=0.1439629067543231&hotContIds=1371444,1371329,1371511

def downloadmore():
    while True:
        n = 12
        if n > 48:
            return
        # 下载视频
        url = "http://www.pearvideo.com/category_loading.jsp?reqType=5&categoryId=10&start=%d" % n
        n += 12
        # print (n)
        # pass
        download (url)


downloadmore ()

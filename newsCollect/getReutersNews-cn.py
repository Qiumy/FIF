# -*- coding:utf-8 -*-

import urllib.request
import chardet
import urllib.parse
from lxml import etree

from bs4 import BeautifulSoup
import json
import time
import logging
import codecs

error_urls = []

def download(url, user_agent='wswp', proxy=None, num_retries=2):
    print('Downloading: ', url)
    headers = {'User-agent': user_agent}
    request = urllib.request.Request(url, headers=headers)

    opener = urllib.request.build_opener()
    if proxy:
        proxy_params = {urllib.parse.urlparse(url).scheme: proxy}
        opener.add_handler(urllib.request.ProxyHandler(proxy_params))
    try:
        html = opener.open(request).read()
        charset = chardet.detect(html)['encoding']
        if charset == 'GB2312' or charset == 'gb2312':
            html = html.decode('GBK').encode('utf-8')
        else:
            html = html.decode(charset).encode('utf-8')
    except urllib.request.URLError as e:
        print('Download error', e.reason)
        html = None
        if num_retries > 0:
            if num_retries > 0:
                if hasattr(e, 'code') and 500 <= e.code < 600:
                    # recursively retry 5xx HTTP errors
                    return download(url, user_agent, proxy, num_retries - 1)
    except Exception as e:
        print(e)
        error_urls.append(url)
    return html, url


def parse(html_doc, url):
    print(type(html_doc))
    html = etree.HTML(html_doc, parser=etree.HTMLParser(encoding='utf-8'))
    articles = html.xpath('//article')
    data = []
    with open("reuterNews-cn-2017-09-04.json", 'a') as f:
        for article in articles:
            img = article.xpath('div/a/img/@src')[0]
            content = article.xpath('.//div[@class="story-content"]')[0]
            title = content.xpath('.//h3')[0].text.strip()
            link = content.xpath('.//a/@href')[0]
            con = content.xpath('.//p')[0].text.strip()
            time = content.xpath('.//time/span')[0].text

            item = {}
            item['title'] = title
            item['link'] = link
            item['content'] = con
            item['time'] = time
            item['img'] = img
            # print("#################: ",item)

            json_str = json.dumps(item, ensure_ascii=False)
            try:
                f.write(json_str + '\n')
            except Exception as e:
                print(e)
                error_urls.append(url)

if __name__ == '__main__':
    logging.basicConfig(filename='./log/reutersCollect-cn.log',
                        level=logging.INFO)

    cnt = 1481
    while True:
        url = "http://cn.reuters.com/news/archive/businessNews" \
              "?view=page&pageSize=10&page={}".format(cnt)
        logging.info("#{}#info message: cnt->{}".format(
            time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
            cnt))
        html, url = download(url, proxy='127.0.0.1:1080')
        parse(html, url)
        cnt += 1
        time.sleep(0.3)
    with open('errorUrl-cn.txt', 'w') as f:
        for url in error_urls:
            f.write(url + '\n')

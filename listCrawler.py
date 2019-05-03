import requests
from bs4 import BeautifulSoup
import datetime
from tqdm import tqdm
from appleCrawler import Crawler
import json
import pandas as pd


class News:
    date = ''
    title = ''
    content = ''
    url = ''
    def __init__(self, date, title, url, content):
        self.date = date
        self.title = title
        self.url = url
        self.content = content

def getDate():
    now = datetime.datetime(2019, 5, 1)
    date_list = []
    while now != datetime.datetime(2019, 1, 1):
        now -= datetime.timedelta(days=1)
        y = str(now.year)
        m = str(now.month)
        d = str(now.day)
        if(len(m) < 2):
            m = '0' + m
        if(len(d) < 2):
            d = '0' + d
        date_list.append(y + m + d)
    return date_list
def get_content(url):
    crawler = Crawler()
    return crawler.get_title_and_content(url)[1]

def storeNews(news_list):
    news_0430 = pd.DataFrame(index=range(len(news_list)), columns=['date', 'title', 'content', 'url'])
    for news in news_list:
        news_0430.loc[news_list.index(news)] = [news.date, news.title, news.content, news.url]
    news_0430.to_csv('news_0430.csv', encoding="utf_8_sig")

    # for news in news_list:
    #     doc = {'date' : news.date, 'title' : news.title, 'content' : news.content, 'url' : news.url}
    #     with open('0430news.txt', 'a', encoding='utf-8'):
    #         json.dumps(doc, indent=4, ensure_ascii=False)

if __name__ == '__main__':
    date_list = getDate()
    news_list = []
    date = '20190430'
    # for date in date_list[0]:
    print(date)
    url = 'https://tw.appledaily.com/appledaily/archive/{}'.format(date)
    print(url)
    header = {
        'Host': 'tw.appledaily.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:66.0) Gecko/20100101 Firefox/66.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-TW,en-US;q=0.7,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate, br',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Cookie': 'nxtu=1556702446.1927948501-6308-469A-9C26-5CA2909DC677; nxtu=1556702446.1927948501-6308-469A-9C26-5CA2909DC677; LPVID=I2NTczNTIxYzhiNzA0Mjkz; isLoggedIn=false; country=TW; adisblk=Y; page_id=1556783251.497-f2aa-9e67-8e22-e24f9af44f82',
        'Upgrade-Insecure-Requests': '1',
        'Cache-Control': 'max-age=0',
        'TE': 'Trailers'
    }
    rs = requests.session()
    res = rs.get(url, headers=header)
    soup = BeautifulSoup(res.text, 'html.parser')
    ul_tags = soup.find_all('ul', class_="fillup")
    # ul_tags[0]

    for block in tqdm(ul_tags):
        for news in block.find_all('a'):
            if(news.get('title') != None):
                news_obj = News(date, news.get('title'), news.get('href'), get_content(news.get('href')))
                news_list.append(news_obj)
    storeNews(news_list)
    # get_content(news_list)
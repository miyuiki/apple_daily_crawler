from appleCrawler import Crawler

if __name__ == '__main__':

    crawler = Crawler()
    crawler.login('YOUR_EMAIL', 'YOUR_PASSWORD')
    url = 'https://tw.appledaily.com/new/realtime/20190423/1555525'

    print('title : ' + str(crawler.get_title_and_content(url)[0]))
    print('content : ' + str(crawler.get_title_and_content(url)[1]))
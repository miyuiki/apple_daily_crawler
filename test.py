from appleCrawler import Crawler

if __name__ == '__main__':

    crawler = Crawler()
    crawler.login('YOUR_EMAIL', 'YOUR_PASSWORD')
    url = 'https://tw.entertainment.appledaily.com/daily/20130802/35193634/?fbclid=IwAR133WpJXaUHjv8rCI3zHAnwSxmjnrm_rQraNqMSkz4OpNjs3609euxzdJ4'

    print('title : ' + str(crawler.get_title_and_content(url)[0]))
    print('content : ' + str(crawler.get_title_and_content(url)[1]))
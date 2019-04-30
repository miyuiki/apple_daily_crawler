import requests
from bs4 import BeautifulSoup as bs
import re
from urllib.parse import quote

class Crawler:
    username = ''
    password = ''
    url = ''
    headers = {
        'Host': 'auth.appledaily.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-TW,en-US;q=0.7,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://auth.appledaily.com/web/v6/apps/598aee773b729200504d1f31/login?type=redirect&redirect_uri=https%3A%2F%2Ftw.appledaily.com%2Fnew%2Frealtime%2F20190429%2F1558639&region=TW&lang=zh_tw&gaParams=%5B%5D&pixelParams=%7B%7D&utm_source=twad_web&utm_medium=internal&utm_campaign=twad_content_block&utm_content=1558639',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '69',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Cookie': 'nxtu=1543288007.55523CBBDF-661A-49B0-BFF0-940A7160431F; _parsely_visitor={%22id%22:%227a884c6b-a533-4215-8c7b-4ff6514241e8%22%2C%22session_count%22:7%2C%22last_session_ts%22:1548061178566}; CrmJson={"A":"99","GG":"99","SEG":"","PGG":"","UC":""}; CrmValid=1556624258904; lang=zh_tw; omo.sid=s%3Agr3ALO8yNjoD2olgmUeVpG1VvlNt57HX.9zEciGCuVr7t3FJ3Y338t2qj2KLbqr%2BhxfcDhzOLKdc; isLoggedIn=false; LPVID=FiZGI2NTlkOTVmMGJiZGFh; LPSID-49269227=0atKf2LZQXO8cLYDABuXeg; articleValid=20190430193742; articleExpires=Tue%20Apr%2030%202019%2019%3A37%3A42%20GMT%2B0800%20(%E5%8F%B0%E5%8C%97%E6%A8%99%E6%BA%96%E6%99%82%E9%96%93); articleID=; article=0; adisblk=Y; OMO_LSTLGWAY=email; country=TW',
        'Upgrade-Insecure-Requests': '1'
    }
    rs = requests.session()

    def login(self, username, password):

        info = 'phoneNumber=&email={}&password={}'.format(quote(username), quote(password))
        # print(info)
        res = self.rs.get('https://auth.appledaily.com/web/v6/apps/598aee773b729200504d1f31/login?type=redirect&redirect_uri=https://tw.appledaily.com/new/realtime/20190429/1558639&region=TW&lang=zh_tw&gaParams=[]&pixelParams={}&utm_source=twad_web&utm_medium=internal&utm_campaign=twad_content_block&utm_content=1558639&' + info, headers=self.headers)

    def get_title_and_content(self, url):
        header2 = {
            'Host': 'tw.appledaily.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'zh-TW,en-US;q=0.7,en;q=0.3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Referer': 'https://auth.appledaily.com/web/v6/apps/598aee773b729200504d1f31/redirect',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Cookie': 'nxtu=1543288007.55523CBBDF-661A-49B0-BFF0-940A7160431F; _parsely_visitor={%22id%22:%227a884c6b-a533-4215-8c7b-4ff6514241e8%22%2C%22session_count%22:7%2C%22last_session_ts%22:1548061178566}; nxtu=1543288007.55523CBBDF-661A-49B0-BFF0-940A7160431F; CrmJson={"A":"99","GG":"99","SEG":"","PGG":"","UC":""}; CrmValid=1556624258904; isLoggedIn=false; LPVID=FiZGI2NTlkOTVmMGJiZGFh; LPSID-49269227=0atKf2LZQXO8cLYDABuXeg; articleValid=20190430193742; articleExpires=Tue%20Apr%2030%202019%2019%3A37%3A42%20GMT%2B0800%20(%E5%8F%B0%E5%8C%97%E6%A8%99%E6%BA%96%E6%99%82%E9%96%93); articleID=; article=0; FRONTSIZE=18; adisblk=Y; OMO_LSTLGWAY=email; country=TW; page_id=1556599954.885-5a49-cc11-5605-df79b1f88013',
            'Upgrade-Insecure-Requests': '1'
        }
        res2 = self.rs.get(url, headers=header2)

        soup = bs(res2.text, 'html.parser')
        tags = soup.find_all("p")
        content = re.search('<p>(.+)（(.+)／(.+)）', str(tags[0])).group(1)

        content_soup = bs(content, features="lxml")
        tags2 = soup.find_all("h1")

        return tags2[0].text, content_soup.text
if __name__ == '__main__':
    pass

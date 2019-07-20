# 蘋果新聞爬蟲程式
由於蘋果每日新聞更改為需要登入且付費才能閱讀內文，
因此需要提供帳號資訊才能爬取新聞
## Installation
下載 `appleCrawler.py` 並放至專案資料夾底下即可
## Usage
```python
from appleCrawler import Crawler

crawler = Crawler()
crawler.login('YOUR_EMAIL', 'YOUR_PASSWORD')
url = 'https://tw.appledaily.com/new/realtime/20190423/1555525'

title = crawler.get_title_and_content(url)[0]
content = crawler.get_title_and_content(url)[1]
```

可參考`example.py`

若要爬取某日的所有新聞，請執行 `listCrawler.py`，
並額外新增一個日期參數
```
python listCrawler.py 20190430
```
請確保日期格式符合yyyymmdd

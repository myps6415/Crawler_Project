# Python 網路爬蟲課程 10

:::warning
:warning: 注意事項 :warning:
* 課程內容以 Python 爬蟲為主軸，Python 基礎不會著墨過深，基礎的部份遇到困難請同學善用 [Google](https://www.google.com/)
* 課程內容是本人的嘔心瀝血之作，若有引用請標明出處
* 本文最後編輯日期：2020/01/10
:::

## 課堂使用環境安裝 :computer:
* 本課程使用 [Anaconda](https://www.anaconda.com/download/) 做為教學環境
* 請下載對應電腦作業系統的 Python 3.6 版本
* 詳細安裝流程 :point_right: [Python Anaconda 環境安裝教學](/h5XtZtlRSB2TQP-marFL5g)
* [Python 網路爬蟲課程 2](/8ZVF56fBQ-ydJC5Sj0Gubg) 之後的課程均使用 [Google Chrome](https://www.google.com/intl/zh-TW_ALL/chrome/) 作為課堂所用，請在課堂開始前先行安裝完成

## 上週作業
* 撰寫程式爬取五頁，接著轉換別項商品，共爬三項商品
這個題目不難，假設我們這次要爬的商品是 iPhone、iPad、macbook 這三樣，因此將這三樣寫在一個 list 內，以迴圈的方式便可將三樣商品依序爬取，程式碼如下：
```python=
import requests
from bs4 import BeautifulSoup
import sqlite3
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

items = ['iphone', 'ipad', 'macbook']
url = 'https://shopee.tw/search/?keyword={}&page={}&sortBy=relevancy'

for item in items:
    page = 0
    while page < 5:
        driver = webdriver.Chrome('/Users/fish/Documents/workspace/chromedriver')
        driver.get(url.format(item, page))
        time.sleep(3)
        
        res = driver.page_source
        soup = BeautifulSoup(res, 'html.parser')
    
        for i in soup.find_all(class_ = 'col-xs-2-4 shopee-search-item-result__item'):
            title = i.find(class_ = 'shopee-item-card__text-name').text
            price = i.find(class_ = 'shopee-item-card__current-price').text
            love = i.find(class_ = 'shopee-item-card__btn-like__text').text
            href = 'https://shopee.tw' + i.find(class_ = 'shopee-item-card--link').get('href')

            print([item, title, price, love, href], '第 ' + str(page + 1) + '頁')
    
        page += 1
        driver.close()
```

程式碼中可以看到，透過 while 處理，而停止條件為 `page < 5`，這樣一來便可以順利地跑過 page 為 0~4 的各個頁面

## API 爬蟲實戰
開始之前請各位先安裝 Chrome 的應用軟體，方便於本課程後續內容
* 安裝 [JSON Formatter](https://tinyurl.com/vv4jrka)
![](https://i.imgur.com/p4k14fC.png)

本次課程內容為 Hahow 網站爬蟲，這個網站開設了許多線上課程，而我們要爬取的目標為課程的基本資料
![](https://i.imgur.com/cfWvWpt.png)

在網頁中，我們觀察這個網頁，能夠發現到網站溝通訊息中有個網址是 `https://api.hahow.in/api/categories`，代表這個網站背後有透過 api 在進行溝通，api 溝通對我們來說是比較方便的，裡面的內容會是整理過的形式
![](https://i.imgur.com/OqlZDBB.png)

因此我們拿這串 api 的網址貼回瀏覽器，可以看到呈現如下
![](https://i.imgur.com/y3zx0RY.png)

會這樣整齊地排列是因為剛剛已經裝了 [JSON Formatter](https://tinyurl.com/vv4jrka)，沒裝的狀況下則會如下，在資料較多的狀況下會變得凌亂不易閱讀
![](https://i.imgur.com/xpJyiRB.png)

我們的目標為爬取課程的資訊，因此找到相對應的 api 網址為 `https://api.hahow.in/api/courses`，打開後我們可以看到它已經幫我們計算好了，平台上共 262 堂課，另外就是課程的一些資訊，如價格、預售價格、網址...等
![](https://i.imgur.com/91mhCi9.png)

仔細觀察 api，我們會發現到 data 中僅有 24 筆資料，因此可以知道這個 api 也有翻頁的機制，符合網頁上一頁有 24 堂課程的設計
![](https://i.imgur.com/TTHOAe4.png)

我們將目標設定在爬取課程的 _id、title、price、preOrderedPrice、metaDescription，完整的程式碼如下：
```python=
import requests
from bs4 import BeautifulSoup

url = 'https://api.hahow.in/api/courses?page={}'
page = 0

while True:
    res = requests.get(url.format(page))
    if res.json()['data']:
        for item in res.json()['data']:
            _id = item['_id']
            title = item['title']
            price = item['price']
            preOrderedPrice = item['preOrderedPrice']
            description = item['metaDescription']
            c.execute('insert into hahow_information (id, title, price, preOrderedPrice, description) values (?,?,?,?,?)', [_id ,title, price, preOrderedPrice, description])
            conn.commit()
            print([_id ,title, price, preOrderedPrice, description])
            
    else:
        break
        
    page += 1
```
輸出：
```
['5b26587f67ff51001e25cf0a', '實用Photoshop- 入門到大師，紮實範例', 2046, 1280, 'Photoshop 對我來說它不只是一個 軟體，它是一個創作的媒介，在我學習的過程當中看了很多Photoshop 工具書，但對我的創作卻沒有提升， 所以開這門課的緣由就是為了讓大家學習軟體工具也能知道怎麼運用，融會貫通後，也可以創作出屬於自己的作品。']
['5acb00ded21aee001e55b670', '簡報方舟：高效簡報的系統化做法', 1800, 1200, '簡報能力很重要，但做簡報之前，要先擁有正確的簡報思維！簡報教練林長揚的簡報方舟課程，利用系統化學習模組，為你打造簡報即戰力！讓你的簡報觀、換位思考、架構設計、畫面呈現、上台表現皆大大提升！']
['5b3070e92c4c440043918161', '比阿里巴巴還便宜的女裝批發', 3980, 3680, '當你修完這門課之後，你將學到中國電商淘寶與阿里巴巴背後的女裝供貨來源，不需要使用支付寶跳過繁瑣的付款流程與降低風險，實質拿到出廠價格降低進貨成本把關貨源的品質，了解女裝市場最新流行趨勢強先一步上架！掌握安全以及穩定的運送時效！']
['5aa918b7d0f8ac001e2881cb', '會聲會影7堂課，人人都是剪接師', 899, 699, '你是否有想過要將回憶製作成影片，但是不知道如何下手？在這堂課我們將會以非常容易上手的會聲會影來教大家如何自行剪輯影片。']
```

以上，本課程設計的內容到此告一段落，最後來回顧一下這十堂課我們教了些什麼！

## 課程總結
### Python 基礎
* 環境安裝 #Anaconda
* 使用資料庫 #SQLite
* 字串 #'text'
* 串列 #[1,2,3]

### Python 運算式及陳述
* if, elif, else
* For 迴圈 (for loop)
* While 迴圈 (while loop)
* break, continue, pass
* 例外處理 #try…except

### Python 爬蟲和數據處理相關套件
* BeautifulSoup
* Requests
* Selenium
* Pandas
* Chrome 小工具 #JavaScrip Switcher、JSON Formatter

### 爬蟲課程體驗
* 網頁爬取
* 圖片爬取
* Selenium 模擬人類行為爬取
* 透過網站提供的 API 爬取

### 網頁爬取
1. Yahoo 購物中心
2. 飛比比價網
3. 六合彩資訊
4. 蘋果日報
5. 自由時報
6. 聯合新聞網
7. PTT 八卦板
8. 臺北公園走透透

### 圖片爬取
* PTT 圖片爬取
* PTT 回應數 30 以上的才爬

### Selenium 模擬人類行為爬取
* 蝦皮購物

### 透過網站提供的 API 爬取
* Hahow

這門課到這邊完整的結束了，感謝各位的參與，期待以後再相見！

---
:::success
課結束囉:100:
希望你喜歡這門課
:::

###### tags: `Python` `Python 網路爬蟲課程` `Crawler` `網路爬蟲` `SQLite`
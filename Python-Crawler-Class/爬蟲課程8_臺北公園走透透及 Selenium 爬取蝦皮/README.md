# Python 網路爬蟲課程 8

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

## [臺北公園走透透](https://parks.taipei/Web/Park/Index/鄰里公園)爬取實戰
在這門課中最有趣的是，同學會應用爬蟲技術在自己想要的網站上，而有些網站的設計較為特殊，爬取的技巧便會是之前課程內容中沒有的，同學就無法順利的完成爬蟲，當同學來詢問之後，這個網站就會變為課程內容回饋給同學
![](https://i.imgur.com/Ai9GBxR.png)

觀察網頁，拉到網頁底端可以看到換頁按鈕
![](https://i.imgur.com/uGCdLbL.png)

點擊第二頁，看看有什麼變化
![](https://i.imgur.com/RrBT4XA.png)

在這我們可以清楚看到翻頁後，網址變化為 `https://parks.taipei/Web/Park/Index/鄰里公園?page=2`，我們便能運用這點來撰寫爬蟲的翻頁動作

開始來寫程式吧！

```python=
import requests
from bs4 import BeautifulSoup
import sqlite3

conn = sqlite3.connect('~/Taipei_Park.db')
c = conn.cursor()

page = 1
url = 'https://parks.taipei/Web/Park/Index/鄰里公園?page={}'

res = requests.get(url.format(page), verify = False)
soup = BeautifulSoup(res.text, 'html.parser')

# 嘗試抓出第一頁的所有公園網址
for i in soup.find(class_ = 'page_park').find_all('a'):
    if i.get('href'):
        if 'Index' not in i.get('href'):
            print('https://parks.taipei' + i.get('href'))
```

輸出：
```
https://parks.taipei/Web/Park/Detail/861276D2F6824EA6978BC25A0EFBC441
https://parks.taipei/Web/Park/Detail/0259DF9DDC224DD79C04A0F47DC97E63
https://parks.taipei/Web/Park/Detail/4DC5A0AC80C24BCDB3E77D452EA02CCF
https://parks.taipei/Web/Park/Detail/B7CAA52723064E2EAEFA22E297BD2382
https://parks.taipei/Web/Park/Detail/9BB4B98EE622473B812538EE8B7C5837
https://parks.taipei/Web/Park/Detail/FB8EADD29462418EB17F4E9008F0A3A2
https://parks.taipei/Web/Park/Detail/3E5088766B824B5B829B5EAE5114E074
https://parks.taipei/Web/Park/Detail/67545E579B434E41A11ED84803A99594
https://parks.taipei/Web/Park/Detail/15A0B69EDEA2479C92535437F08CBF64
https://parks.taipei/Web/Park/Detail/F877C8E8F17C4A29B6AFFFE16D03BFA4
https://parks.taipei/Web/Park/Detail/06B2571B12994CB3B974BCB974058CE9
https://parks.taipei/Web/Park/Detail/3776C1363BCA44A78CEE3E996B3E8DA1
```

```python=+
page = 1
park_url = [] #存所有公園網址

while page != 33:
    url = 'https://parks.taipei/Web/Park/Index/鄰里公園?page={}'
    res = requests.get(url.format(page), verify = False)
    soup = BeautifulSoup(res.text, 'html.parser')
    for i in soup.find(class_ = 'page_park').find_all('a'):
        if i.get('href'):
            if 'Index' not in i.get('href'):
                park_url.append('https://parks.taipei' + i.get('href'))
                print(page, 'https://parks.taipei' + i.get('href'))
    page += 1
```
輸出：
```
1 https://parks.taipei/Web/Park/Detail/861276D2F6824EA6978BC25A0EFBC441
1 https://parks.taipei/Web/Park/Detail/0259DF9DDC224DD79C04A0F47DC97E63
1 https://parks.taipei/Web/Park/Detail/4DC5A0AC80C24BCDB3E77D452EA02CCF
1 https://parks.taipei/Web/Park/Detail/B7CAA52723064E2EAEFA22E297BD2382
1 https://parks.taipei/Web/Park/Detail/9BB4B98EE622473B812538EE8B7C5837
1 https://parks.taipei/Web/Park/Detail/FB8EADD29462418EB17F4E9008F0A3A2
1 https://parks.taipei/Web/Park/Detail/3E5088766B824B5B829B5EAE5114E074
1 https://parks.taipei/Web/Park/Detail/67545E579B434E41A11ED84803A99594
1 https://parks.taipei/Web/Park/Detail/15A0B69EDEA2479C92535437F08CBF64
1 https://parks.taipei/Web/Park/Detail/F877C8E8F17C4A29B6AFFFE16D03BFA4
1 https://parks.taipei/Web/Park/Detail/06B2571B12994CB3B974BCB974058CE9
1 https://parks.taipei/Web/Park/Detail/3776C1363BCA44A78CEE3E996B3E8DA1
2 https://parks.taipei/Web/Park/Detail/7DD6845920844645ABD17CCE15EA105B
2 https://parks.taipei/Web/Park/Detail/B31D4E0A5842403F9DF1062C109BA5B5
2 https://parks.taipei/Web/Park/Detail/770E7EAEDEF448829A417DD93950B15D
2 https://parks.taipei/Web/Park/Detail/86132EF07BF54A1F804E90C02CF981CC
2 https://parks.taipei/Web/Park/Detail/18D47F4E178349C4A0DC24C1EFD35069
2 https://parks.taipei/Web/Park/Detail/17DA8DFCE3A94259B41C72D0EE74196F
2 https://parks.taipei/Web/Park/Detail/E8AB39ED5D2E495CBC31C727ECF71E7A
2 https://parks.taipei/Web/Park/Detail/5C93F82329A445D7BB703AF3D70D8C21
2 https://parks.taipei/Web/Park/Detail/EE4B7DDDC23347E6B66E33A04E57D4A8
2 https://parks.taipei/Web/Park/Detail/D5A598D1B8544E78824C0B7EDD8DCC68
2 https://parks.taipei/Web/Park/Detail/41BFFA5C3FE9405C8118850684018B9A
2 https://parks.taipei/Web/Park/Detail/959E40938C0A4C1B85C9A1AFEED2C515
...
```

```python=+
for i in park_url:
    save_info = []
    res = requests.get(i, verify = False)
    soup = BeautifulSoup(res.text, 'html.parser')
    for detial in soup.find(class_ = 'detail_info').find_all('p'):
        detial = detial.text.split(':')[1]
        save_info.append(detial)
    
    facility_list = list(soup.find(class_ = 'park_prvn').stripped_strings)
    facility_list = [x.rstrip('：') for x in facility_list]
    Service_facilities = facility_list[1]
    Sports_facilities = facility_list[3]
    Rides = facility_list[5]
    toilet = facility_list[7]
    save_info.extend([Service_facilities, Sports_facilities, Rides, toilet])
    c.execute('insert into park (place, lining, address, area, type, year, management, phone, time, service_facilities, sports_facilties, rides, toilet) values (?,?,?,?,?,?,?,?,?,?,?,?,?)', save_info)
    conn.commit()
    print(save_info)
```
輸出：
```
['臺北市內湖區', '寶湖里、金湖里', '民權東路6段與民權東路6段203巷交叉口旁', '804 平方公尺', '鄰里公園', '106', '花卉試驗中心內湖分隊', '26586601', '', '公園無該項設施', '公園無該項設施', '公園無該項設施', '公園無該項設施']
['臺北市南港區', '東明里', '南港區興華路、市民大道口', '1910 平方公尺', '鄰里公園', '105', '南港公園管理所', '02-27884255', '全天', '公園無該項設施', '公園無該項設施', '公園無該項設施', '公園無該項設施']
...
```

以上就是臺北公園走透透爬蟲的課程內容，此內容在授課時是完全可以爬取沒有問題的，而在編輯這份講義的今天 (2020/01/10)，該網站已經改版，講義的部分就以當時授課的狀態呈現，暫不更動！

## 初試 Selenium 套件
### Selenium 簡介
* Selenium 是為了測試網站而出現的套件
* 在爬蟲應用中，它是非常好的工具
* 它能夠控制瀏覽器，像是人類瀏覽網頁

### 安裝 Selenium
請在 Terminal 輸入：
```shell=
conda install -c conda-forge selenium
```

### Selenium 必要軟體下載
請到[下載點](https://chromedriver.storage.googleapis.com/index.html?path=80.0.3987.16/)選取符合自己作業系統相對應的軟體，存放在找得到的位置

### 實作
本課程以蝦皮網站作為課程內容，因網站使用 JavaScript 撰寫時，無法透過 requests 套件取得網頁原始碼，因此在這時候會以 selenium 模擬人操作的方式開啟瀏覽器，以這樣的模式取得網頁原始碼

在蝦皮的網站中，我們的目標是在搜尋列中輸入要搜尋的東西，在本課重中以 `iPhone` 為例
![](https://i.imgur.com/dDPZFgk.png)

因此在網頁原始碼中，我們要定位好搜尋列的原始碼
![](https://i.imgur.com/zvKTiyL.png)

在程式碼中，透過 `.send_keys()` 將字串送入搜尋列中
```python=
search_bar = driver.find_element_by_class_name('shopee-searchbar-input__input')
search_bar.send_keys('iPhone')
```
順利執行網頁搜尋列會自動的加入 `iPhone`
![](https://i.imgur.com/0OZGYA6.png)

接著，我們要讓它按下搜尋，我們在瀏覽網頁時打完字要按下搜尋，可以透過鍵盤按下 enter，因此在這邊我們要操作模擬人按下 enter，程式碼為：
```python=
search_bar.send_keys(Keys.ENTER)
```
這時便能看到被程式所操作的瀏覽器進入到搜尋結果的頁面
![](https://i.imgur.com/id3zidH.png)

如此一來就到了我們所要的頁面，透過之前課程教過的 BeautifulSoup 取得網頁原始碼，完整程式碼如下：
```python=
import time
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

url = 'https://shopee.tw'

driver = webdriver.Chrome('/Users/fish/Documents/workspace/chromedriver')
driver.get(url)
time.sleep(5)

#找到搜尋欄，並輸入 iPhone
search_bar = driver.find_element_by_class_name('shopee-searchbar-input__input')
search_bar.send_keys('iPhone')

search_bar.send_keys(Keys.ENTER)

res = driver.page_source
soup = BeautifulSoup(res, 'html.parser')

for i in soup.find_all(class_ = 'shopee-item-card__lower-padding'):
    print(i.text)
```

輸出：
```
🍎保證原廠品質 iPhone充電線 Apple充電線 iPhone X 8 7 6 Plus iPad 現貨 傳輸線$230 - $6993779(7811)3.4折
【iPhone】Mcdodo 100%智能斷電 快充線 傳輸線 充電線 線 iphone 呼吸線 數據線 iPhone線$199 - $25951(152) 蝦皮優選
台灣公司貨 雷射防偽標簽  RK3036 AnyCast 手機電視棒 hdmi av  MHL M5 plus HDMI$60 - $299767(1286) 蝦皮優選
用不壞 新版磁吸充電線 三合一 充電線 蘋果/安卓/Type-c 充電線 iphone充電線 oppo$55 - $150150(239)4.5折 蝦皮優選
現貨【最高🍎品質】傳輸線 充電線 線 Apple線 iphone充電線 數據線 iPhone線 ipad$110 - $699326(529)1.1折 蝦皮優選
Iphone6 64G 4.7吋 太空灰外觀9成新 只賣5500元$5,5003尚未有評價NEW
Iphone6 金色 64G外觀9成新，只要6000元$6,0003尚未有評價NEW
自售 iPhone6s 64g 玫瑰金 功能完全正常 沒摔過 無泡水 有小傷痕 意者聊聊 會有小驚喜價格$6,50041尚未有評價
出清  頻果 iphone5 iphoone5s 16G 32G 64G iphone6  顏色隨機　送手機套$2,500 - $8,500413(24)
...
```

透過這樣的方式，我們便能順利的截取到透過 JavaScript 建置的網頁！
這堂課到這邊就結束囉，我們 [Python 網路爬蟲課程 9](/FuhQd68qRtK3GtxME3vyzg) 見 :eyes:

---
:::success
第八堂課結束囉:100:
請各位找到自己有興趣的網頁透過爬蟲的方式爬取下來，多加練習才會記得學到的東西喔！
:::

###### tags: `Python` `Python 網路爬蟲課程` `Crawler` `網路爬蟲` `SQLite`
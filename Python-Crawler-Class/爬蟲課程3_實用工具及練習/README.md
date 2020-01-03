# Python 網路爬蟲課程 3
:::warning
:warning: 注意事項 :warning:
* 課程內容以 Python 爬蟲為主軸，Python 基礎不會著墨過深，基礎的部份遇到困難請同學善用 [Google](https://www.google.com/)
* 課程內容是本人的嘔心瀝血之作，若有引用請標明出處
* 本文最後編輯日期：2018/08/31
:::

## 課堂使用環境安裝 :computer:
* 本課程使用 [Anaconda](https://www.anaconda.com/download/) 做為教學環境
* 請下載對應電腦作業系統的 Python 3.6 版本
* 詳細安裝流程 :point_right: [Python Anaconda 環境安裝教學](/h5XtZtlRSB2TQP-marFL5g)
* [Python 網路爬蟲課程 2](/8ZVF56fBQ-ydJC5Sj0Gubg) 之後的課程均使用 [Google Chrome](https://www.google.com/intl/zh-TW_ALL/chrome/) 作為課堂所用，請在課堂開始前先行安裝完成

## [Python 網路爬蟲課程 2](https://github.com/myps6415/Python-Crawler-Class/tree/master/爬蟲課程2_爬蟲基礎練習) 課後練習
題目：請爬取[飛比價格的 iPhone X 查詢結果](https://feebee.com.tw/product/iPhone%20X%20256G%20%E6%99%BA%E6%85%A7%E5%9E%8B%E6%89%8B%E6%A9%9F/?q=iphone%20x)所有價格，並計算其均價
> 提示：
> 1. 建立一個 List 儲存所有價格
> 2. 處理數字中的逗號 #.replace(',', '')
> 3. 將文字轉為數字 #int(12345)
> 4. 加總 #sum()
> 5. 計算長度 #len()

### 解說
#### STEP 1：在程式碼的開頭，我先定義了一個空 List 叫做 price，準備用於存放 while 迴圈中爬到的價格資訊

#### STEP 2：在 while 迴圈中才透過 requests 對網站呼叫，這樣才能夠在每一輪迴圈中重新定義 res 的網頁原始碼

#### STEP 3：找到的每一筆價格透過 .replace(',', '') 將數字中的逗號拿掉，並用 int() 包覆，使其是可以數字運算的型態

#### STEP 4：建立 while 迴圈的停止條件，底下程式碼指如果抓不到價格，透過 break 停止迴圈

#### STEP 5：記得每做完一輪頁數加 1

#### STEP 6：均價的計算方式為 $(價格加總) \div (商品數量)$，這邊可以想成 List 中所有項目相加後，除以 List 長度

詳細請參考程式碼：
```python=
import requests
from bs4 import BeautifulSoup

url = 'https://feebee.com.tw/product/iPhone%20X%20256G%20%E6%99%BA%E6%85%A7%E5%9E%8B%E6%89%8B%E6%A9%9F/?q=iphone%20x&page={}'
page = 1
price = []

while True:
    res = requests.get(url.format(page))
    soup = BeautifulSoup(res.text, 'html.parser')

    for iPhone_price in soup.find_all(class_ = 'price ellipsis'):
        price.append(int(iPhone_price.text.replace(',', '')))
        
    if soup.find(class_ = 'price ellipsis') is None:
        break
        
    page += 1

print(sum(price)/len(price))
```

執行結果：
```
39160.75799086758
```

## Google Chrome 工具安裝
課程走到這裡，相信有些同學開始嘗試透過學到的內容運用在自己趕興趣的網站上，也相信有同學遇到了程式完全沒寫錯，但就是一直跳錯誤訊息的狀況，因此在本節要教大家安裝一個 [Google Chrome](https://www.google.com/intl/zh-TW_ALL/chrome/) 的插件

### STEP 1：進入 [Chrome 線上應用程式商店](https://chrome.google.com/webstore/category/extensions?utm_source=chrome-ntp-icon)
![](https://i.imgur.com/rnttCr4.png)

### STEP 2：搜尋 ***Javascript***
![](https://i.imgur.com/IjIFYcg.png)

### STEP 3：將 ***Quick Javascript Switcher*** 加到 [CHROME](https://www.google.com/intl/zh-TW_ALL/chrome/)
![](https://i.imgur.com/5GEfEJn.png)

### STEP 4：確認安裝完成
確認在 [CHROME](https://www.google.com/intl/zh-TW_ALL/chrome/) 的上方有 ![](https://i.imgur.com/NZ6OhiD.png =30x30) 圖示

完成上述步驟後，對網站寫爬蟲之前能夠先確認該網站是否透過 Javascript 建置，若是，以目前到第三堂課的進度來說是無法處理這些網站的，因此請先跳過撰寫爬蟲爬取透過 Javascript 建置的網站

> 底下用[蝦皮購物](https://shopee.tw/)作為使用 ***Quick Javascript Switcher*** 的範例
1. 透過 [CHROME](https://www.google.com/intl/zh-TW_ALL/chrome/) 開啟 [蝦皮購物](https://shopee.tw/)
![](https://i.imgur.com/0qoIngw.jpg)

2. 點擊剛裝好的 ![](https://i.imgur.com/NZ6OhiD.png =30x30) ***Quick Javascript Switcher***
畫面會變得一片空白，代表整個網站都是透過 Javascript 建置
![](https://i.imgur.com/LvfuXPB.png)

## 六合彩資訊爬取
原本的課程規劃中沒有這個單元，但在上 [Python 網路爬蟲課程 2](/8ZVF56fBQ-ydJC5Sj0Gubg) 實體課程下課後，同學來向我說她想爬[六合彩開獎網站](https://www.lotto-8.com/listltohk.asp)，令我印象深刻！而實際了解網站後認為相當適合作為網頁爬蟲初學的練習，因此就納入課程內容囉！老師是從來沒有買過六合彩的 :joy:

### 爬取標的
在網站中會看到如下圖表格
![](https://i.imgur.com/g6ldZVn.png)

我們的爬取目標為**日期**、**六合彩中獎號碼**、**特別號**，**下次開獎日期**對資料分析來說沒有太多用途，因此排除。
老師另外要請同學將**六個六合彩中獎號碼分別存在欄位中**，因此資料庫欄位請設計為：


| id | date | num1 | num2 | num3 | num4 | num5 | num6 | special_num |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| 1 | 2018/07/03 | 3 | 21 | 22 | 41 | 45 | 49 | 10 |
| 2 | 2018/06/28 | 6 | 13 | 23 | 29 | 38 | 45 | 41 |
| ... | ... | ... | ... | ... | ... | ... | ... | ... |

### 撰寫程式
#### STEP 1：網頁觀察
1. 首先，我們要先確認網頁中哪些 tag 是我們要用到的，請同學先在網頁中找到我們要的標的，按滑鼠右鍵選擇**檢查**
![](https://i.imgur.com/WzoWLxN.png)

2. 滑鼠放在底部工具列標記藍色的那一行網頁原始法，能夠看到網頁中相對應的資料被藍色標記，而此行是我們要的其中一筆資料
![](https://i.imgur.com/t7t5GCn.png)

3. 原始碼左邊的下三角符號 (![](https://i.imgur.com/5S3aK80.png)) 將原始碼縮小觀察，會發現原始碼重複相間，仔細觀察會發現較長的為背景藍色的資料，較短的為背景白色的資料
![](https://i.imgur.com/FXbFBRm.png)

此時，我們已經找到了重複性，可以撰寫程式來處理了 :smirk:

#### STEP 2：程式基本設定
程式一開始透過 requests 向網頁請求，然後透過 BeautifulSoup 解析取得的網頁原始碼
```python=
import requests
from bs4 import BeautifulSoup

url = 'http://www.lotto-8.com/listltohk.asp'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
```

#### STEP 3：二個 for 迴圈取得一切
這邊範例使用兩個 for 迴圈處理這個網站，第一個 for 迴圈取得藍底的資料，第二個 for 迴圈取得白底的資料
```python=+
for i in soup.find_all('tr', style = 'text-align:center; background-color: #CCEEFF;'):
    text = i.text.split('\n')
    text.pop(0)
    text.pop(-1)
    text.pop(-1)
    text.pop(-1)
    text[1] = text[1].replace('\xa0','')
    print(text)

print('======================第一段迴圈結束======================')

for i2 in soup.find_all('tr', style = 'text-align:center; '):
    text = i2.text.split('\n')
    text.pop(0)
    text.pop(-1)
    text.pop(-1)
    text.pop(-1)
    text[1] = text[1].replace('\xa0','')
    print(text)
```

執行結果 (程式最後執行時間：2018/08/16)：
由於執行結果較長，底下結果部分用 **...** 表示執行結果，中間**第一段迴圈結束**要讓同學較明顯看出藍底資料爬完後開始爬白底資料的過程
```
['2018/08/14', '32,37,38,42,43,49', '24']
['2018/08/09', '08,10,11,20,21,34', '13']
['2018/08/04', '04,15,23,34,37,48', '30']
['2018/07/31', '24,27,36,43,44,46', '30']
['2018/07/26', '22,32,37,44,46,49', '38']
['2018/07/21', '13,14,15,37,38,44', '40']
...
['2018/01/11', '03,29,31,43,47,49', '19']
['2018/01/02', '12,18,28,35,39,42', '36']
['2017/12/28', '15,17,23,40,44,46', '11']
['2017/12/24', '01,16,26,34,39,47', '11']
['2017/12/19', '03,09,33,38,44,49', '24']
['2017/12/14', '07,10,20,25,34,35', '08']
======================第一段迴圈結束======================
['2018/08/11', '01,11,25,38,47,49', '37']
['2018/08/07', '04,21,25,39,46,47', '12']
['2018/08/02', '03,05,11,34,35,45', '28']
['2018/07/28', '05,07,11,26,30,43', '17']
['2018/07/24', '02,16,17,27,32,37', '12']
['2018/07/19', '12,16,23,25,40,42', '20']
...
['2018/01/06', '01,12,21,31,36,49', '23']
['2017/12/30', '01,13,22,25,36,38', '37']
['2017/12/26', '02,07,16,28,30,37', '12']
['2017/12/21', '14,21,22,28,30,47', '03']
['2017/12/16', '01,03,06,09,24,28', '36']
['2017/12/12', '04,15,29,34,38,48', '30']
...
```

### 存到 SQLite
```python=
import sqlite3

conn = sqlite3.connect('~/class_data.db')
c = conn.cursor()

for i in soup.find_all('tr', style = 'text-align:center; background-color: #CCEEFF;'):
    text = i.text.split('\n')
    text.pop(0)
    text.pop(-1)
    text.pop(-1)
    text.pop(-1)
    text[1] = text[1].replace('\xa0','')
    num1 = text[1].split(',')[0]
    num2 = text[1].split(',')[1]
    num3 = text[1].split(',')[2]
    num4 = text[1].split(',')[3]
    num5 = text[1].split(',')[4]
    num6 = text[1].split(',')[5]
    c.execute('insert into Mark_Six(date, num1, num2, num3, num4, num5, num6, special_num) values (?, ?, ?, ?, ?, ?, ?, ?)', [text[0], num1, num2, num3, num4, num5, num6, text[2]])
    conn.commit()
    
for i2 in soup.find_all('tr', style = 'text-align:center; '):
    text = i2.text.split('\n')
    text.pop(0)
    text.pop(-1)
    text.pop(-1)
    text.pop(-1)
    num1 = text[1].split(',')[0]
    num2 = text[1].split(',')[1]
    num3 = text[1].split(',')[2]
    num4 = text[1].split(',')[3]
    num5 = text[1].split(',')[4]
    num6 = text[1].split(',')[5]
    c.execute('insert into Mark_Six(date, num1, num2, num3, num4, num5, num6, special_num) values (?, ?, ?, ?, ?, ?, ?, ?)', [text[0], num1, num2, num3, num4, num5, num6, text[2]])
    conn.commit()
```

執行結果：
![](https://i.imgur.com/8Eqpzcv.png)

## 蘋果日報爬取實戰
在這一節中會帶各位實做[蘋果日報今日 TOP 30](https://tw.appledaily.com/hot/daily) 的爬取
我們的目標是**編號**、**標題**、**觀看人數**、**各新聞網址**
![](https://i.imgur.com/KC5DwAe.jpg)

### 撰寫程式
#### STEP 1：網頁觀察
![](https://i.imgur.com/PaHXL5v.png)

#### STEP 2：找到規則，開始撰寫程式
程式開頭，先引入所需套件
```python=
import requests
from bs4 import BeautifulSoup
```

接著定義網址然後透過 requests 呼叫取得網頁原始碼
```python=+
url = 'https://tw.appledaily.com/hot/daily'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
```

對每一條新聞標題透過 for 迴圈巡覽，在[蘋果日報今日 TOP 30](https://tw.appledaily.com/hot/daily) 中，可以先透過 `.find(class_ = 'all')`，再接著找 class = all 底下的所有 li 開頭的 tag，因此寫法為 `.find(class_ = 'all').find_all('li')`。接著我們就可以在迴圈中定義 id、標題和觀看次數，迴圈部分的程式碼如下：
```python=+
for i in soup.find(class_ = 'all').find_all('li'):
    num = i.find(class_ = 'aht_title_num').text
    title = i.find(class_ = 'aht_title').text
    view = i.find(class_ = 'aht_pv_num').text
    print(num, title, view)
```
這樣執行之後的輸出結果為：
```
01 獨家調查 台灣淪世界垃圾場 半年86國百萬噸湧入 121534
02 離譜 中國不要 台灣狂收 政府麻木 放任14個月 55862
03 老饕認證的好滋味　在地傳統美食飄香42年 21329
04 林瑞陽晾妻肉貼熟女 一家人數鈔真親密 29378
05 47歲鍾麗緹澄清沒發胖！女神為嫩夫拚子依舊性感！ 15324
06 2童在水上樂園遭性侵 色狼強拉被害人到漂漂河橋下逞慾 26854
07 拾荒嬤推58公斤 換回107元「快活不下去」 26247
08 街口支付涉吸金 金管會震怒 22572
09 楊靜賓館會小16歲歌手 「姊弟」按捏太激情 14644
10 扯 菲泰也把廢料丟台灣 15885
11 小戴徵男友條件 歐亞混血不說英語 13448
12 全台集氣今晚打中國 棒球 男籃齊出陣 20423
13 「要去很遠的地方」小丸子幫櫻桃子道別離 10148
14 盧廣仲 挾《花甲》11入圍光環 對幹李國毅搶視帝 16465
15 街口急了 和LINE Pay明著幹 7126
16 棄2000萬年薪 胡定吾子創街口 7495
17 聯航用貨幣區分兩岸 官網奇招抗中 我外交部：樂觀其成 17205
18 孫安佐認罪 棄上訴 12月宣判 爭取兩月內遣送回台 21655
19 足底筋膜炎治療全攻略 不再步步驚心 17060
20 獄中畫畫健身 律師：他是藝術家 16281
21 AV明日花綺羅爆G奶 附身《美女與野獸》貝兒 7839
22 《瘋狂亞洲富豪》 4帥圈粉 亨利高汀戲外台灣女婿 8594
23 晉升A咖的好機會！賓士Ａ-Class大改款８月底正式登場 11510
24 《爆炸2》12提名最威 安心亞首沾金哭了 9847
25 中國最美女總裁 李穎 一路開外掛 7742
26 搭公車頻被堵 柯改坐公務車上班 17275
27 宋慧喬 笑納 美顏零死角 雪花秀香港趴 嫻妃佘詩曼駕到 9137
28 林心如淪遺珠 誇張軒睿「好棒」 7805
29 【蘋中人】黑手變大明星 陳竹昇 12715
30 0.001秒銀恨 楊俊瀚：很嘔 14136
```

此時我們完成了第一頁資訊的爬取，但通常我們在搜集資料時，每篇文章的主文也會是我們必要的資訊，因此要取得主文的關鍵在於每篇文章的網址，蒐集到文章的網址我們才有辦法進到網址內搜集主文，因此，還想將每一則的網址搜集下來怎麼做？

1. 先觀察網頁原始碼
![](https://i.imgur.com/B1iMlSn.png)

這時會發現網址的所在位置和 title 一樣，都在 `class = "aht_title"` 底下
因此要取得原始碼中的網址，可以透過 `.get()` 來處理
而網址在 **a** 開頭的 tag 中，因此在多加一個 `.find('a')` 來做取得網址那一行網頁原始碼，最後透過 `.get()` 取得 `href`，寫法為：
```python=
i.find(class_ = 'aht_title').find('a').get('href')
```

2. 在迴圈中加入一行 url 變數定義取得的網址，並且 print 出觀察
```python=
for i in soup.find(class_ = 'all').find_all('li'):
    num = i.find(class_ = 'aht_title_num').text
    title = i.find(class_ = 'aht_title').text
    view = i.find(class_ = 'aht_pv_num').text
    url =  i.find(class_ = 'aht_title').find('a').get('href')
    print(num, title, view, url)
```

執行結果：
```
01 獨家調查 台灣淪世界垃圾場 半年86國百萬噸湧入 121534 https://tw.news.appledaily.com/headline/daily/20180830/38112027
02 離譜 中國不要 台灣狂收 政府麻木 放任14個月 55862 https://tw.news.appledaily.com/headline/daily/20180830/38112039
03 老饕認證的好滋味　在地傳統美食飄香42年 21329 https://tw.news.appledaily.com/headline/daily/20180830/38111334
04 林瑞陽晾妻肉貼熟女 一家人數鈔真親密 29378 https://tw.entertainment.appledaily.com/daily/20180830/38111756
05 47歲鍾麗緹澄清沒發胖！女神為嫩夫拚子依舊性感！ 15324 https://tw.entertainment.appledaily.com/daily/20180830/38111379
06 2童在水上樂園遭性侵 色狼強拉被害人到漂漂河橋下逞慾 26854 https://tw.news.appledaily.com/headline/daily/20180830/38112175
07 拾荒嬤推58公斤 換回107元「快活不下去」 26247 https://tw.news.appledaily.com/headline/daily/20180830/38112056
08 街口支付涉吸金 金管會震怒 22572 https://tw.finance.appledaily.com/daily/20180830/38111607
09 楊靜賓館會小16歲歌手 「姊弟」按捏太激情 14644 https://tw.entertainment.appledaily.com/daily/20180830/38111765
10 扯 菲泰也把廢料丟台灣 15885 https://tw.news.appledaily.com/headline/daily/20180830/38112053
11 小戴徵男友條件 歐亞混血不說英語 13448 https://tw.sports.appledaily.com/daily/20180830/38111999
12 全台集氣今晚打中國 棒球 男籃齊出陣 20423 https://tw.sports.appledaily.com/daily/20180830/38111958
13 「要去很遠的地方」小丸子幫櫻桃子道別離 10148 https://tw.entertainment.appledaily.com/daily/20180830/38111785
14 盧廣仲 挾《花甲》11入圍光環 對幹李國毅搶視帝 16465 https://tw.entertainment.appledaily.com/daily/20180830/38111691
15 街口急了 和LINE Pay明著幹 7126 https://tw.finance.appledaily.com/daily/20180830/38111615
16 棄2000萬年薪 胡定吾子創街口 7495 https://tw.finance.appledaily.com/daily/20180830/38111619
17 聯航用貨幣區分兩岸 官網奇招抗中 我外交部：樂觀其成 17205 https://tw.news.appledaily.com/international/daily/20180830/38111900
18 孫安佐認罪 棄上訴 12月宣判 爭取兩月內遣送回台 21655 https://tw.news.appledaily.com/headline/daily/20180830/38112067
19 足底筋膜炎治療全攻略 不再步步驚心 17060 https://tw.news.appledaily.com/headline/daily/20180830/38110375
20 獄中畫畫健身 律師：他是藝術家 16281 https://tw.news.appledaily.com/headline/daily/20180830/38112073
21 AV明日花綺羅爆G奶 附身《美女與野獸》貝兒 7839 https://tw.entertainment.appledaily.com/daily/20180830/38111789
22 《瘋狂亞洲富豪》 4帥圈粉 亨利高汀戲外台灣女婿 8594 https://tw.entertainment.appledaily.com/daily/20180830/38111771
23 晉升A咖的好機會！賓士Ａ-Class大改款８月底正式登場 11510 https://tw.news.appledaily.com/headline/daily/20180830/38110429
24 《爆炸2》12提名最威 安心亞首沾金哭了 9847 https://tw.entertainment.appledaily.com/daily/20180830/38111705
25 中國最美女總裁 李穎 一路開外掛 7742 https://tw.finance.appledaily.com/daily/20180830/38111626
26 搭公車頻被堵 柯改坐公務車上班 17275 https://tw.news.appledaily.com/headline/daily/20180830/38111836
27 宋慧喬 笑納 美顏零死角 雪花秀香港趴 嫻妃佘詩曼駕到 9137 https://tw.entertainment.appledaily.com/daily/20180830/38111799
28 林心如淪遺珠 誇張軒睿「好棒」 7805 https://tw.entertainment.appledaily.com/daily/20180830/38111723
29 【蘋中人】黑手變大明星 陳竹昇 12715 https://tw.news.appledaily.com/headline/daily/20180830/38112091
30 0.001秒銀恨 楊俊瀚：很嘔 14136 https://tw.sports.appledaily.com/daily/20180830/38111987
```
到這邊我們順利的將頁面中看到的 id、標題、觀看人數以及所有的網址取出來了！

:::success
到這邊第三堂課告一段落囉 :100:
接著請各位以前面蘋果日報章節學到的技巧運用在[自由時報焦點新聞](http://news.ltn.com.tw/list/newspaper)
![](https://i.imgur.com/d6fHP2Y.png)
請各位 print 出`標題`、`類別`、`網址`
解答在下堂 [Python 網路爬蟲課程 4](/AVX1bD4FSaCj4f84fY5RrQ)，請練習完成再點喔！
我們下堂課見 :wave:
:::

###### tags: `Python` `Python 網路爬蟲課程` `Crawler` `網路爬蟲` `SQLite`

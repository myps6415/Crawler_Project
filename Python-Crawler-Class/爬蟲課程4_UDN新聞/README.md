# Python 網路爬蟲課程 4

:::warning
:warning: 注意事項 :warning:
* 課程內容以 Python 爬蟲為主軸，Python 基礎不會著墨過深，基礎的部份遇到困難請同學善用 [Google](https://www.google.com/)
* 課程內容是本人的嘔心瀝血之作，若有引用請標明出處
* 本文最後編輯日期：2018/09/19
:::

## 課堂使用環境安裝 :computer:
* 本課程使用 [Anaconda](https://www.anaconda.com/download/) 做為教學環境
* 請下載對應電腦作業系統的 Python 3.6 版本
* 詳細安裝流程 :point_right: [Python Anaconda 環境安裝教學](/h5XtZtlRSB2TQP-marFL5g)
* [Python 網路爬蟲課程 2](/8ZVF56fBQ-ydJC5Sj0Gubg) 之後的課程均使用 [Google Chrome](https://www.google.com/intl/zh-TW_ALL/chrome/) 作為課堂所用，請在課堂開始前先行安裝完成

## [Python 網路爬蟲課程 3](/TX7GQ1GKTa-O1VSAe-w2YQ) 課後練習
請透過先前學到爬取[蘋果日報今日 TOP 30](https://tw.appledaily.com/hot/daily) 的技巧運用在[自由時報焦點新聞](http://news.ltn.com.tw/list/newspaper)
如果還沒有實際操作這部分的同學，請先不要看這一節的內容，實際練習後再看本節解答，不然真的會原地踏步無法進步喔！
### 完成練習的同學，我們來看講解吧：
![](https://i.imgur.com/CZ54Dck.png)

我們的目標是`標題`、`類別`、`網址`，因此來看這三個項目分別在網頁原始碼中的樣子吧！
![](https://i.imgur.com/MCHGVgg.png)
從上圖我們可以發現，每一則新聞的資訊都是在 `<ul class="list">` 底下的 `<li>`，因此這是我們撰寫程式時抓取的重要指標，來寫程式吧！
```python=
import requests
from bs4 import BeautifulSoup

url = 'http://news.ltn.com.tw/list/newspaper'

res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

for i in soup.find(class_='list').find_all('li'):
    title = i.find(class_ = 'tit').find('p').text
    tag = i.find(class_ = 'tagarea').text
    url = i.find(class_ = 'tit').get('href')
    print([title, tag, url])
```

在程式碼的迴圈中，我定義了題目要求的`標題`、`類別`、`網址`，這三個的共通點都是在 `<li>` 後再各別 `.find()` 各自的 tag，最後的執行結果為：
```
['台北市長選舉 本報民調// 柯文哲33.43％丁守中24.71％姚文智14.9％', '頭版新聞', 'news/focus/paper/1228896']
['蔡政府首度執行死刑// 殘殺妻女 李宏基槍決', '頭版新聞', 'news/focus/paper/1228897']
['侵台秋颱恐一～兩個 須防共伴效應', '頭版新聞', 'news/focus/paper/1228898']
['暫聘管中閔為台大校長 法院駁回', '頭版新聞', 'news/focus/paper/1228899']
['高雄罕見日暈 揮別雨災', '頭版新聞', 'news/focus/paper/1228900']
['台北市長選舉》操盤手懸缺 柯文哲且戰且走', '焦點新聞', 'news/focus/paper/1228837']
['台北市長選舉》端政策牛肉 姚文智打團隊戰', '焦點新聞', 'news/focus/paper/1228838']
['台北市長選舉》防柯挖牆腳 丁守中勤走基層', '焦點新聞', 'news/focus/paper/1228839']
['台北市長選舉》柯文哲藍綠都吸票 姚文智衝擊較大', '焦點新聞', 'news/focus/paper/1228840']
['百里侯大戰選情評估》民進黨固守中台灣 衝雙北宜蘭', '焦點新聞', 'news/focus/paper/1228890']
['百里侯大戰選情評估》國民黨決戰中台灣 伺機奪北高', '焦點新聞', 'news/focus/paper/1228891']
['九合一大選 20993人登記', '焦點新聞', 'news/focus/paper/1228892']
['國民黨台東縣鬧分裂》鄺麗貞突登記 夫吳俊立怒嗆離婚', '焦點新聞', 'news/focus/paper/1228893']
['國民黨桃園市鬧分裂》楊麗環選定了 陳學聖斥忘恩負義', '焦點新聞', 'news/focus/paper/1228894']
['金門唯一民進黨議員陳滄江 退黨退選', '焦點新聞', 'news/focus/paper/1228895']
```

## UDN 新聞網
在這一系列的第四堂課，我會帶各位再爬一個新聞網站：[聯合新聞網即時版](https://udn.com/news/breaknews/1)
![](https://i.imgur.com/jIK8b9O.png)

### 觀察網頁
觀察[聯合新聞網即時版](https://udn.com/news/breaknews/1)的網頁原始碼可以發現，所有新聞的標題都是被 `<dt>` 所包覆
![](https://i.imgur.com/lt89UsI.png)
簡單的觀察後，我們可以開始嘗試撰寫程式了！

### 撰寫程式
#### STEP 1：嘗試適用的 tag
和先前的課程一樣，套用 `requests` 和 `BeautifulSoup`，定義好網址，最後把 `soup.find_all('dt')` 印出來觀察 (在 Jupyter Notebook 最後一行沒有寫 print 也可印出結果)
```python=
import requests
from bs4 import BeautifulSoup

url = 'https://udn.com/news/breaknews/1'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

soup.find_all('dt')
```
執行結果：
```
[<dt><a class="toprow_shopping sp" href="https://shopping.udn.com/mall/Cc1a00.do?sid=91_udn&amp;utm_source=udn.com&amp;utm_medium=referral_familybar_udn&amp;utm_term=familybar_udn&amp;utm_campaign=20150103_UDN" target="_blank">買東西</a></dt>,
 <dt><a class="toprow_udnfunlife sp" href="https://udesign.udnfunlife.com/mall/Cc1a00.do?sid=91_udn&amp;utm_source=udn.com&amp;utm_medium=referral_familybar_udn&amp;utm_term=familybar_udn&amp;utm_campaign=20170118_UDN" target="_blank">有設計</a></dt>,
 <dt><a class="toprow_tickets sp" href="https://tickets.udnfunlife.com/application/utk01/utk0101_.aspx?sid=91_udn&amp;utm_source=udn.com&amp;utm_medium=referral_familybar_udn&amp;utm_term=familybar_udn&amp;utm_campaign=20170118_UDN" target="_blank">售票網</a></dt>,
 <dt><a class="toprow_rss" href="/rssfeed/lists/2" target="_blank">RSS</a></dt>,
 <dt><a class="toprow_app" href="https://mobile.udn.com/" target="_blank">App</a></dt>,
 <dt><a class="toprow_fb" href="https://www.facebook.com/myudn" target="_blank"></a></dt>,
 <dt><a class="toprow_mynews" href="https://udn.com/mypage/">我的新聞</a></dt>,
 <dt><a class="toprow_family" href="javascript:void(0);" id="toprow_family">udn family</a></dt>,
 <dt><a class="toprow_search sp" href="javascript:void(0);" id="toprow_search">搜尋</a></dt>,
...
```

從執行結果來看，也有其他對我們來說是雜訊的資訊被包在 `<dt>` 底下，因此我們需要再下更多條件來篩選需要的資訊

#### STEP 2：增加更多篩選條件
回到網站中，我們先針對網頁原始碼一條一條往上查詢，直到找到能夠包住所有我們需要的資訊被一條原始碼包住為止
![](https://i.imgur.com/0HCqBdu.png)

從上圖中我們可以得知當滑鼠移到 `id="breaknews_body"` 的位置時，因此將其加入程式的篩選機制中，並嘗試印出
```python=+
for i in soup.find(id = 'breaknews_body').find_all('dt'):
    print(i.text)
```

執行結果：
```
社會散播「登革熱有人死」 台中男子被逮送辦 09-10 10:230
數位微軟Xbox One推出全新聲控 使用者可透過Alexa及Cortana操作09-10 10:2010
兩岸「雙11締造者」張勇 阿里集團70後主帥09-10 10:1998
產經烘焙餐飲物流全攻略 南僑用差異化利基拚戰09-10 10:180
.inline-ad { position: relative; overflow: hidden; box-sizing: border-box; }
.inline-ad div { margin: auto; text-align: center; }
.inline-ad iframe { margin:auto; display: block; /*width: auto !important;*/ }
.inline-ad div[id^=google_ads_iframe] {
 padding: 50px 0 30px;
}
.inline-ad div[id^=google_ads_iframe]:before {
 content: "推薦";
 font-size:13px;
 color:#999;
 text-align:left;
 border-top: 1px solid #d9d9d9;
 width: 100%;
 position: absolute;
 top: 15px;
 left: 0;
 padding-top: 5px;
}
...
```

看上去有新聞標題和日期在裡面了，但格式仍然混亂，且仍有雜訊在其中，因此套用 [Python 網路爬蟲課程 2](/8ZVF56fBQ-ydJC5Sj0Gubg) 所教的 `.stripped_strings` 來處理
```python=+
for i in soup.find(id = 'breaknews_body').find_all('dt'):
    print(i.stripped_strings)
```

執行結果：
```
<generator object stripped_strings at 0x7ff9da065b48>
<generator object stripped_strings at 0x7ff9da065b48>
<generator object stripped_strings at 0x7ff9da065b48>
<generator object stripped_strings at 0x7ff9da065b48>
<generator object stripped_strings at 0x7ff9da065b48>
<generator object stripped_strings at 0x7ff9da065b48>
<generator object stripped_strings at 0x7ff9da065b48>
<generator object stripped_strings at 0x7ff9da065b48>
<generator object stripped_strings at 0x7ff9da065b48>
...
```
:::danger
希望各位還記得上面這樣的執行結果是怎麼回事！
不記得也沒關係，這是複習 [Python 網路爬蟲課程 2](/8ZVF56fBQ-ydJC5Sj0Gubg) 的好機會 :mega:
:::

接著，我們將上面產生的多個物件一樣用 **for** 迴圈處理
```python=+
for i in soup.find(id = 'breaknews_body').find_all('dt'):
    for t in i.stripped_strings:
        print(t)
```

執行結果：
```
社會
散播「登革熱有人死」 台中男子被逮送辦
09-10 10:23
0
數位
微軟Xbox One推出全新聲控 使用者可透過Alexa及Cortana操作
09-10 10:20
10
兩岸
「雙11締造者」張勇 阿里集團70後主帥
09-10 10:19
98
產經
烘焙餐飲物流全攻略 南僑用差異化利基拚戰
09-10 10:18
0
.inline-ad { position: relative; overflow: hidden; box-sizing: border-box; }
.inline-ad div { margin: auto; text-align: center; }
.inline-ad iframe { margin:auto; display: block; /*width: auto !important;*/ }
.inline-ad div[id^=google_ads_iframe] {
 padding: 50px 0 30px;
}
...
```

從結果我們看到，新聞標題、日期...等資訊已經整齊了，但仍有雜訊，因此我在程式中加入 if 判斷式來處理
```python=+
for i in soup.find(id = 'breaknews_body').find_all('dt'):
    for t in i.stripped_strings:
        if '.inline-ad' not in t and 'googletag.cmd.push' not in t and 'div-gpt-ad' not in t:
            t = t.split('\n')
            print(t)
```

執行結果：
```
['社會']
['散播「登革熱有人死」 台中男子被逮送辦']
['09-10 10:23']
['0']
['數位']
['微軟Xbox One推出全新聲控 使用者可透過Alexa及Cortana操作']
['09-10 10:20']
['10']
['兩岸']
['「雙11締造者」張勇 阿里集團70後主帥']
['09-10 10:19']
['98']
['產經']
['烘焙餐飲物流全攻略 南僑用差異化利基拚戰']
['09-10 10:18']
['0']
['全球']
['中國使館稱「語言不通」 讓關西機場允許派車接人']
['09-10 10:18']
['359']
...
```

上面的執行結果已經可以清楚看到我們要的資訊，但現在這樣的資料型態並不是我們可以存到 SQLite 的格式，因此我們需要對它做些處理。
觀察剛剛程式的執行結果可以發現，每筆資料皆被 List 所包覆，每印出 4 筆是 1 則新聞的所有資訊，包含`來源`、`標題`、`日期`、`觀看數`
因此，老師的處理方法是建立一個空的 List，每執行一次迴圈就將資料存入 List 中，當 List 長度為 4 時，將 List 印出，印出後清空整個 List，讓後續的資料能夠再從 0 開始存入，反覆此動作直到資料爬完
```python=+
data = []
for i in soup.find(id = 'breaknews_body').find_all('dt'):
    for t in i.stripped_strings:
        if '.inline-ad' not in t and 'googletag.cmd.push' not in t and 'div-gpt-ad' not in t:
            t = t.split('\n')
            data.append(t[0])
            if len(data) == 4:
                print(data)
                data.clear()
```

執行結果：
```
['社會', '散播「登革熱有人死」 台中男子被逮送辦', '09-10 10:23', '0']
['數位', '微軟Xbox One推出全新聲控 使用者可透過Alexa及Cortana操作', '09-10 10:20', '10']
['兩岸', '「雙11締造者」張勇 阿里集團70後主帥', '09-10 10:19', '98']
['產經', '烘焙餐飲物流全攻略 南僑用差異化利基拚戰', '09-10 10:18', '0']
['全球', '中國使館稱「語言不通」 讓關西機場允許派車接人', '09-10 10:18', '359']
['全球', '俄地方選舉日 示威群眾數百人遭逮捕', '09-10 10:17', '12']
['股市', '開飆3訊號 下車4徵兆 抱好！抱牢！跟著飆股賺翻天', '09-10 10:15', '0']
['要聞', '多元性別友善政策問卷調查 將邀縣市長候選人回應', '09-10 10:15', '25']
['全球', '瑞典國會選舉 極右翼得票大增', '09-10 10:13', '44']
['股市', '金屬價格上沖下洗 電子零組件啟動利差翹翹板', '09-10 10:12', '1']
...
```

做到這，我們已經可以順利的將[聯合新聞網即時版](https://udn.com/news/breaknews/1)的第一頁乾淨整齊的取出來，但通常我們在蒐集資料的時候，我們要的不會僅有第一頁，因此需要翻頁繼續往後爬，接下來的課程將教各位如何在[聯合新聞網即時版](https://udn.com/news/breaknews/1)取得過去的歷史資料！

### 翻頁
在先的課程中，有些網站可以單純地透過更改網址達到網頁翻頁的效果 (在 [Python 網路爬蟲課程 2](/8ZVF56fBQ-ydJC5Sj0Gubg) 網頁爬蟲翻頁，沒跟到的同學可以先到第 2 章練習)，但在這次的網站[聯合新聞網即時版](https://udn.com/news/breaknews/1)無法透過更改網址中的頁碼進而翻頁，原因在於該網頁沒有翻頁機制，而是拉到網頁的最底部點選 ![](https://i.imgur.com/v9CZjn0.png =80x20) 來取得更多文章，因此，我們需要找到取得舊文章的其他方法！
![](https://i.imgur.com/ay8HSPE.png)

#### 尋找可用於爬取歷史資料的位置
此時，我們需要在 [Chrome](https://www.google.com/intl/zh-TW_ALL/chrome/) 瀏覽器透過滑鼠按`右鍵`，選擇`檢查`打開底下的工具列
![](https://i.imgur.com/dt80lNA.png)

接著選取 `Network`
![](https://i.imgur.com/5nG5cb0.png)

再來請選擇左上角的 ![](https://i.imgur.com/WyloH49.png =30x30) 清空所有和網站溝通留下的資訊
![](https://i.imgur.com/oaH02aj.png)

清空之後，點擊 ![](https://i.imgur.com/v9CZjn0.png =80x20) 觀察在做這個動作之後是如何和網頁呼叫取得後續的資料
![](https://i.imgur.com/yGggxPB.png)

點擊之後，會跑出許多的文件，這時候我們向上拉，找到第一個取得的文件
![](https://i.imgur.com/y2xrWog.jpg)

打開會發現裡面有一串網址，這是我們可以用來觀察的對象
![](https://i.imgur.com/xYpSMdE.png)

我們將取得的網址貼回瀏覽器中觀察，從下圖來觀察，可以發現取得的網址同樣可以取得新聞，且更改網址能夠成功的翻頁
![](https://i.imgur.com/paocTCO.jpg)

在網址的部分，經過實測，最後的 `?_=xxxxxx` 拿掉不影響網頁顯示，因此在程式碼定義網址的時候不放沒關係
![](https://i.imgur.com/LtL0yXl.png)

接著嘗試更改網址中有數字的部分，發現改第一個數字有翻頁的效果，因此這個網址便是我們要用來爬歷史資料的網址
![](https://i.imgur.com/XgRa5np.png)

#### 撰寫程式
首先，我把頁碼和 url 定義好，在 url 中使用 {} 為後續透過迴圈填入頁碼填入所用
接下來的程式碼帶大家取得第 1 頁
```python=+
page = 1
url = 'https://udn.com/news/get_breaks_article/{}/1/0'
res = requests.get(url.format(page))
soup = BeautifulSoup(res.text, 'html.parser')
```

在網頁中，所有的新聞資料都被原始碼 `class="lazyload"` 所包覆，因此撰寫程式時可以使用
![](https://i.imgur.com/4gllswb.png)

我先透過 `.find_all()` 來觀察會取得什麼資料，程式碼：
```python=+
for i in soup.find_all(class_='lazyload'):
    print(i.text)
```

執行結果：
```
要聞陳學聖：讓新住民融入變城市助力 工作權是關鍵09-16 21:51155
要聞三峽競總成立蘇貞昌竟動怒 展現嚴格治軍好口才09-16 21:473873
數位iPhone XS預購熱 潛藏這些迷思09-16 21:368370
運動柏林馬／基普喬蓋改寫世界紀錄 肯亞總統稱國家英雄09-16 21:35427
文教居禮夫人不再冠夫姓？宅神：也不能講德國總理梅克爾了09-16 21:2915977
生活肺心為您／兩岸交流 陸研發針刺麻醉、肺幹細胞移植09-16 21:18344
生活肺心為您／心肌梗塞沒有症狀？醫師說其實有這幾種09-16 21:185688
生活肺心為您／不只造成肺病 這些疾病也與空汙有關09-16 21:18822
社會疑租賃糾紛惹禍 6旬房東遇刺身亡09-16 21:181594
...
```
透過這樣的方法，我們已經可以順利的取出`新聞標題`、`日期`和`觀看人數`，這些內容我們要存入資料庫中，因此要整理成存入資料庫的格式。另外，每個新聞的網址也是我們要蒐集的對象，因此程式碼為：
```python=+
for i in soup.find_all(class_='lazyload'):
    tag = i.find(class_ = 'cate').text
    title = i.find('h2').text
    date = i.find(class_ = 'dt').text
    view = i.find(class_ = 'view').text
    href = 'https://udn.com' + i.find('h2').find('a').get('href')
    print([tag, title, date, view, href])
```

執行結果：
```
['要聞', '陳學聖：讓新住民融入變城市助力 工作權是關鍵', '09-16 21:51', '155', 'https://udn.com/news/story/10958/3371093?from=udn-ch1_breaknews-1-0-news']
['要聞', '三峽競總成立蘇貞昌竟動怒 展現嚴格治軍好口才', '09-16 21:47', '3873', 'https://udn.com/news/story/10958/3371087?from=udn-ch1_breaknews-1-0-news']
['數位', 'iPhone XS預購熱 潛藏這些迷思', '09-16 21:36', '8370', 'https://udn.com/news/story/12467/3371065?from=udn-ch1_breaknews-1-0-news']
['運動', '柏林馬／基普喬蓋改寫世界紀錄 肯亞總統稱國家英雄', '09-16 21:35', '427', 'https://udn.com/news/story/7005/3371064?from=udn-ch1_breaknews-1-0-news']
['文教', '居禮夫人不再冠夫姓？宅神：也不能講德國總理梅克爾了', '09-16 21:29', '15977', 'https://udn.com/news/story/12401/3371062?from=udn-ch1_breaknews-1-0-news']
['生活', '肺心為您／兩岸交流 陸研發針刺麻醉、肺幹細胞移植', '09-16 21:18', '344', 'https://udn.com/news/story/7266/3371050?from=udn-ch1_breaknews-1-0-news']
['生活', '肺心為您／心肌梗塞沒有症狀？醫師說其實有這幾種', '09-16 21:18', '5688', 'https://udn.com/news/story/7266/3371051?from=udn-ch1_breaknews-1-0-news']
['生活', '肺心為您／不只造成肺病 這些疾病也與空汙有關', '09-16 21:18', '822', 'https://udn.com/news/story/7266/3371053?from=udn-ch1_breaknews-1-0-news']
['社會', '疑租賃糾紛惹禍 6旬房東遇刺身亡', '09-16 21:18', '1594', 'https://udn.com/news/story/7315/3371049?from=udn-ch1_breaknews-1-0-news']
...
```

做到這邊，同學們順利的將第 1 頁新聞整理好印出來，接下來的程式碼的程式邏輯是不斷的翻頁印出
:::warning
:warning: 請注意：下列程式碼沒有迴圈的停止條件，執行後會不斷的向前翻頁，請適時停止程式！
:::
```python=+
page = 1

while True:    
    url = 'https://udn.com/news/get_breaks_article/{}/1/0'
    res = requests.get(url.format(page))
    soup = BeautifulSoup(res.text, 'html.parser')

    for i in soup.find_all(class_='lazyload'):
        tag = i.find(class_ = 'cate').text
        title = i.find('h2').text
        date = i.find(class_ = 'dt').text
        view = i.find(class_ = 'view').text
        href = 'https://udn.com' + i.find('h2').find('a').get('href')
        print([tag, title, date, view, href])

    page += 1
```

做到這邊，老師要出個**作業**給各位，期望各位同學運用先前所學，在迴圈中加入判斷日期的**停止條件**
**請同學將新聞往回爬取 3 天存到 SQLite，3 天的資料蒐集完即停止迴圈**，解答就請各位同學完成後，再到 [Python 網路爬蟲課程 5](/xJ2ulqdNSFyfHb7MUZFwZQ) 看看和自己所想的邏輯是否一樣！

---
:::success
第四堂課結束囉:100:
請務必實際練習過上面的題目，這樣才會成長喔！
:::
###### tags: `Python` `Python 網路爬蟲課程` `Crawler` `網路爬蟲` `SQLite`
# Python 網路爬蟲課程 6

:::warning
:warning: 注意事項 :warning:
* 課程內容以 Python 爬蟲為主軸，Python 基礎不會著墨過深，基礎的部份遇到困難請同學善用 [Google](https://www.google.com/)
* 課程內容是本人的嘔心瀝血之作，若有引用請標明出處
* 本文最後編輯日期：2020/01/09
:::

## 課堂使用環境安裝 :computer:
* 本課程使用 [Anaconda](https://www.anaconda.com/download/) 做為教學環境
* 請下載對應電腦作業系統的 Python 3.6 版本
* 詳細安裝流程 :point_right: [Python Anaconda 環境安裝教學](/h5XtZtlRSB2TQP-marFL5g)
* [Python 網路爬蟲課程 2](/8ZVF56fBQ-ydJC5Sj0Gubg) 之後的課程均使用 [Google Chrome](https://www.google.com/intl/zh-TW_ALL/chrome/) 作為課堂所用，請在課堂開始前先行安裝完成

## PTT 表特板圖片爬取實戰
本課程延伸 [Python 網路爬蟲課程 5](/xJ2ulqdNSFyfHb7MUZFwZQ)，因此未完成的同學請先至上堂刻完成課程內容在觀看這門課！

上一堂課教大家爬取 PTT 的文字，而這門課和前面所有的課程不同，教你將網站上的圖片爬下來存在資料夾中，省下大家一頁一頁點進去的時間，直接將圖片存取下來！

這次請大家到 [PTT 表特版](https://www.ptt.cc/bbs/Beauty/index.html)
![](https://i.imgur.com/EHwBuJ0.png)

接著隨意點進一篇觀察
![](https://i.imgur.com/dG80SAy.png)

可以發現到裡面每張圖片都有一個相對應的網址，這邊老師幫大家整理出來圖片網址會有的幾種型態如下：
* http://i.imgur.com/A2wmlqW.jpg
* http://i.imgur.com/A2wmlqW  # 沒有 .jpg
* https://i.imgur.com/A2wmlqW.jpg
* http://imgur.com/A2wmlqW.jpg
* https://imgur.com/A2wmlqW.jpg
* https://imgur.com/A2wmlqW
* http://m.imgur.com/A2wmlqW.jpg
* https://m.imgur.com/A2wmlqW.jpg

在這門課中，想請大家練習一個技巧叫做 **Regular Expression**，中文名稱為**正則表達式**，正則表達式使用單個字串來描述、匹配一系列符合某個句法規則的字串。在很多文字編輯器裡，正規表達式通常被用來檢索、替換那些符合某個模式的文字

### Regular Expression
請大家到這個網站：https://www.regexpal.com
![](https://i.imgur.com/pp7MMdc.png)

將剛剛列出來的網址貼到 `Test String` 中
![](https://i.imgur.com/hP4QrXV.png)

我們的目標是透過 Regular Expression 將所有網址包含在其中

在範例中，如果輸入 `http://`，會變得沒有辦法包含開頭是 `https://` 的字串
![](https://i.imgur.com/2SKW1Ln.png)

反之，如果輸入 `https://`，會變得沒有辦法包含開頭是 `http://` 的字串
![](https://i.imgur.com/sobXw18.png)

因此在 Regular Expression 中我們可以輸入 `http?://` 解決篩選條件
![](https://i.imgur.com/gRogmQX.png)

接著，鍵入 `i.imgur.com`，會發現有些網址為 `imgur.com` 開頭，無法被包含在其中
![](https://i.imgur.com/iYmDtMA.png)

解決方法和先前類似，改為鍵入`http?://(i.)?imgur.com`，就能包含這兩種資料
![](https://i.imgur.com/zP3ILkj.png)

另外，有些資料是 `m.imgur.com` 開頭，因此需再針對這些資料加入條件，變為 `http?://(i.)?(m.)?imgur.com`
![](https://i.imgur.com/tti1JPd.png)

這樣我們便能把 PTT 表特版中所有對應的網址都抓取進來，開始設計程式吧！

### 爬蟲設計
```python=
import requests
import time
import datetime
import re
import os
import urllib.request
from bs4 import BeautifulSoup

today = time.strftime("%m/%d").lstrip('0')

url = 'https://www.ptt.cc/bbs/Beauty/index.html'
date_list = []
beautiful_href = []

while True:
    while True:
        #送出超過 18 歲
        res = requests.get(url, cookies={'over18': '1'})

        #如果網頁回應是200，將得到的網頁原始碼交給 BeautifulSoup
        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            break
        else:
            print('error')
    
    #找到要的版面
    for i in soup.find_all(class_ = 'r-ent'):
        #找出未被刪除的文章
        if i.find(class_ = 'title').find('a'):
            #如果日期是今日，做下列的事
            if i.find(class_ = 'date').text.replace(' ','') == today:
                title = i.find(class_ = 'title').find('a').text
                date = i.find(class_ = 'date').text.replace(' ','')
                #將這頁的日期存入 list 中
                date_list.append(date)
                reply = i.find(class_ = 'nrec').text
                href = 'https://www.ptt.cc' + i.find(class_ = 'title').find('a').get('href')
                beautiful_href.append(href)
                #找出上一頁網址
                for j in soup.find_all(class_ = 'btn wide'):
                    if '上頁' in j.text:
                        url = 'https://www.ptt.cc/'+j.get('href')
                print(title, date, reply, href)
    
    
    #如果 list 中有今天，將 list 清空
    if today in date_list:
        date_list.clear()
    #如果 list 中 沒有今天，while loop 結束
    elif today not in date_list:
        break
```

到這邊會輸出：
```
[正妹] 上班族 7/14 3 https://www.ptt.cc/bbs/Beauty/M.1531502412.A.0F4.html
[帥哥] 翔 sho (12) 7/14 2 https://www.ptt.cc/bbs/Beauty/M.1531502544.A.8AA.html
[帥哥] Lane 7/14  https://www.ptt.cc/bbs/Beauty/M.1531503221.A.E4C.html
[正妹] 李佳恩 7/14 9 https://www.ptt.cc/bbs/Beauty/M.1531503248.A.1B4.html
[正妹] 泉水らん 7/14 9 https://www.ptt.cc/bbs/Beauty/M.1531510717.A.597.html
[正妹] 短髮女子   7/14 41 https://www.ptt.cc/bbs/Beauty/M.1531516098.A.F04.html
[正妹]辣媽 7/14 16 https://www.ptt.cc/bbs/Beauty/M.1531529373.A.BC9.html
[帥哥] 傑尼斯王子總選舉2018 7/14  https://www.ptt.cc/bbs/Beauty/M.1531535272.A.C68.html
[正妹] 希島愛里 (希島あいり) 7/14 8 https://www.ptt.cc/bbs/Beauty/M.1531536266.A.FFE.html
[神人] 五官精緻的記者妹妹 7/14 1 https://www.ptt.cc/bbs/Beauty/M.1531537313.A.9F7.html
[正妹] 肉特(85) 7/14 4 https://www.ptt.cc/bbs/Beauty/M.1531537431.A.058.html
[神人] 成吉思汗綜合格鬥比賽舉牌妹 7/14 10 https://www.ptt.cc/bbs/Beauty/M.1531539061.A.38B.html
[正妹] 日曆女孩 7/14 5 https://www.ptt.cc/bbs/Beauty/M.1531539964.A.080.html
[廣告] 燦坤7月會員特典 全館5折起 | 7/13-7/16  7/14 X3 https://www.ptt.cc/bbs/Beauty/M.1531540865.A.B10.html
[正妹] 軟特 7/14 13 https://www.ptt.cc/bbs/Beauty/M.1531542036.A.21B.html
[正妹] 初音實 (初音みのり) 7/14 12 https://www.ptt.cc/bbs/Beauty/M.1531544140.A.AE9.html
[正妹] 東森新聞-蕭景云 7/14  https://www.ptt.cc/bbs/Beauty/M.1531546476.A.840.html
Re: [正妹] 黑絲好身材-波蘭部落客 7/14 38 https://www.ptt.cc/bbs/Beauty/M.1531547965.A.735.html
[正妹] 迪士尼女孩 7/14 4 https://www.ptt.cc/bbs/Beauty/M.1531554056.A.642.html
[正妹] 大學生 7/14 5 https://www.ptt.cc/bbs/Beauty/M.1531502375.A.C4B.html
```

接著在繼續撰寫
```python=
ima_list = []
for beauti in beautiful_href:
    res = requests.get(beauti)
    soup = BeautifulSoup(res.text, 'html.parser')
    imgur = soup.find(id='main-content').find_all('a')
    for i in imgur:
        if re.match(r'^https?://(i.)?(m.)?imgur.com', i['href']):
            ima_list.append(i['href'])
            print(beauti, i['href'])
```

輸出：
```
https://www.ptt.cc/bbs/Beauty/M.1531502412.A.0F4.html https://imgur.com/PSYrW2a.jpg
https://www.ptt.cc/bbs/Beauty/M.1531502412.A.0F4.html https://imgur.com/77iKYoJ.jpg
https://www.ptt.cc/bbs/Beauty/M.1531502412.A.0F4.html https://imgur.com/y8Igy35.jpg
https://www.ptt.cc/bbs/Beauty/M.1531502412.A.0F4.html https://imgur.com/ab5wKrQ.jpg
https://www.ptt.cc/bbs/Beauty/M.1531502412.A.0F4.html https://imgur.com/hiwOuRo.jpg
https://www.ptt.cc/bbs/Beauty/M.1531502412.A.0F4.html https://imgur.com/VKP4LSJ.jpg
https://www.ptt.cc/bbs/Beauty/M.1531502544.A.8AA.html https://i.imgur.com/kRbN0YC.jpg
https://www.ptt.cc/bbs/Beauty/M.1531502544.A.8AA.html https://i.imgur.com/03vK4qJ.jpg
https://www.ptt.cc/bbs/Beauty/M.1531502544.A.8AA.html https://i.imgur.com/MbUmCKK.jpg
https://www.ptt.cc/bbs/Beauty/M.1531502544.A.8AA.html https://i.imgur.com/npfyWWI.jpg
https://www.ptt.cc/bbs/Beauty/M.1531502544.A.8AA.html https://i.imgur.com/jazB2zp.jpg
https://www.ptt.cc/bbs/Beauty/M.1531502544.A.8AA.html https://i.imgur.com/Qjt9err.jpg
https://www.ptt.cc/bbs/Beauty/M.1531502544.A.8AA.html https://i.imgur.com/3FK4B0L.jpg
https://www.ptt.cc/bbs/Beauty/M.1531502544.A.8AA.html https://i.imgur.com/sO6dBHT.jpg
https://www.ptt.cc/bbs/Beauty/M.1531503221.A.E4C.html https://i.imgur.com/4el7zto.jpg
...
```

```python=
for url in ima_list:
    if url.split('//')[1].startswith('m.'):
        url = url.replace('//m.', '//i.')
    if not url.split('//')[1].startswith('i.'):
        url = url.split('//')[0] + '//i.' + url.split('//')[1]
    if not url.endswith('.jpg'):
        url += '.jpg'
    fname = url.split('/')[-1]
    print(fname)
    urllib.request.urlretrieve(url, os.path.join('~/today', fname))
    
# ~/today 請改為自己要存圖片的資料夾
```

輸出：
```
PSYrW2a.jpg
77iKYoJ.jpg
y8Igy35.jpg
ab5wKrQ.jpg
hiwOuRo.jpg
VKP4LSJ.jpg
kRbN0YC.jpg
03vK4qJ.jpg
MbUmCKK.jpg
npfyWWI.jpg
jazB2zp.jpg
Qjt9err.jpg
3FK4B0L.jpg
sO6dBHT.jpg
...
```

執行完後，就可以到資料夾看成果了
![](https://i.imgur.com/GBwb1SZ.png)

這堂課到這邊就結束囉，我們 [Python 網路爬蟲課程 7](/fIr3TZVLTHufUpa54boJsw) 見 :eyes:

---
:::success
第六堂課結束囉:100:
請務必實際練習過上面的題目，這樣才會成長喔！
在這，我要出一份作業給大家，因為要找出公認的美女，因此請大家只爬回覆數大於等於 30 的美女圖 100 篇，小提示：透過 if 判斷回文數
:::

###### tags: `Python` `Python 網路爬蟲課程` `Crawler` `網路爬蟲` `SQLite`
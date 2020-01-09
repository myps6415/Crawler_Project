# Python 網路爬蟲課程 7

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

## [Python 網路爬蟲課程 6](/u_XHEOtyRamzAxJ30IzZXw) 作業
在上一堂課的最後，有出了一個作業，只爬回覆數大於等於 30 的美女圖 100 篇，請沒有完成的同學先不要看解答，自己嘗試看看，這樣才會進步喔 :+1:

```python=
import requests
import time
import datetime
import re
import os
import sys
import urllib.request
from bs4 import BeautifulSoup

url = 'https://www.ptt.cc/bbs/Beauty/index.html'
beauty_url = []
image_url = []

while len(beauty_url) < 100:
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
        #檢查是否被刪文
        if i.find(class_ = 'title').find('a'):
            #將爬到的回文數改為數值型態，並比較是否大於等於 30
            if i.find(class_ = 'nrec').text:
                #如果值是爆，是我們要的
                if '爆' in i.find(class_ = 'nrec').text:
                    reply_num = 100
                elif 'X' in i.find(class_ = 'nrec').text:
                    reply_num = 100
                else:
                    reply_num = int(i.find(class_ = 'nrec').text)
                    
                if reply_num >= 30:
                    title = i.find(class_ = 'title').find('a').text
                    if '公告' not in title:
                        href = 'https://www.ptt.cc' + i.find(class_ = 'title').find('a').get('href')
                        if len(beauty_url) < 100:
                            beauty_url.append(href)
                            res2 = requests.get(href, cookies={'over18': '1'})
                            soup2 = BeautifulSoup(res2.text, 'html.parser')
                            imgur = soup2.find(id='main-content').find_all('a')
                            for i in imgur:
                                if re.match(r'^https?://(i.)?(m.)?imgur.com', i['href']):
                                    image_url.append(i['href'])
                                    print(len(beauty_url), title, href, i['href'])

    #找出上一頁網址
    for j in soup.find_all(class_ = 'btn wide'):
        if '上頁' in j.text:
            url = 'https://www.ptt.cc/'+j.get('href')
```

輸出：
```
1 [正妹] 戰鬥民族妹子 https://www.ptt.cc/bbs/Beauty/M.1531921396.A.7C7.html https://i.imgur.com/HovMUeb.jpg
1 [正妹] 戰鬥民族妹子 https://www.ptt.cc/bbs/Beauty/M.1531921396.A.7C7.html https://i.imgur.com/haskvJ8.jpg
1 [正妹] 戰鬥民族妹子 https://www.ptt.cc/bbs/Beauty/M.1531921396.A.7C7.html https://i.imgur.com/zbVvQrA.jpg
1 [正妹] 戰鬥民族妹子 https://www.ptt.cc/bbs/Beauty/M.1531921396.A.7C7.html https://i.imgur.com/k0aHl5A.jpg
1 [正妹] 戰鬥民族妹子 https://www.ptt.cc/bbs/Beauty/M.1531921396.A.7C7.html https://i.imgur.com/hIYJR7H.jpg
1 [正妹] 戰鬥民族妹子 https://www.ptt.cc/bbs/Beauty/M.1531921396.A.7C7.html https://i.imgur.com/Lpljpiq.jpg
1 [正妹] 戰鬥民族妹子 https://www.ptt.cc/bbs/Beauty/M.1531921396.A.7C7.html https://i.imgur.com/NdoNJHI.jpg
1 [正妹] 戰鬥民族妹子 https://www.ptt.cc/bbs/Beauty/M.1531921396.A.7C7.html https://i.imgur.com/WQAqPnq.jpg
1 [正妹] 戰鬥民族妹子 https://www.ptt.cc/bbs/Beauty/M.1531921396.A.7C7.html https://i.imgur.com/FvJn2OQ.jpg
1 [正妹] 戰鬥民族妹子 https://www.ptt.cc/bbs/Beauty/M.1531921396.A.7C7.html https://i.imgur.com/o6YMVhO.jpg
1 [正妹] 戰鬥民族妹子 https://www.ptt.cc/bbs/Beauty/M.1531921396.A.7C7.html https://i.imgur.com/T92KYky.jpg
1 [正妹] 戰鬥民族妹子 https://www.ptt.cc/bbs/Beauty/M.1531921396.A.7C7.html https://i.imgur.com/nJafBIt.jpg
2 [正妹] 就3張 https://www.ptt.cc/bbs/Beauty/M.1531875994.A.F01.html https://i.imgur.com/v2LKO0c.jpg
2 [正妹] 就3張 https://www.ptt.cc/bbs/Beauty/M.1531875994.A.F01.html https://i.imgur.com/0SxWQYi.jpg
2 [正妹] 就3張 https://www.ptt.cc/bbs/Beauty/M.1531875994.A.F01.html https://i.imgur.com/ri6RDgC.jpg
2 [正妹] 就3張 https://www.ptt.cc/bbs/Beauty/M.1531875994.A.F01.html http://i.imgur.com/EayfffK.jpg
2 [正妹] 就3張 https://www.ptt.cc/bbs/Beauty/M.1531875994.A.F01.html http://i.imgur.com/vMr85Ln.jpg
2 [正妹] 就3張 https://www.ptt.cc/bbs/Beauty/M.1531875994.A.F01.html http://i.imgur.com/qwxJAIh.jpg
3 [正妹] 今天是瑤瑤 郭書瑤生日 https://www.ptt.cc/bbs/Beauty/M.1531880122.A.506.html https://imgur.com/VlVEJQn.jpg
3 [正妹] 今天是瑤瑤 郭書瑤生日 https://www.ptt.cc/bbs/Beauty/M.1531880122.A.506.html https://imgur.com/lNC2GQm.jpg
3 [正妹] 今天是瑤瑤 郭書瑤生日 https://www.ptt.cc/bbs/Beauty/M.1531880122.A.506.html https://imgur.com/9IdWlzg.jpg
...
```

接著撰寫
```python=
for index, url in enumerate(image_url):
    percent = (float(index)+1) / float(len(image_url)) * 100
    
    if url.split('//')[1].startswith('m.'):
        url = url.replace('//m.', '//i.')
    if not url.split('//')[1].startswith('i.'):
        url = url.split('//')[0] + '//i.' + url.split('//')[1]
    if not url.endswith('.jpg'):
        url += '.jpg'
    fname = url.split('/')[-1]
    try:
        urllib.request.urlretrieve(url, os.path.join('/home/fish/桌面/beauty_30up', fname))
        sys.stdout.write("%.2f"%percent)
        sys.stdout.write("%, ")
        sys.stdout.write(url+'\r')
        sys.stdout.flush()
    except:
        pass
```

輸出：
```
100.00%, https://i.imgur.com/DkV6dXe.jpgjpg
```

以上就是作業的撰寫方式，可以順利的爬下評論數大於 30 的 100 篇文章！

學了這麼多東西，我想是時候讓大家回憶過去所學，來個小考吧！滿分 110 分
```
1. 將 teacher_hope 字串透過逗號 (，) 斷開 (10%)
teacher_hope = '各位同學，時光匆匆來到了第七堂課，老師希望各位有從課程中學到東西，最重要的是覺得 Python 有趣，未來這堂課程結束仍然持續接觸，這是老師所樂見的事情'

2. 印出一個存有 1 ~ 500 的 list (10%)
3. 印出 feebee 網站比價 iPhone X 的結果 (15%)
(https://feebee.com.tw/product/iPhone%20X%20256G%20%E6%99%BA%E6%85%A7%E5%9E%8B%E6%89%8B%E6%A9%9F/?q=iphone%20x)
4. 印出蘋果日報編號、標題、觀看人數 (15%)(https://tw.appledaily.com/hot/daily)
5. 若能多印出蘋果日報網址，加 5 分 (5%)
6. 透過 Pandas 套件讀取 SQLite 資料庫，並印出前五筆資料 (10%)
7. 叫出表中的 title 資料 (5%)
8. 列出 tag 欄位的佔比 (5%)
9. 畫出 tag 佔比的長條圖 (中文顯示不出來沒關係) (5%)
10. 印出 PTT 八卦板今日文章前 40 篇標題 (20%)
11. [加分題] 對這門課有任何心得感想，請在下列寫下 (10%)
```

這堂課到這邊就結束囉，我們 [Python 網路爬蟲課程 8](/iDU6Bhq7QMOPBF2tL2kwDA) 見 :eyes:

---
:::success
第七堂課結束囉:100:
考試加油，Open book
不會的可以 Google !!!
:::

###### tags: `Python` `Python 網路爬蟲課程` `Crawler` `網路爬蟲` `SQLite`
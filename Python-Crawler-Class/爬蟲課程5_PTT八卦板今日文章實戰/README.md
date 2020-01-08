# Python 網路爬蟲課程 5

:::warning
:warning: 注意事項 :warning:
* 課程內容以 Python 爬蟲為主軸，Python 基礎不會著墨過深，基礎的部份遇到困難請同學善用 [Google](https://www.google.com/)
* 課程內容是本人的嘔心瀝血之作，若有引用請標明出處
* 本文最後編輯日期：2020/01/08
:::

## 課堂使用環境安裝 :computer:
* 本課程使用 [Anaconda](https://www.anaconda.com/download/) 做為教學環境
* 請下載對應電腦作業系統的 Python 3.6 版本
* 詳細安裝流程 :point_right: [Python Anaconda 環境安裝教學](/h5XtZtlRSB2TQP-marFL5g)
* [Python 網路爬蟲課程 2](/8ZVF56fBQ-ydJC5Sj0Gubg) 之後的課程均使用 [Google Chrome](https://www.google.com/intl/zh-TW_ALL/chrome/) 作為課堂所用，請在課堂開始前先行安裝完成

## [Python 網路爬蟲課程 4](/AVX1bD4FSaCj4f84fY5RrQ) 課後練習
* 請將[聯合新聞網即時版](https://udn.com/news/breaknews/1)往回爬取 3 天存到 SQLite，3 天的資料蒐集完即停止迴圈

如果還沒有實際操作這部分的同學，請先不要看這一節的內容，請回到 [Python 網路爬蟲課程 4](/AVX1bD4FSaCj4f84fY5RrQ) 實際練習後再看本節解答！

:::info
完成練習的同學，我們來看講解吧：
:::

老師在撰寫本題解答的日期為 2018/09/19，因此包含當天往回算 3 天為 2018/09/17，在這個題目中，我們有兩種方法可以解決：

### 方法一：加入 if 判斷日期：
在程式碼中，我在 while 迴圈中加入 if 判斷日期若出現第 4 天，則停止，因此在我寫解答的今天往回推 4 天為 09-16
```python=
import requests
from bs4 import BeautifulSoup
import time

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
        if '09-16' not in date:
            print([tag, title, date, view, href])
        
    if '09-16' in date:
        print('DONE')
        break

    page += 1
```

執行結果：
```
['生活', '藍營政治化翠玉白菜？卓冠廷：請尊重台中人', '09-19 14:46', '346', 'https://udn.com/news/story/7266/3376141?from=udn-ch1_breaknews-1-0-news']
['股市', '華映證實裁員 幅度約1.4%屬末位淘汰調整 ', '09-19 14:45', '1390', 'https://udn.com/news/story/7253/3376136?from=udn-ch1_breaknews-1-0-news']
['要聞', '扁同意擔任姚文智競選顧問 中監：了解評估處理', '09-19 14:43', '617', 'https://udn.com/news/story/10958/3376135?from=udn-ch1_breaknews-1-0-news']
...
['運動', '中職／高三棄游從投 成就火球男吳世豪、朱俊祥', '09-17 07:00', '13236', 'https://udn.com/news/story/7001/3370936?from=udn-ch1_breaknews-1-0-news']
['運動', '外卡殊死戰大難臨頭 洋基還在找自己的領袖', '09-17 07:00', '24417', 'https://udn.com/news/story/6999/3370986?from=udn-ch1_breaknews-1-0-news']
['運動', '日職／郭俊麟奇兵致勝 西武避免憾事重演', '09-17 07:00', '11514', 'https://udn.com/news/story/7001/3370927?from=udn-ch1_breaknews-1-0-news']
DONE
```

### 方法二：while 迴圈加入停止條件
第二個方法使用 while 迴圈的特性，while 迴圈要在 True 的情形下才會不斷的執行，因此一開始執行時， `'09-16' not in date` 是 True，直到 17 日的資料爬完會轉為 False，因此中止迴圈！
```python=
import requests
from bs4 import BeautifulSoup
import time

page = 1
date = ''

while '09-16' not in date:    
    url = 'https://udn.com/news/get_breaks_article/{}/1/0'
    res = requests.get(url.format(page))
    soup = BeautifulSoup(res.text, 'html.parser')

    for i in soup.find_all(class_='lazyload'):
        tag = i.find(class_ = 'cate').text
        title = i.find('h2').text
        date = i.find(class_ = 'dt').text
        view = i.find(class_ = 'view').text
        href = 'https://udn.com' + i.find('h2').find('a').get('href')
        if '09-16' not in date:
            print([tag, title, date, view, href])

    page += 1
```

執行結果：
```
['生活', '藍營政治化翠玉白菜？卓冠廷：請尊重台中人', '09-19 14:46', '346', 'https://udn.com/news/story/7266/3376141?from=udn-ch1_breaknews-1-0-news']
['股市', '華映證實裁員 幅度約1.4%屬末位淘汰調整 ', '09-19 14:45', '1390', 'https://udn.com/news/story/7253/3376136?from=udn-ch1_breaknews-1-0-news']
['要聞', '扁同意擔任姚文智競選顧問 中監：了解評估處理', '09-19 14:43', '617', 'https://udn.com/news/story/10958/3376135?from=udn-ch1_breaknews-1-0-news']
...
['運動', '中職／高三棄游從投 成就火球男吳世豪、朱俊祥', '09-17 07:00', '13236', 'https://udn.com/news/story/7001/3370936?from=udn-ch1_breaknews-1-0-news']
['運動', '外卡殊死戰大難臨頭 洋基還在找自己的領袖', '09-17 07:00', '24417', 'https://udn.com/news/story/6999/3370986?from=udn-ch1_breaknews-1-0-news']
['運動', '日職／郭俊麟奇兵致勝 西武避免憾事重演', '09-17 07:00', '11514', 'https://udn.com/news/story/7001/3370927?from=udn-ch1_breaknews-1-0-news']
```

## 作業延伸：存到 SQLite
在這一節中，請各位同學將上面作業爬的資料存到 SQLite 中，如果忘記做法請到 [Python 網路爬蟲課程 2](/8ZVF56fBQ-ydJC5Sj0Gubg) 複習怎將資料存到資料庫喔！
:::danger
這邊請同學先完成，才有辦法繼續後面的課程！
:::
---
## PTT 八卦板今日文章實戰
在網頁版的 PTT 中，首先會碰到的狀況就是需要認證是滿 18 歲
![](https://i.imgur.com/z0P8D5z.png)

因此我們需要先了解這個狀況下的運作規則，請在 Chrome 瀏覽器下的檢查，點取 Network
![](https://i.imgur.com/NwF4L4i.png)

設定好後點取網頁中的「我同意，我已年滿十八歲進入」，在此步驟之後會看到檢查列開始跳出網頁的回應資訊
![](https://i.imgur.com/nqO6MUh.png)

在這邊可以找到第一筆產生的資料「over18」，將其點擊觀察內容
![](https://i.imgur.com/4bkZsNC.png)

可以觀察到當中 `set-cookie` 內含有 `over18=1`，這就是我們所需的寫在爬蟲中的資訊

釐清了必要的資訊之後，我們就可以完整的規劃爬蟲程式設計的流程：
1. 定義今日日期
2. 進入頁面
3. 取得頁面中的所有今日文章與上一頁的網址
4. 頁面中包含今日文章，將其印出後，連到上一頁進行步驟 3

完整程式碼：
```python=
import requests
import time
import datetime
import sqlite3
from bs4 import BeautifulSoup

today = time.strftime("%m/%d").lstrip('0')

url = 'https://www.ptt.cc/bbs/Gossiping/index.html'
date_list = []

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
                #找出上一頁網址
                for j in soup.find_all(class_ = 'btn wide'):
                    if '上頁' in j.text:
                        url = 'https://www.ptt.cc/'+j.get('href')
                print(title, date, reply)
    
    
    #如果 list 中有今天，將 list 清空
    if today in date_list:
        date_list.clear()
    #如果 list 中 沒有今天，while loop 結束
    elif today not in date_list:
        break
```

輸出：
```
Re: [新聞] 丁守中：因為找網紅很花錢 沒找網紅合作 7/13 4
Re: [新聞] 丁守中：因為找網紅很花錢 沒找網紅合作 7/13 4
[問卦] 日本鄉下的水土保持比台灣爛? 7/13 3
Re: [問卦] 說月收少經濟差不生小孩是否可悲？ 7/13 
Re: [新聞] 丁守中：因為找網紅很花錢 沒找網紅合作 7/13 3
[問卦] 急!怎麼複製魔鏡歌詞網的歌詞  在線等 7/13 
[問卦] 為什麼男生越壞女生越愛 7/13 2
[問卦] 有沒有材料、化工、光電三者的關係？ 7/13 1
[新聞] 傳內閣將改組 林佳龍建議多下鄉宣傳政績 7/13 
Re: [問卦] 少子化真的是全民問題嗎? 7/13 
[新聞] 恐空汙害的？！醫：肺癌患者高達7成不 7/13 
Re: [問卦] 歐洲人是不是不太打籃球 7/13 1
[新聞] 回到20年前！安大略省重啟舊版性別教育 7/13 4
[問卦] 去工地蹲過的水電工作擁高收入是應得的吧 7/13 5
Re: [問卦] 最近PTT白天為什麼都容易過載? 7/13 
...
```

到這邊，就能夠順利印出標題，日期及回應數，期望各位同學能夠自己練習包含爬取到網址，甚至爬到內文，以及之前上課教過的怎麼存到資料庫中！

這堂課到這邊就結束囉，我們 [Python 網路爬蟲課程 6](/u_XHEOtyRamzAxJ30IzZXw) 見 :eyes:

---
:::success
第五堂課結束囉:100:
請務必實際練習過上面的題目，這樣才會成長喔！
:::

###### tags: `Python` `Python 網路爬蟲課程` `Crawler` `網路爬蟲` `SQLite`
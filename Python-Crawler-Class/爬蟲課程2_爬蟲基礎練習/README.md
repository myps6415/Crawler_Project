# Python 網路爬蟲課程 2
:::warning
:warning: 注意事項 :warning:
* 課程內容以 Python 爬蟲為主軸，Python 基礎不會著墨過深，基礎的部份遇到困難請同學善用 [Google](https://www.google.com)
* 課程內容是本人的嘔心瀝血之作，若有引用請標明出處
* 本文最後編輯日期：2018/08/07
:::

## 課堂使用環境安裝 :computer:
* 本課程使用 [Anaconda](https://www.anaconda.com/download/) 做為教學環境
* 請下載對應電腦作業系統的 Python 3.6 版本
* 詳細安裝流程 :point_right: [Python Anaconda 環境安裝教學](/h5XtZtlRSB2TQP-marFL5g)
* [Python 網路爬蟲課程 2](/8ZVF56fBQ-ydJC5Sj0Gubg) 之後的課程均使用 [Google Chrome](https://www.google.com/intl/zh-TW_ALL/chrome/) 作為課堂所用，請在課堂開始前先行安裝完成

## 基礎課程導引 :triangular_flag_on_post:
* 如果對 Python 完全沒有基礎，請先到第一堂課惡補 :point_right: [Python 網路爬蟲課程 1](/O62YpbrzR-KwQxiVhb3CQA)


## 網頁原始碼
網頁是由多個標籤 (tag) 所組成的階層式文件，如圖
![](https://i.imgur.com/5lW9fRW.png)

因此我們可以從中找出規則，透過撰寫程式自動歸納整理對我們而言有用的資訊

## 撰寫爬蟲前
動手撰寫爬蟲之前，先不要衝動直接打開程式編輯器，應該先想想看有沒有現成的服務或工具已經有想要的資訊了，例如：
* 現成的服務 ([XQ 操盤高手](https://www.xq.com.tw/XQlite-Download.aspx))
* 包好的資料 ([維基百科](https://zh.wikipedia.org/wiki/Wikipedia:%E6%95%B0%E6%8D%AE%E5%BA%93%E4%B8%8B%E8%BD%BD))
* 其他人寫好分享的程式 ([Yahoo 新聞](https://github.com/TTPLP/Project-Yahoo-News-Crawler-hitler11319))

如果已經有現成的東西能夠使用，就能夠節省時間無需從頭來過了！

### 非得寫程式時，考慮以下順序：
1. 網站是否有提供 API ([Hahow](https://hahow.in), [Youtube](https://www.youtube.com),...)
2. 網址是否有規則 (日期，代號)
3. JavaScript, JSON
4. 網頁很複雜時，找看看有沒有行動版網頁

## 使用 BeautifulSoup
* 用來解析並擷取網頁資訊的 Python 函式庫
* 讓開發者撰寫少量的程式碼即可快速解析網頁原始碼
* 課程安裝的 Anaconda 中已包含 BeautifulSoup，無需額外安裝
* 在課程中大量的和 **Requests** 套件搭配使用

本節以 [Yahoo 購物中心的 ASUS 手機頁](https://tw.buy.yahoo.com/?catitemid=109590)作為課程範例
![](https://i.imgur.com/BFTyJjQ.png)

:::info
本節目的：取得下圖中商品的標題及售價 :eyes:
![](https://i.imgur.com/3FzJ2RL.png)
:::

## 開始寫 Python
### STEP 1：引入 Python 爬蟲套件
首先，在程式的一開始，我們需要引入幾個寫爬蟲所需的函式庫
> :exclamation:注意：寫程式請注意字母大小寫
```python=
import requests
from bs4 import BeautifulSoup
```

### STEP 2：定義要爬的網址
引入之後，我會先定義一個變數名為 **`url`**，變數內容為 [Yahoo 購物中心的 ASUS 手機頁](https://tw.buy.yahoo.com/?catitemid=109590)的網址
```python=+
url = 'https://tw.buy.yahoo.com/?catitemid=109590'
```

### STEP 3：向網址要回資料並解析
透過 requerts 向網頁要資料回來，接著透過 BeautifulSoup 解析網頁原始碼
```python=+
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
```

### STEP 4：透過 Chrome 瀏覽器觀察網頁
接下來，我們要確定網頁中哪個部份是我們要的，才有辦法透過撰寫程式指定位置；因此我們會在瀏覽器中做下列步驟：
1. 點擊滑鼠右鍵
![](https://i.imgur.com/TjY0cYI.png)

2. 對想觀察的物件點擊檢查，此範例對標題按滑鼠右鍵點擊檢查
![](https://i.imgur.com/iK4HQvU.png)

3. 將滑鼠放在原始碼標注藍色底的位置，會發現網頁上香對應的位置也會標記著藍底
![](https://i.imgur.com/iDe9nZc.png)

4. 此時藍底所包覆的位置不包含我們想要的價格，因此我們會用滑鼠在網頁原始碼向上滑動，找到藍底將我們要的資訊都包覆的原始碼
![](https://i.imgur.com/XcDJSId.png)

5. 點擊原始碼左邊的下三角符號 (![](https://i.imgur.com/5S3aK80.png)) 將原始碼縮小觀察，會發現許多相似的原始碼
![](https://i.imgur.com/iW740ox.png)

6. 滑鼠移到其他相似的原始碼上，能夠發現以相同的格式標記著其他商品資訊，因此確認找到的這些 tag 是要用在寫程式中的
![](https://i.imgur.com/FugStvE.png)

### STEP 5：透過 .find() 取出指定的 tag
在這一步驟，我們嘗試使用 BeautifulSoup 的 **`.find()`** 功能取出第一個 tag
```python=+
soup.find(class_ = 'item yui3-u srp-multi-image')
```

執行結果如下，和瀏覽器中觀察的一樣：
```
<div class="item yui3-u srp-multi-image" data-cluster="智慧型手機" data-ga-label="7841193" data-level="4_430_6859_109590" data-mlrscore="" data-p="1" data-pid="7841193" data-ppos="1" data-score="0.0">
<div class="wrap">
<div class="srp-carousel">
<div class="carousel">
<div class="carousel-list yui3-g">
<div class="srp-pdimage cf content yui3-u">
<a data-slk="image" data-ylk="sec:item;pid:7841193;itemid:7841193;slk:image" href="https://tw.buy.yahoo.com/gdsale/ASUS-ZenFone-Max-Pro-ZB60-7841193.html" title="ASUS ZenFone Max Pro ZB602KL(6G/64G)">
<img alt="ASUS ZenFone Max Pro ZB602KL(6G/64G)" height="180" src="https://s.yimg.com/zp/MerchandiseImages/1DD30F5F94-SP-5924162.jpg" width="180"/>
</a>
...
```

### STEP 6：透過 .text 取得 tag 中的文字
剛剛我們已經可以順利的取得指定的原始碼，但對我們來說重要的是原始碼中的資訊，因此這邊教大家使用 **`.text`** 來取得原始碼中的文字
```python=+
soup.find(class_='item yui3-u srp-multi-image').text
```

執行結果如下，可以發現原始碼已經不在了，但仍有對我們來說是雜訊的**換行符號**，因此要用其他方法來處理這串文字：
```
'\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nASUS ZenFone Max Pro ZB602KL(6G/64G)\n\n\n網路價 $8,990\n\n\n折價券\n\n\n\n\n'
```

### STEP 7：透過 .stripped_strings 處理文字
這一步請各位嘗試使用 **`.stripped_strings`** 執行
```python=+
soup.find(class_='item yui3-u srp-multi-image').stripped_strings
```

執行結果會出現：
```
<generator object stripped_strings at 0x114e8d620>
```
這代表結果有多個物件在裡面，老師介紹 2 個方法處理這種狀況：
#### 方法 1
直接多個物件放入 List 中
```python=+
list(soup.find(class_='item yui3-u srp-multi-image').stripped_strings)
```

執行結果：
```
['ASUS ZenFone Max Pro ZB602KL(6G/64G)', '網路價', '$8,990', '折價券']
```

#### 方法 2
透過 for 迴圈一個個讀取並印出來，底下範例用字母 a 作為變數，讀取每個值並印出： 
```python=+
for a in soup.find(class_='item yui3-u srp-multi-image').stripped_strings:
    print(a)
```

執行結果：
```
ASUS ZenFone Max Pro ZB602KL(6G/64G)
網路價
$8,990
折價券
```

### STEP 8：使用 .find_all() 找出所有需要的資料
剛剛我們學會了找第一個 tag，而我們的目標是所有的商品標題和價格，因此這一步教大家使用 **`.find_all()`**
```python=+
soup.find_all(class_='item yui3-u srp-multi-image')
```
執行結果會發現和剛剛不同的是用 List 包住所有找到的結果：
```
[<div class="item yui3-u srp-multi-image" data-cluster="智慧型手機" data-ga-label="7415506" data-level="4_430_6859_109590" data-mlrscore="" data-p="1" data-pid="7415506" data-ppos="1" data-score="0.0">
 <div class="wrap">
 <div class="srp-carousel">
 <div class="carousel">
 <div class="carousel-list yui3-g">
 <div class="srp-pdimage cf content yui3-u">
 <a data-slk="image" data-ylk="sec:item;pid:7415506;itemid:7415506;slk:image" href="https://tw.buy.yahoo.com/gdsale/ASUS-ZenFone-4-Max-ZC554K-7415506.html" title="ASUS ZenFone 4 Max ZC554KL (3G/32G)智慧型手機">
...]
```

### STEP 9：.find_all() 搭配 for 迴圈和 .stripped_strings
使用 .find_all() 時，我們得到的結果已經是多個回傳值了，因此若我們直接使用 .stripped_strings 會發生錯誤，所以在這一步當中我們需要先透過 for 迴圈將資料一個個讀入，再透過 .stripped_strings 來做處理，底下範例透過 list() 包覆結果
```python=+
for asus in soup.find_all(class_='item yui3-u srp-multi-image'):
    print(list(asus.stripped_strings))
```
執行結果：
```
['ASUS ZenFone Max Pro ZB602KL(6G/64G)', '網路價', '$8,990', '折價券']
['ASUS ZenFone Max Pro (3G/32G) ZB602KL智慧手...', '網路價', '$6,990', '折價券']
['ASUS ZenFone Max Pro ZB602KL(3G/32G)智慧手機', '網路價', '$6,990', '折價券']
['ASUS ZenFone Max Pro ZB602KL(6G/64G)智慧手機', '網路價', '$8,990', '折價券']
['ASUS ZenFone Max Pro ZB602KL(6G/64G) 性能電...', '網路價', '$8,990', '折價券']
['ASUS ZenFone Max Pro ZB602KL(3G/32G) 性能電...', '網路價', '$6,990', '折價券']
['ASUS ZenFone Max Pro ZB602KL (3G/32G) 智慧...', '網路價', '$6,990', '折價券']
['ASUS ZenFone Max Pro ZB602KL (6G/64G) 智慧...', '網路價', '$8,990', '折價券']
['ASUS ZenFone Max M1 ZB555KL 2G/32G 5.5吋智...', '網路價', '$4,580', '折價券']
['補貨中', '補貨中', '補貨中', '補貨中', '(套餐組)ASUS ZenFone Max Plus (M1) 全螢幕電力怪獸手...', '網路價', '$5,990', '折價券']
['補貨中', '補貨中', '補貨中', 'ASUS ZenFone Max Plus (M1)\xa0ZB570TL全...', '網路價', '$6,990', '折價券']
```
做到這邊，我們已經順利的得到了商品標題和售價，但仍然不完美！因為包含了不應該存在的~~補貨中~~以及可以算是雜訊的~~網路價~~和~~折價券~~，這些都不是我們要放入資料庫的資訊，因此我們要做到最好就要設法把它拿掉！

### STEP 10：去除雜訊
#### STEP 10.1：遇到補貨中的資料整串拿掉
在這一小步請大家遇到補貨中的資料就整串拿掉，因為沒貨的資料存入資料庫中也只是垃圾資訊，做法使用上一堂課教過得 **`if`** 來判斷
```python=
for asus in soup.find_all(class_='item yui3-u srp-multi-image'):
    values = list(asus.stripped_strings)
    if '補貨中' not in values:
        print(values)
```
執行結果：
```
['ASUS ZenFone Max Pro ZB602KL(6G/64G)', '網路價', '$8,990', '折價券']
['ASUS ZenFone Max Pro (3G/32G) ZB602KL智慧手...', '網路價', '$6,990', '折價券']
['ASUS ZenFone Max Pro ZB602KL(3G/32G)智慧手機', '網路價', '$6,990', '折價券']
['ASUS ZenFone Max Pro ZB602KL(6G/64G)智慧手機', '網路價', '$8,990', '折價券']
['ASUS ZenFone Max Pro ZB602KL(6G/64G) 性能電...', '網路價', '$8,990', '折價券']
['ASUS ZenFone Max Pro ZB602KL(3G/32G) 性能電...', '網路價', '$6,990', '折價券']
['ASUS ZenFone Max Pro ZB602KL (3G/32G) 智慧...', '網路價', '$6,990', '折價券']
['ASUS ZenFone Max Pro ZB602KL (6G/64G) 智慧...', '網路價', '$8,990', '折價券']
['ASUS ZenFone Max M1 ZB555KL 2G/32G 5.5吋智...', '網路價', '$4,580', '折價券']
```
透過 if 判斷後可以看到~~補貨中~~的資料順利的拿掉了，再來是每個 List 中的網路假和折價券要拿掉，在繼續往下看之前，老師希望各位先自己試著做，做完在繼續看老師的寫法，這樣才有進步的機會 :muscle:

#### STEP 10.2：拿掉 List 中的雜訊
在這一步中，老師運用了 [Python 網路爬蟲課程 1](/O62YpbrzR-KwQxiVhb3CQA) 教過得 **.pop()** 來處理存在於 List 中不要的雜訊
```python=
for asus in soup.find_all(class_='item yui3-u srp-multi-image'):
    values = list(asus.stripped_strings)
    if '補貨中' not in values:
        values.pop(1) # 網路價都存於 List 中的第二個位置，因此透過上堂課教過得 pop 將它拿掉
        values.pop(-1) # 折價券都存於 List 中的最後一個位置，因此透過上堂課教過得 pop 將它拿掉
        print(values)
```
執行結果：
```
['ASUS ZenFone Max Pro ZB602KL(6G/64G)', '$8,990']
['ASUS ZenFone Max Pro (3G/32G) ZB602KL智慧手...', '$6,990']
['ASUS ZenFone Max Pro ZB602KL(3G/32G)智慧手機', '$6,990']
['ASUS ZenFone Max Pro ZB602KL(6G/64G)智慧手機', '$8,990']
['ASUS ZenFone Max Pro ZB602KL(6G/64G) 性能電...', '$8,990']
['ASUS ZenFone Max Pro ZB602KL(3G/32G) 性能電...', '$6,990']
['ASUS ZenFone Max Pro ZB602KL (3G/32G) 智慧...', '$6,990']
['ASUS ZenFone Max Pro ZB602KL (6G/64G) 智慧...', '$8,990']
['ASUS ZenFone Max M1 ZB555KL 2G/32G 5.5吋智...', '$4,580']
```

做到這邊，我們已經完成了 [Yahoo 購物中心的 ASUS 手機頁](https://tw.buy.yahoo.com/?catitemid=109590)的爬取，接下來，這些蒐集到的資料我們要把它存到 SQLite 資料庫中

> 後續課程會使用到的 SQLite 請各位先安裝 [DB Browser for SQLite](http://sqlitebrowser.org)
> 如果需要了解一些簡單的介紹 :point_right: [SQLite 基本介紹及安裝](/7U3s9VX0ROO_jxls7T-PWg)
> 各位同學可以先去泡杯咖啡休息一會再回來後續的課程:coffee:

## 爬取資料至 SQLite
要透過 Python 操作 SQLite，需要先 import SQLite 的套件，接著指定資料庫放在電腦中的位置
```python=
import sqlite3

conn = sqlite3.connect('~/asus.db') # ~ 為資料庫存放路徑
c = conn.cursor()
```

完成上述步驟後，將先前寫好的 for 迴圈處理流程拿回來修改
```python=+
for asus in soup.find_all(class_='item yui3-u srp-multi-image'):
    values = list(asus.stripped_strings)
    if '補貨中' not in values:
        values.pop(1) # 網路價都存於 List 中的第二個位置，因此透過上堂課教過得 pop 將它拿掉
        values.pop(-1) # 折價券都存於 List 中的最後一個位置，因此透過上堂課教過得 pop 將它拿掉
        c.execute('insert into asus(title, price) values(?,?)', values) #insert into 後面放資料表的名稱，資料表後的括號放要添加資料的欄位名稱
        conn.commit() #記得加這行，否則資料進不去資料庫
        print(values) #印出結果，不加這行印出結果也行
```

範例程式最後有 print 出執行結果：
```
['ASUS ZenFone Max Pro ZB602KL(6G/64G)', '$8,990']
['ASUS ZenFone Max Pro (3G/32G) ZB602KL智慧手...', '$6,990']
['ASUS ZenFone Max Pro ZB602KL(3G/32G)智慧手機', '$6,990']
['ASUS ZenFone Max Pro ZB602KL(6G/64G)智慧手機', '$8,990']
['ASUS ZenFone Max Pro ZB602KL(6G/64G) 性能電...', '$8,990']
['ASUS ZenFone Max Pro ZB602KL(3G/32G) 性能電...', '$6,990']
['ASUS ZenFone Max Pro ZB602KL (3G/32G) 智慧...', '$6,990']
['ASUS ZenFone Max Pro ZB602KL (6G/64G) 智慧...', '$8,990']
['ASUS ZenFone Max M1 ZB555KL 2G/32G 5.5吋智...', '$4,580']
```

最後，請同學透過 DB Browser for SQLite 觀看資料是否正確爬取，結果如圖：
![](https://i.imgur.com/JHV5PzN.png)

## 網頁爬蟲翻頁
來到課程的最後一小節啦 :sparkles:
這一節中會教大家處理網頁翻頁的方法，在爬取資料時，通常不會只要第一頁的資料，因此透過寫程式翻頁是相當重要的技巧，在這節課程中使用[飛比價格的 iPhone X 查詢結果](https://feebee.com.tw/product/iPhone%20X%20256G%20%E6%99%BA%E6%85%A7%E5%9E%8B%E6%89%8B%E6%A9%9F/?q=iphone%20x)作為範例
![](https://i.imgur.com/c8EIL1N.png)

### 爬取範圍
這邊老師僅要求各位同學爬取頁面中的價格，並且印出，直到印出最後一頁的所有價格後停止程式
![](https://i.imgur.com/ONbNDOv.png)

### 網頁觀察
#### STEP 1：找到網頁中的頁碼
進入[飛比價格的 iPhone X 查詢結果](https://feebee.com.tw/product/iPhone%20X%20256G%20%E6%99%BA%E6%85%A7%E5%9E%8B%E6%89%8B%E6%A9%9F/?q=iphone%20x)，拉到頁面最底部會找到頁碼資訊
![](https://i.imgur.com/E7gQ6a9.png)

#### STEP 2：點擊第 2 頁，接著觀察網址變化
這時候，會發現網址的最後面多了 **&page=2**，頁面再拉回底部選取第一頁，仍會發現網址最後面帶有 **&page=1**
![](https://i.imgur.com/I7ux2kc.png)

**做到這邊，我們已經確定了網頁規則，開始撰寫程式**

### 撰寫程式
#### STEP 1：引入爬蟲需要的函式庫
```python=
import requests
from bs4 import BeautifulSoup
```

#### STEP 2：設定 URL 和頁碼
> :exclamation:注意：URL 末端使用 {} 
```python=+
url = 'https://feebee.com.tw/product/iPhone%20X%20256G%20%E6%99%BA%E6%85%A7%E5%9E%8B%E6%89%8B%E6%A9%9F/?q=iphone%20x&page={}'
page = 1
```

#### STEP 3：透過 while 迴圈每執行完一輪 page + 1
當字串中含有 {} 時，代表後續可以填入，因此程式碼中透過 **`.format()`** 將定義為 1 的變數 **page** 帶入，接著透過 for 迴圈讀取網頁中的價格，並一個個印出正在第幾頁的價格，執行完後 page + 1，變成在第 2 頁，執行上述步驟，直到翻到最後一頁，找不到網頁原始碼中含有 class = 'price ellipsis' 的資訊，用 break 停止整個 while 迴圈
```python=+
while True:
    res = requests.get(url.format(page))
    soup = BeautifulSoup(res.text, 'html.parser')

    for iPhone_price in soup.find_all(class_ = 'price ellipsis'):
        print('第' + str(page) + '頁:'+ iPhone_price.text)
    if soup.find(class_ = 'price ellipsis') is None:
        break
    page += 1
```

執行結果：
```
第1頁:29,900
第1頁:30,000
第1頁:30,900
第1頁:31,900
第1頁:32,490
第1頁:32,700
第1頁:32,700
第1頁:32,700
第1頁:32,999
第1頁:32,999
第1頁:33,000
第1頁:33,490
第1頁:33,500
第1頁:33,500
第1頁:33,500
第1頁:34,500
第1頁:34,500
第1頁:34,500
第1頁:34,500
第1頁:34,500
第2頁:34,500
...
```

## 課後練習
恭喜各位完成了 [Python 網路爬蟲課程 2](/8ZVF56fBQ-ydJC5Sj0Gubg)，課程最後老師想請各位實際練習
題目中會用到課堂中沒上過得內容，請善用 [Google](https://www.google.com/)
:::warning
題目：請爬取[飛比價格的 iPhone X 查詢結果](https://feebee.com.tw/product/iPhone%20X%20256G%20%E6%99%BA%E6%85%A7%E5%9E%8B%E6%89%8B%E6%A9%9F/?q=iphone%20x)所有價格，並計算其均價
>

> 提示：
> 1. 建立一個 List 儲存所有價格
> 2. 處理數字中的逗號 #.replace(',', '')
> 3. 將文字轉為數字 #int(12345)
> 4. 加總 #sum()
> 5. 計算長度 #len()

請各位先不要看解答，實際想過寫過才有辦法進步 :muscle:
解法在下堂課教各位 :point_right: [Python 網路爬蟲課程 3](/TX7GQ1GKTa-O1VSAe-w2YQ)
:::
___

:::success
第二堂課結束囉:100:
這堂課所教的爬蟲技巧是非常基礎的喔 :running:
請各位將本堂課程熟悉到後面的課程才不會跟不上喔 :point_up: 
:::

###### tags: `Python` `Python 網路爬蟲課程` `Crawler` `網路爬蟲` `SQLite`
# Python 網路爬蟲課程 1
:::warning
:warning: 注意事項 :warning:
* 課程內容以 Python 爬蟲為主軸，Python 基礎不會著墨過深，基礎的部份遇到困難請同學善用 [Google](https://www.google.com/)
* 課程內容是本人的嘔心瀝血之作，若有引用請標明出處
* 本文最後編輯日期：2018/08/07
:::

## 課堂使用環境安裝 :computer:
* 本課程使用 [Anaconda](https://www.anaconda.com/download/) 做為教學環境
* 請下載對應電腦作業系統的 Python 3.6 版本
* 詳細安裝流程 :point_right: [Python Anaconda 環境安裝教學](/h5XtZtlRSB2TQP-marFL5g)

## Jupyter Notebook 使用教學
本課程使用 Jupyter Notebook 作為課程所用
詳細的操作方法 :point_right: [Python Jupyter Notebook 使用教學](/PX-Qm3F-SA61cKXOP0TiBA)

## Python 基礎
### 資料型態

#### 字串 (String)
* 使用單引號或雙引號包覆文字
```python=
'this is string'
"this is string"
```
> :exclamation:注意：
> 若使用單引號 ('')，字串內不可又放入一個單引號，否則程式會出錯
```python=
'it's string' #執行會出現錯誤訊息
```
> 若要加入單引號在單引號包覆的字串中，撰寫方式如下：
```python=
'it\'s string'
```
> 或直接使用雙引號包覆字串：
```python=
"it's string"
```

#### 整數 (Integer) ＆ 浮點數 (Floating-point number)
* 沒有小數點的數字為整數
* 有小數點的是浮點數
```
1 #整數 (int)
1.0 #浮點數 (float)
```

#### 變數
在撰寫程式時，經常需要設定變數重複運用，此時就會透過此方式達成
以爬蟲程式為例，網頁翻頁時經常在網址中出現 page=(?)，透過更改數值可以達到翻頁的目的，因此在撰寫程式時可以先預設好變數 page 在第 1 頁，後續再透過運算式將 page + 1
```python=
page = 1
```

#### 串列 (List)
* List 是 Python 中最基本可以存放多筆資料的資料型態
* List 中不一定只能放置相同類型的資料 #如下 mix_list
```python=
num_list = [1,2,3]
str_list = ['字串1', '字串2', '字串3']
mix_list = [1,2,3,'字串1','字串2','字串3']
```

##### List 位置
在寫程式運用 List 時，我們經常會需要從 List 中取出資料，因此要取出 List 中某個位置的資料，能夠透過下列方法指定資料位置
* 在 Python 的 List 第 1 個位置是由 0 開始指定，以此類推
* 若要由後向前拿取，則是由 -1 開始指定
```python=
num_list = [1 , 2 , 3 , 4 , 5]
            0   1   2   3   4
           -5  -4  -3  -2  -1
```
從上述範例，若要取出 num_list 中的 2，可透過下列兩個方式：
```python=
num_list[1]
num_list[-4]
```

##### List 加入值
我們經常會需要加入新的元素到 List 中，此時我們會使用 .append()，承上 num_list 範例，若要將數字 6 加入 num_list，方法為：
```python=
num_list.append(6) #[1,2,3,4,5,6]
```

##### List 刪除值
現在 num_list 有數字 1~6 在其中，要刪除剛剛加入的數字 6 可以用運 .pop()，在括號中填入 6 的所在位置，因此有兩種方式達成此目的：
```python=
num_list.pop(5) #[1, 2, 3, 4, 5]
num_list.pop(-1) #[1, 2, 3, 4, 5]
```
承上，num_list 中僅剩數字 1~5，要再刪除 num_list 中的數字 2，方法為：
```python=
num_list.pop(1) #[1, 3, 4, 5]
num_list.pop(-4) #[1, 3, 4, 5]
```
> 本課程會使用到的基本資料型態到這邊告個段落:clap:
> 各位同學可以先去泡杯咖啡休息一會再回來後續的課程:coffee:

### 運算式及陳述
#### if, elif, else
不論在何種程式語言中，都會需要判斷的功能，在 Python 中判斷是透過 if, elif, else 組合達到目的，下圖簡單的描述了其用法
![](https://i.imgur.com/oczlOwh.png)

> 在這邊，我想請各位同學試著實際練習，並思考為何程式是產生這樣的結果
```python=
name = 'Fish'

if name == 'John':
    print('Hi, John')
elif name == 'Fish':
    print('Hi, Fish')
else:
    print('Who are you?')
```

執行結果：
```
Hi, Fish
```

在剛剛的練習範例中，我們先定義了變數 name 為 Fish，接著進入第一個 if 判斷式，若第一個判斷不符合時，會進入 elif 判斷，範例中在 elif 時符合 name 為 Fish，因此執行程式碼 print('Hi, Fish')
> :exclamation:注意：判斷式中可以沒有 elif 和 else，僅透過 if 判斷是否

#### For 迴圈 (for loop)
目的：讓程式重複執行數次:arrows_clockwise:
底下範例建立一個 List 名為 list1，list1 中存有數字 1~10，接著運用 for 迴圈將 list1 中的值一個個印出
```python=
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in list1:
    print(num)
```

執行結果：
```
1
2
3
4
5
6
7
8
9
10
```

#### While 迴圈 (while loop)
目的：讓程式無限次重複執行:arrows_clockwise:
底下範例定義變數 x = 0，透過 while 迴圈將 x + 1 並印出，直到印出 x 的值為 10 停止
```python=
x = 0

while x < 10:
    x += 1
    print(x)
```

執行結果：
```
1
2
3
4
5
6
7
8
9
10
```

##### while 搭配 else
承上範例，如果想要印到 10 之後，由程式告訴我們完成了，可以加入 else，讓程式執行完 while 迴圈後印出 Done
```python=
x = 0

while x < 10:
    x += 1
    print(x)
else:
    print('Done')
```

執行結果：
```
1
2
3
4
5
6
7
8
9
10
Done
```

#### break, continue, pass
* break：停止迴圈
* continue：持續執行迴圈
* pass：略過這一迴圈

在下列範例中仍然讓 x 在 while 迴圈中跑到 10，但其中下了 if x == 3 停止迴圈，else 的部份則是印出 running...，因此可以看到此範例的持行會先印出 2 次 running...，接著印出 3，然後程式就停止了
主因在於 if 判斷式中的 break 中止了整個迴圈，使大於 3 之後的值不會跑到

> :exclamation:注意：
> else 內的 pass 是為了讓同學和後續的範例做比對，此範例中沒寫 pass 仍能跑出相同結果
```python=
x = 0

while x < 10:
    x += 1
    if x == 3:
        print(x)
        break
    else:
        pass
        print('running...')
```

執行結果：
```
running...
running...
3
```

若將 else 中的 pass 改為 continue，則會產生不同的結果
```python=
x = 0

while x < 10:
    x += 1
    if x == 3:
        print(x)
        break
    else:
        continue
        print('running...')
```

執行結果：
```
3
```

各位會發現到，else 中的 running... 不會再被印出，其原因為 continue 的用意是讓迴圈繼續執行，因此程式又回到了 x += 1 迴圈中的第一個動作，print('running...') 在此程式中則沒有機會被執行！

#### 無窮迴圈
* 指迴圈中沒有停止的條件，程式會不斷的執行
* 請謹慎小心的使用
```python=
while True:
    print('無窮迴圈')
```

執行結果：
```
無窮迴圈
無窮迴圈
.
.
.
(...意指不斷印出字串 '無窮迴圈')
```

> 若電腦效能不夠好，極有可能跑到電腦當機，請務必記得在迴圈中給予停止條件
> 若真的不慎寫出了無窮迴圈，請以手動的方式將迴圈中止
 
### 例外處理
寫程式時有時候會遇到例外的狀況，這時我們就會使用 try...except 來處理這樣的狀況，看底下範例：
```python=
try:
    print(a)
except:
    print('a is not defined')
```

執行結果：
```
a is not defined
```

程式中，我們沒有定義 a 這個變數，因此若直接執行 print(a) 一定會出現錯誤訊息。因此用 try 若發生了錯誤，就會執行 except 中所寫的程式碼，因此範例中執行了印出 a is not defined
___

:::success
第一堂課結束囉:100:
[Python 網路爬蟲課程 2](/8ZVF56fBQ-ydJC5Sj0Gubg) 將開始帶簡單的網頁爬蟲
進入前請先將本堂課的內容弄熟悉喔！
:::

###### tags: `Python` `Python 網路爬蟲課程` `Crawler` `網路爬蟲` `SQLite`
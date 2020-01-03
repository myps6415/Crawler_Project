# pcstore_crawler_selenium

* 主程式：chrome_selenium.py
* 爬蟲程式：/chrome_driver/chrome_driver.py
* 必要程式：/chrome_driver/chromedriver (http://chromedriver.chromium.org)
* 執行的電腦必須安裝 [Google Chrome](https://www.google.com/intl/zh-TW_ALL/chrome/)

## 目的:
在 [PChome商店街](https://www.pcstore.com.tw) 爬取輸入字串的第一頁標題

## 流程說明：
由於 **PChome商店街** 查詢的字串會特殊處理過，無法直接用於網址串，因此較簡單的方法為透過模擬人類操作瀏覽器的方式，因此採用 selenium 套件

* 主程式搜集使用者鍵入的字詞，以及最後的第一頁標題處理
* 爬蟲程式將使用者鍵入的字詞輸入至搜尋欄位，並送出查詢，最後取得查詢後頁面的網頁原始碼，將原始碼回給主程式做最後的處理

###### tags: `Python` `Python 網路爬蟲`

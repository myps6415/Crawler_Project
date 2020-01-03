import requests
from bs4 import BeautifulSoup
import time
import csv
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium import webdriver

url = 'https://www.mobile01.com/googlesearch.php?q='
keyword = 'IH電子鍋'
items = list() #爬到的所有網址
information = list() #頁面資訊
i = 2 #蒐集 URL 用，不用改
x = 0 #getMobile01 用
y = 1
howMany = list()

driver = webdriver.Chrome('/Users/fish/Documents/workspace/Crawler/chromedriver')
driver.get(url+keyword)
time.sleep(5)

def Url():
    soup = BeautifulSoup(driver.page_source, 'html.parser')     
    for div in soup.find_all('div','gsc-webResult gsc-result'):
        items.append(div.find('a','gs-title')['href'])
    
def nextPage():
    print(i)
    next_page = driver.find_element_by_xpath('//*[@id="___gcse_1"]/div/div/div/div[5]/div[2]/div/div/div[2]/div[11]/div/div[' + repr(i) +']')
    next_page.click()
    
def getMobile01():
    url = items[x]
    time.sleep(3)
#     url = 'http://www.mobile01.com/sitetransfer.htm?url=https%3A%2F%2Fwww.mobile01.com%2Ftopicdetail.php%3Ff%3D602%26t%3D4911218%26p%3D2'
    
    try:
        resp = requests.get(url +'&p=' + repr(y))
        time.sleep(3)
        print(url +'&p=' + repr(y))
        soup = BeautifulSoup(resp.text, 'html.parser')
        
        title = soup.find('h1','topic').text #標題  
        for div in soup.find_all('div', 'single-post'):
            item = list()
            item.append(div.find('div', 'fn').text) #作者
            item.append(title) #標題
            item.append(url +'&p=' + repr(y)) #網址
            item.append(div.find('div', 'date').text) #日期
            item.append(div.find('div', 'single-post-content').text) #內文
            information.append(item)
    except Exception as e:
        resp = requests.get(url)
        time.sleep(3)
        print(url)
        soup = BeautifulSoup(resp.text, 'html.parser')
        
        title = soup.find('h1','topic').text
        getdate = soup.find_all('p', 'nav')[3].text
        content = soup.find('div', 'single-post-content').text
        
        dateget = getdate.split(' ')
        date = dateget[1] + ' ' + dateget[2]
        
        item = list()
        item.append('Mobile01新聞') #作者
        item.append(title)
        item.append(url)
        item.append(date)
        item.append(content)
        information.append(item)

def getMobile01Page():
    print(items[x])
    driver.get(items[x])
#     url = 'http://www.mobile01.com/sitetransfer.htm?url=https%3A%2F%2Fwww.mobile01.com%2Ftopicdetail.php%3Ff%3D602%26t%3D4911218%26p%3D2'
    time.sleep(3)
    
    if '/sitetransfer' in items[x]:
        try:
            PreviousPage = driver.find_element_by_xpath('//*[@id="section"]/div[1]/div[2]/a[2]')
            PreviousPage.click()
            time.sleep(3)
            trueURL = driver.current_url
            URL = trueURL.split('&p')
            print(URL[0])
            items[x] = URL[0]
        except Exception as e:
            howMany.append('None')
    
    try:
        hoMany = driver.find_element_by_xpath('//*[@id="section"]/div[1]/div[2]/a[6]').text
        howMany.append(hoMany)
        print(hoMany)
        time.sleep(3)  
    except Exception as e:
        try:
            howManyP = driver.find_element_by_xpath('//*[@id="section"]/div[1]/div[2]').text
            print(howManyP)
            if howManyP == '':
                howMany.append('1')
            else:
                test = howManyP.split(' …') #第一次切割, 將…分開
                testagain = test[0].split(' ') #第二次切割, 將頁碼分開
                hoMany = testagain[-1] #取出最後一頁
                print(hoMany)
                howMany.append(hoMany)
                if howMany[0] == '上一頁':
                    PreviousPage = driver.find_element_by_xpath('//*[@id="section"]/div[1]/div[2]/a[2]')
                    PreviousPage.click()
                    howMany.clear()
                    try:
                        hoMany = driver.find_element_by_xpath('//*[@id="section"]/div[1]/div[2]/a[6]').text
                        howMany.append(hoMany)
                    except Exception as e:
                        howManyP = driver.find_element_by_xpath('//*[@id="section"]/div[1]/div[2]').text
                        print(howManyP)
                        if howManyP == '':
                            howMany.append('1')
                        else:
                            test = howManyP.split(' …') #第一次切割, 將…分開
                            testagain = test[0].split(' ') #第二次切割, 將頁碼分開
                            hoMany = testagain[-1] #取出最後一頁
                            print(hoMany)
                            howMany.append(hoMany)
                elif howMany[0] == '檢視完整景點資訊':
                    howMany.clear()
                    howMany.append('None')
                    
                time.sleep(3)
        except Exception as e:
            try:
                howManyP = driver.find_element_by_xpath('//*[@id="section"]/div[1]/p[4]').text
                howMany.append('1')
            except Exception as e:
                howMany.append('None')    
                
def urlCSV():
    with open('URL.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow('URL',)
        for item in items:
                print(item)
                writer.writerow((column for column in item))           
        
def writeCSV():
    with open(str(x) +'.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(('作者', '標題', '網址', '日期', '內文'))
        for item in information:
                writer.writerow((column for column in item))
        print(information)

def first():
    while True:
        Url()
        nextPage()
        global i
        i += 1
        time.sleep(3)
        if(i == 11):
            Url()
            print(items)
#             urlCSV()
            break
        

def second():        
    getMobile01Page()
    while True:
        if(howMany[0] == 'None'):
            global x
            x += 1
            information.clear()
            howMany.clear()
            break
        getMobile01()
        time.sleep(3)
        print(howMany)
        print(information)
        global y
        y += 1
        if (y == int(howMany[0])):
            getMobile01()
            print(information)
            writeCSV()
            information.clear()
            howMany.clear()
            x += 1
            y = 1
            break
        elif(int(howMany[0]) == 1):
            getMobile01()
            print(information)
            writeCSV()
            information.clear()
            howMany.clear()
            x += 1
            y = 1
            break
        
first()
while True:
    second()
    if(x == 99):
        second()
        driver.close()
        break


# 特殊情況用
# getMobile01Page()
# while True:
#     getMobile01()
#     y += 1
#     if (y == int(howMany[0])):
#         getMobile01()
#         print(information)
#         writeCSV()
#         break

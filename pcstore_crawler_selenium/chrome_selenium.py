from bs4 import BeautifulSoup
from chrome_driver import chrome_driver

if __name__ == '__main__':
    url = 'https://www.pcstore.com.tw'
    keyword = input('請輸入欲查詢商品關鍵字：')

    to_soup = chrome_driver.crawler(url, keyword).pcstore_crawler()
    soup = BeautifulSoup(to_soup, 'html.parser')

    for i in soup.find_all(class_ = 'pic2t pic2t_bg'):
        print(i.text)
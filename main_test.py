import sys #for user input
from selenium import webdriver #Dealing with browser commands
from bs4 import BeautifulSoup as bs #Html/xml parser
import pandas as pd #To create csvs

def main():

    #base_url1 = 'https://www.weblio.jp/content/'
    #base_url = 'https://tangorin.com/sentences?search='
    base_url = 'https://jisho.org/search/'
    url_suffix = '%20%23sentences'

    driver = webdriver.Chrome("C:/Users/vicke/Documents/Python Scripts/Kanjiscraper/chromedriver_win32/chromedriver")
    f= open("results.txt","w+", encoding = 'utf-8')

    search_term = '感じ'
    url = base_url + search_term + url_suffix
    driver.get(url)
    content = driver.page_source
    soup = bs(content)

    main_results = soup.find('div', id='main_results')
    sentence = main_results.find('div', {'class':'sentence_content'})
    japanese = sentence.find('ul', {'class':'japanese_sentence japanese japanese_gothic clearfix'})
    #TODO: Separate japanese into kanji and furigana
    english = sentence.find('span', {'class':'english'}).text
    print(japanese)
    print(english)


    f.write(search_term + '\n')
    f.write(japanese + '\n')
    f.write(english + '\n')
    f.close()

if __name__ == '__main__':
    main()

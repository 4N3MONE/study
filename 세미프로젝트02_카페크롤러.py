from bs4 import BeautifulSoup 
from selenium import webdriver
import datetime
import time
import sys
import pyperclip
from selenium.webdriver.common.keys import Keys
import pyautogui
import math
import pandas as pd
searchdate = input("""
시점을 선택해주세요. 
1 : 코로나 이전(2020년 1월 31일 이전)
2 : 코로나 이후(2020년 1월 31일 이후)
""")
query = input("검색할 단어(국내야간관광/국내관광)를 입력하세요 : ")
searchcnt = int(input("몇 건을 검색하시겠습니까?: "))
page_cnt = math.ceil(searchcnt/10)
now = datetime.datetime.now()
nowdate = now.strftime('%Y-%m-%d') 

if searchdate == "1" :
  coronafilename = "코로나이전"
  startdate1 = "20190101"
  enddate1 = "20200101"
if searchdate == "2" :
  coronafilename = "코로나이후"
  startdate1 = "2020101"
  enddate1 = nowdate
path1 = "C:\\tmp\\크롤링\\"

  #오늘 날짜 구하기, 코로나 시점 정하기

coronastart = "2020-01-31"
path = "C:\\tmp\\크롤링\\"
filename = path+query+"_"+"카페"+"_"+nowdate+"_"+coronafilename+".csv"

#네이버 카페 검색 접속
path = "c:/tmp/chromedriver.exe"
driver = webdriver.Chrome(path)

news = []
dict1 = []
cafe_list = []

for page in range(page_cnt) :
  url = 'https://search.naver.com/search.naver?where=articleg&query={}&ie=utf8&st=rel&date_option=6&date_from={}&date_to={}&board=&srchby=text&dup_remove=1&cafe_url=&without_cafe_url=&sm=tab_opt&nso=so%3Ar%2Cp%3Afrom{}to{},a:all&start={}1' .format (query, startdate1, enddate1, startdate1, enddate1, page)
  target_info = {}
  path = "c:/tmp/chromedriver.exe"
  driver = webdriver.Chrome(path)
  driver.get(url)
  time.sleep(2)
  html = driver.page_source
  soup = BeautifulSoup(html, 'html.parser')
  contents_lists = soup.select('dd.sh_cafe_passage')
  for content in contents_lists:
    cafe_list.append(content.text)
  driver.close()

content_str = ' '.join(cafe_list)
target_info['content'] = content_str
dict1.append(target_info)        
        
df = pd.DataFrame(dict1)  #df로 변환
        
    
    
    # 새로 만들 파일이름 지정
filename = path1+query+"_"+"카페"+"_"+nowdate+"_"+coronafilename+".csv" 
df.to_csv(filename,encoding="utf-8-sig" , index=False)
print("="*80)
print("{}에 크롤링 결과가 저장되었습니다.".format(filename))

from bs4 import BeautifulSoup
from datetime import datetime
from selenium import webdriver
import requests
import pandas as pd
import re
import math,time,sys
from selenium.webdriver.common.keys import Keys


#각 크롤링 결과 저장하기 위한 리스트 선언 
title_text=[]
link_text=[]
source_text=[]
date_text=[]
contents_text=[]
result={}
now = datetime.now()
nowdate = now.strftime('%Y%m%d') 

#엑셀로 저장하기 위한 변수
RESULT_PATH ='C:/tmp/크롤링/'  #결과 저장할 경로
now = datetime.now() #파일이름 현 시간으로 저장하기


searchdate = input("""
시점을 선택해주세요. 
1 : 코로나 이전(2020년 1월 31일 이전)
2 : 코로나 이후(2020년 1월 31일 이후)
""")
query = input("검색할 단어(국내야간관광/국내관광)를 입력하세요 : ")
searchcnt = int(input("몇 건을 검색하시겠습니까?(10단위) : "))
page_cnt = math.ceil(searchcnt/10)
coronastart = "20200131"

if searchdate == "1" :
  coronafilename = "코로나이전"
  startdate = "2019.01.01"
  startdate1 = "20190101"
  enddate = "2020.01.01"
  enddate1 = "20200101"
if searchdate == "2" :
  coronafilename = "코로나이후"
  startdate = "2020.01.01"
  enddate = now.strftime('%Y.%m.%d')
  startdate1 = "2020101"
  enddate1 = nowdate
path1 = "C:\\tmp\\크롤링\\"

# def main():
#     info_main = input("="*50+"\n"+"입력 형식에 맞게 입력해주세요."+"\n"+" 시작하시려면 Enter를 눌러주세요."+"\n"+"="*50)
    
#     maxpage = input("최대 크롤링할 페이지 수 입력하시오: ")  
#     query = input("검색어 입력: ")  
#     sort = input("뉴스 검색 방식 입력(관련도순=0  최신순=1  오래된순=2): ")    #관련도순=0  최신순=1  오래된순=2
#     s_date = input("시작날짜 입력(2019.01.04):")  #2019.01.04
#     e_date = input("끝날짜 입력(2019.01.05):")   #2019.01.05
    
#     crawler(maxpage,query,sort,s_date,e_date) 
    
# main()


# def crawler(maxpage,query,sort,s_date,e_date):

   
news = []
dict1 = []
news_list = []

for page in range(page_cnt) :
    url = 'https://search.naver.com/search.naver?&where=news&query={}&sm=tab_pge&sort=1&photo=0&field=0&reporter_article=&pd=3&ds={}&de={}&docid=&nso=so:dd,p:{}to{},a:all&mynews=0&start={}1&refresh_start=0'.format(query,startdate,enddate,startdate1,enddate1,page)
    target_info = {}
    path = "c:/tmp/chromedriver.exe"
    driver = webdriver.Chrome(path)
    driver.get(url)
    time.sleep(2)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    contents_lists = soup.select('ul.type01 dl')

    
    for content in contents_lists:
        news_list.append(content.text.split('보내기')[1])

    driver.close()

    #if (page+1)%10 ==0 :
        #driver.find_element_by_xpath('//*[@id="main_pack"]/div/div[2]/a[10]').click()
        
content_str = ' '.join(news_list)
target_info['content'] = content_str
dict1.append(target_info)        
        
df = pd.DataFrame(dict1)  #df로 변환
        
    
    
    # 새로 만들 파일이름 지정
filename = path1+query+"_"+"뉴스"+"_"+nowdate+"_"+coronafilename+".csv" 
df.to_csv(filename,encoding="utf-8-sig" , index=False)
print("="*80)
print("{}에 크롤링 결과가 저장되었습니다.".format(filename))
    
    
    
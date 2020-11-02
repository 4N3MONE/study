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
1 : 코로나 이전(2020년 1월 1일 이전)
2 : 코로나 이후(2020년 1월 1일 이후)
""")
query = input("검색할 단어(국내야간관광/국내관광)를 입력하세요 : ")
searchcnt = int(input("몇 건을 검색하시겠습니까?: "))

now = datetime.datetime.now()
nowdate = now.strftime('%Y-%m-%d') 
coronastart = "2020-01-01"

if searchdate == "1" :
  coronafilename = "코로나이전"
  startdate = "2019-01-01"
  startdate1 = "20190101"
  enddate = "2020-01-01"
  enddate1 = "20200101"
if searchdate == "2" :
  coronafilename = "코로나이후"
  startdate = "2020-01-01"
  enddate = now.strftime('%Y-%m-%d')
  startdate1 = "2020101"
  enddate1 = nowdate
# searchdate = "1"
# query = "파이썬"
# searchcnt = 11
page_cnt = math.ceil(searchcnt/7)

#오늘 날짜 구하기, 코로나 시점 정하기

path = "C:\\tmp\\크롤링\\"
filename = path+query+"_"+"블로그"+"_"+nowdate+"_"+coronafilename+".csv"
def id_click(id_name):
    driver.find_element_by_id(id_name).click()
    time.sleep(1)

def text_paste(name):
    pyperclip.copy(name)
    webdriver.ActionChains(driver).\
      key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
    time.sleep(2)

#네이버 블로그 검색 접속
path = "c:\\tmp\\chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get("https://section.blog.naver.com/Search/Post.nhn?pageNo=1&rangeType=ALL&orderBy=sim&keyword={}" .format(query) )
time.sleep(2)
full_html = driver.page_source
soup = BeautifulSoup(full_html, 'html.parser')

#기간 입력하기
driver.find_element_by_xpath('//*[@id="content"]/section/div[1]/div[2]/div/div/a').click()
if searchdate == '1' :
  id_click('search_start_date')
  text_paste('2019-01-01')
  pyautogui.press('tab')
  text_paste(coronastart)
  pyautogui.press('tab')
  driver.find_element_by_xpath('//*[@id="periodSearch"]').click()

if searchdate == '2' :
  id_click('search_start_date')
  text_paste(coronastart)
  pyautogui.press('tab')
  text_paste(nowdate)
  pyautogui.press('tab')
  driver.find_element_by_xpath('//*[@id="periodSearch"]').click()
time.sleep(2)


#게시물 크롤링하기
no = 0
dict1 = []

for x in range(1,page_cnt+1) :
  full_html = driver.page_source
  soup = BeautifulSoup(full_html, 'html.parser')
  content_list = soup.find_all('div', class_="desc")
  url_list = []
  for content in content_list:
      url = content.find('a')['href']
      url_list.append(url)
  print(url_list)

  for i in range(len(url_list)) :
    target_info = {}
      
    url = "'"+url_list[i]+"'"
    driver.switch_to_window(driver.window_handles[0])
    driver.execute_script('window.open({});'.format(url))
    time.sleep(2)

    driver.switch_to_window(driver.window_handles[1])
    driver.switch_to.frame("mainFrame")
    html2 = driver.page_source
    soup2 = BeautifulSoup(html2, 'html.parser')
    # 내용 크롤링
    overlays = ".se-component.se-text.se-l-default"                                 
    contents = driver.find_elements_by_css_selector(overlays) # date

    content_list = []
    for content in contents:
        content_list.append(content.text)

    if content_list == []:
        time.sleep(3)
        driver.close()
        continue # 결과가 안 나올 경우 형식이 다르므로 깔끔히 버리고 다음 거로 간다

    content_str = ' '.join(content_list)

    # 글 하나는 target_info라는 딕셔너리에 담기게 되고,
    target_info['content'] = content_str
    
    # 각각의 글은 dict1이라는 딕셔너리에 담기게 됩니다.
    dict1.append(target_info)
    time.sleep(1)
        
    no += 1
    print('번호 : {}' .format(no))
    print('내용 : {}' .format(content_str))
    print('\n')
    time.sleep(3)
    driver.close()

    contents = None
    content_str = None
    # 데이터가 잔존하여 예상치 못한 결과가 일어나는 것을 방지하기 위한 초기화

    if no == searchcnt :
      break
  driver.switch_to_window(driver.window_handles[0])
  if x == page_cnt :
    break

  elif page_cnt/10 ==0 :
    driver.find_element_by_xpath('//*[@id="content"]/section/div[3]/a').click()
    time.sleep(2)

  else :
    driver.get("https://section.blog.naver.com/Search/Post.nhn?pageNo={}&rangeType=PERIOD&orderBy=sim&startDate={}&endDate={}&keyword={}" .format(x,startdate,enddate,query) )
    
    time.sleep(2)

result_df = pd.DataFrame(dict1)
result_df.to_csv(filename, encoding="utf-8-sig" , index=False)
# f = open(filename, 'a',encoding='UTF-8')
# f.write(str(dict1))
# f.close( )  #파일 닫기
print("="*80)
print("{}에 크롤링 결과가 저장되었습니다.".format(filename))
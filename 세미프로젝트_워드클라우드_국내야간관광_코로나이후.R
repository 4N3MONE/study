#워드클라우드의 색상 변경하기 기능 포함
#Step 1. 필요한 패키지 설치 및 실행
setwd("c:\\tmp") 
# install.packages("KoNLP") 
#install.packages("wordcloud") 
#install.packages("stringr")
install.packages("wordcloud2")

library(rJava)
library(KoNLP) 
library(wordcloud)
library(stringr)  
library(wordcloud2)

Sys.setenv(JAVA_HOME='C:\\Program Files\\Java\\jre1.8.0_261')
#Step 2. 사전 관련 작업
useNIADic() 
getwd()

setwd('C:\\tmp\\크롤링')
# csv <- read.table("국내야간관광_블로그_2020-10-16_코로나이전.csv", encoding="UTF-8", header = T, fill = T)
data1 <- readLines("국내야간관광_블로그_2020-10-16_코로나이후_텍스트.txt")
data1 <- gsub("//d+","",data1)
data1 <- gsub("[[:punct:]]", "", data1)
data1 <- gsub("^[가-힣]", "", data1)
data1 <- gsub("[A-Za-z]", "", data1)
data1 <- gsub("△", "", data1)
data1 <- gsub("▲", "", data1)
data1 <- gsub("▶", "", data1)
data1 <- gsub("^", "", data1)
data1 <- gsub("▼", "", data1)

data2 <- extractNoun(data1)
head(data2,5)
data3 <- unlist(data2)
head(data3)

data4 <- Filter(function(x) {nchar(x) <= 10 & nchar(x) >1}, data3)
length(data4)
head(data4)
wordcount <- table(data4)
head(sort(wordcount, decreasing=T),100)

sub1 <- c("\\d+","야간","관광", "여행", "선정", "공사", "국내", "시간", "한국관광", "지역", "관광객", "명소", "관광지", "다양", "추천", "운영", "문화", "산업","하나", 
          "이번", "한국", "전망", "거리", "산책", "매력", "활성화", "사진", "사업", "코스", "프로그램", "도시", "발표", "소개", "경제",
          "콘텐츠", "모습", "전국", "가능", "진행", "추진", "효과", "시작", "전문가", "세계", "하기", "방문", "사람", "유명", "생각", "대표", "때문", "위치", "경관",
          "https", "하면", "올해", "공간", "이곳", "ㅋ", "ㅎ", "야행", "최종", "예약", "신규", "예정", "이름", "준비", "홍보", "오늘", "판단", "특별", "연결", "정보", "핵심",
          "최초", "안녕", "아래", "강화", "이용", "제공", "지방자치단체", "naver", "com", "최대", "홈페이지", "텔레콤", "마케팅", "기업", "맛집", "지원", "상품", "서비스", "www",
          "들이", "있습니","^^")
i <- 1
cnt_txt <- length(sub1)
cnt_txt
for ( i in 1:cnt_txt) {data4 <- gsub((sub1[i]), "", data4)}

data5 <- Filter(function(x) {nchar(x)<= 10&nchar(x)>1}, data4)
wordcount2 <- table(data5) 
wordcount2 <- head(sort(wordcount2, decreasing=T),250)

palete <- brewer.pal(8,"Dark2")
wordcloud2(data = wordcount2, fontFamily = '나눔바른고딕', color = "random-dark", shape = "circle")


setwd('c:\\tmp')
write.csv(wordcount2, file = "wordcount2_코로나이후.csv")
wordcount3 <- read.csv('wordcount2_코로나이후.csv', header = T)
head(wordcount3,20)

library(data.table)
library(wordcloud2)
getwd()
setwd('C:\\tmp\\크롤링')



# data1 <- read.csv("인스타크롤링_딩고.csv", encoding = "cp949")
data1 <- readLines("인스타크롤링_딩고.txt")

head(data1,5)

summary((data1))


head(sort(wordcount, decreasing=T),20)

data2 <- unlist(data1)
length(data2)
head(data2)
wordcount <- table(data2)
head(sort(wordcount, decreasing=T),30)


sub1 <- c('딩고', 'Dingo','dingo', '멍스타그램', '애견카페', '강아지','dog', '까꿍', '서산')
i <- 1
cnt_txt <- length(sub1)
cnt_txt
class(data2)
for ( i in 1:cnt_txt) {data2 <- gsub((sub1[i]), "", data2)}


# data2 <- gsub('모바','모바일', data2)


data3 <- Filter(function(x) {nchar(x)>1}, data2)

wordcount2<- table(data3)

head(sort(wordcount2, decreasing=T),10)

wordcloud <- head(sort(wordcount2, decreasing=T),50)



wordcloud2(data = wordcloud, size = 0.7,fontFamily = '나눔바른고딕', color = "random-dark", shape = "circle")

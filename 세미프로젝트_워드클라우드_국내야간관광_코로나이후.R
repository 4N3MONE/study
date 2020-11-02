#¿öµåÅ¬¶ó¿ìµåÀÇ »ö»ó º¯°æÇÏ±â ±â´É Æ÷ÇÔ
#Step 1. ÇÊ¿äÇÑ ÆÐÅ°Áö ¼³Ä¡ ¹× ½ÇÇà
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
#Step 2. »çÀü °ü·Ã ÀÛ¾÷
useNIADic() 
getwd()

setwd('C:\\tmp\\Å©·Ñ¸µ')
# csv <- read.table("±¹³»¾ß°£°ü±¤_ºí·Î±×_2020-10-16_ÄÚ·Î³ªÀÌÀü.csv", encoding="UTF-8", header = T, fill = T)
data1 <- readLines("±¹³»¾ß°£°ü±¤_ºí·Î±×_2020-10-16_ÄÚ·Î³ªÀÌÈÄ_ÅØ½ºÆ®.txt")
data1 <- gsub("//d+","",data1)
data1 <- gsub("[[:punct:]]", "", data1)
data1 <- gsub("^[°¡-ÆR]", "", data1)
data1 <- gsub("[A-Za-z]", "", data1)
data1 <- gsub("¡â", "", data1)
data1 <- gsub("¡ã", "", data1)
data1 <- gsub("¢º", "", data1)
data1 <- gsub("^", "", data1)
data1 <- gsub("¡å", "", data1)

data2 <- extractNoun(data1)
head(data2,5)
data3 <- unlist(data2)
head(data3)

data4 <- Filter(function(x) {nchar(x) <= 10 & nchar(x) >1}, data3)
length(data4)
head(data4)
wordcount <- table(data4)
head(sort(wordcount, decreasing=T),100)

sub1 <- c("\\d+","¾ß°£","°ü±¤", "¿©Çà", "¼±Á¤", "°ø»ç", "±¹³»", "½Ã°£", "ÇÑ±¹°ü±¤", "Áö¿ª", "°ü±¤°´", "¸í¼Ò", "°ü±¤Áö", "´Ù¾ç", "ÃßÃµ", "¿î¿µ", "¹®È­", "»ê¾÷","ÇÏ³ª", 
          "ÀÌ¹ø", "ÇÑ±¹", "Àü¸Á", "°Å¸®", "»êÃ¥", "¸Å·Â", "È°¼ºÈ­", "»çÁø", "»ç¾÷", "ÄÚ½º", "ÇÁ·Î±×·¥", "µµ½Ã", "¹ßÇ¥", "¼Ò°³", "°æÁ¦",
          "ÄÜÅÙÃ÷", "¸ð½À", "Àü±¹", "°¡´É", "ÁøÇà", "ÃßÁø", "È¿°ú", "½ÃÀÛ", "Àü¹®°¡", "¼¼°è", "ÇÏ±â", "¹æ¹®", "»ç¶÷", "À¯¸í", "»ý°¢", "´ëÇ¥", "¶§¹®", "À§Ä¡", "°æ°ü",
          "https", "ÇÏ¸é", "¿ÃÇØ", "°ø°£", "ÀÌ°÷", "¤»", "¤¾", "¾ßÇà", "ÃÖÁ¾", "¿¹¾à", "½Å±Ô", "¿¹Á¤", "ÀÌ¸§", "ÁØºñ", "È«º¸", "¿À´Ã", "ÆÇ´Ü", "Æ¯º°", "¿¬°á", "Á¤º¸", "ÇÙ½É",
          "ÃÖÃÊ", "¾È³ç", "¾Æ·¡", "°­È­", "ÀÌ¿ë", "Á¦°ø", "Áö¹æÀÚÄ¡´ÜÃ¼", "naver", "com", "ÃÖ´ë", "È¨ÆäÀÌÁö", "ÅÚ·¹ÄÞ", "¸¶ÄÉÆÃ", "±â¾÷", "¸ÀÁý", "Áö¿ø", "»óÇ°", "¼­ºñ½º", "www",
          "µéÀÌ", "ÀÖ½À´Ï","^^")
i <- 1
cnt_txt <- length(sub1)
cnt_txt
for ( i in 1:cnt_txt) {data4 <- gsub((sub1[i]), "", data4)}

data5 <- Filter(function(x) {nchar(x)<= 10&nchar(x)>1}, data4)
wordcount2 <- table(data5) 
wordcount2 <- head(sort(wordcount2, decreasing=T),250)

palete <- brewer.pal(8,"Dark2")
wordcloud2(data = wordcount2, fontFamily = '³ª´®¹Ù¸¥°íµñ', color = "random-dark", shape = "circle")


setwd('c:\\tmp')
write.csv(wordcount2, file = "wordcount2_ÄÚ·Î³ªÀÌÈÄ.csv")
wordcount3 <- read.csv('wordcount2_ÄÚ·Î³ªÀÌÈÄ.csv', header = T)
head(wordcount3,20)

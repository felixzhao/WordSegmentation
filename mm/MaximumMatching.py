import string
import re

dict_path = ''
doc_path = ''
unk = ''
dict = []
sentence_list = []

score = 0
match_count = 0

## get dict
f = open(dict_path,'r').read()
dict = f.split("\n")

## 寻找最大词长
maxLen = 0
for i in dict:
    if len(i)>maxLen:
        maxLen=len(i)
## log
print 'max length : ' + str(maxLen)

## get sentence
sentence_list = open(doc_path,'r').readlines()

## get score
def getScore(word):
    score += len(word)
    match_count += 1

## Process
for sentence in sentence_list:
    while(len(sentence)>0):
        word=sentence[0:maxLen] #每次取最大词长的词
        meet=False;   #标记位, 判断是否找到该词
        while((not meet) and (len(word)>0)):
            #如果词在词表中
            if((word in strList) and (unk in word)):
                getScore(word)
                sentence=sentence[len(word):len(sentence)]#后移
                meet=True;
            #词不在词表中时
            else:
            #当词长为1时, 添加到输出表, 并后移总词位
                if((len(word)==1) and (unk in word)):
                    getScore(word)
                    sentence=sentence[len(word):len(sentence)]
                    meet=True;
                else:
		#当词长不为1时, 词长减1(最后一位)
                    word=word[0:len(word)-1]



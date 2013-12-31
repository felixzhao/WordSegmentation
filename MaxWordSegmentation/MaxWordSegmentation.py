# -*- coding: cp936 -*-
#最大匹配法进行分词, 测试文件为MaxWordSegmentationTest.py
#author 徐能
#date 2013/3/25
import string
import re

#读入词表文件到内存list
#输入:词典文件名, 输出:词典中所有词的list表,其中最大词长
def load_dict(filename):
	f = open(filename,'r').read()
	maxLen = 1
	strList=f.split("\n")

	#寻找最大词长
	for i in strList:
		if len(i)>maxLen:
			maxLen=len(i)

	return strList,maxLen;

#分词方法.
#输入:词表中所有词的列表与其中的最大词长, 输出:分词后的列表
def segmentation(strList,maxLen,sentence):
	wordList=[]	 #用于输出的词列表

	while(len(sentence)>0):
		word=sentence[0:maxLen] #每次取最大词长的词

		meet=False;   #标记位, 判断是否找到该词

		while((not meet) and (len(word)>0)):
			#如果词在词表中
			if(word in strList):
				wordList.append(word)   #添加到输出列表
				sentence=sentence[len(word):len(sentence)]#后移
				meet=True;
			#词不在词表中时
			else:
				#当词长为1时, 添加到输出表, 并后移总词位
				if(len(word)==1):
					wordList.append(word)
					sentence=sentence[len(word):len(sentence)]
					meet=True;
				else:
				#当词长不为1时, 词长减1(最后一位)
					word=word[0:len(word)-1]
	return wordList

#主函数
def main():
	strList,maxLen=load_dict('dict.txt')
	print("词表中最大词长度为:",maxLen)
    #输入句子
	sentence = input('请输入中文句子：')
	print('输入的句子为:',sentence)
#	sentence='迈向充满希望的新世纪'
	print('输入的句子为:',sentence)
	length=len(sentence)
	print('输入的句子长度:',length)
	print("****************开始解析**********************")
	wordl=segmentation(strList,maxLen,sentence)
	#打印分词结果
	for eachChar in wordl:
		print(eachChar,end = "/ ")
	print("")#换行
	print("****************解析完毕!*********************")

#运行
if __name__ == '__main__':
	main()
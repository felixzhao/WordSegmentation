# -*- coding: cp936 -*-
#���ƥ�䷨���зִ�, �����ļ�ΪMaxWordSegmentationTest.py
#author ����
#date 2013/3/25
import string
import re

#����ʱ��ļ����ڴ�list
#����:�ʵ��ļ���, ���:�ʵ������дʵ�list��,�������ʳ�
def load_dict(filename):
	f = open(filename,'r').read()
	maxLen = 1
	strList=f.split("\n")

	#Ѱ�����ʳ�
	for i in strList:
		if len(i)>maxLen:
			maxLen=len(i)

	return strList,maxLen;

#�ִʷ���.
#����:�ʱ������дʵ��б������е����ʳ�, ���:�ִʺ���б�
def segmentation(strList,maxLen,sentence):
	wordList=[]	 #��������Ĵ��б�

	while(len(sentence)>0):
		word=sentence[0:maxLen] #ÿ��ȡ���ʳ��Ĵ�

		meet=False;   #���λ, �ж��Ƿ��ҵ��ô�

		while((not meet) and (len(word)>0)):
			#������ڴʱ���
			if(word in strList):
				wordList.append(word)   #��ӵ�����б�
				sentence=sentence[len(word):len(sentence)]#����
				meet=True;
			#�ʲ��ڴʱ���ʱ
			else:
				#���ʳ�Ϊ1ʱ, ��ӵ������, �������ܴ�λ
				if(len(word)==1):
					wordList.append(word)
					sentence=sentence[len(word):len(sentence)]
					meet=True;
				else:
				#���ʳ���Ϊ1ʱ, �ʳ���1(���һλ)
					word=word[0:len(word)-1]
	return wordList

#������
def main():
	strList,maxLen=load_dict('dict.txt')
	print("�ʱ������ʳ���Ϊ:",maxLen)
    #�������
	sentence = input('���������ľ��ӣ�')
	print('����ľ���Ϊ:',sentence)
#	sentence='�������ϣ����������'
	print('����ľ���Ϊ:',sentence)
	length=len(sentence)
	print('����ľ��ӳ���:',length)
	print("****************��ʼ����**********************")
	wordl=segmentation(strList,maxLen,sentence)
	#��ӡ�ִʽ��
	for eachChar in wordl:
		print(eachChar,end = "/ ")
	print("")#����
	print("****************�������!*********************")

#����
if __name__ == '__main__':
	main()
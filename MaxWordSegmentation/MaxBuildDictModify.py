# -*- coding: cp936 -*-
#修正词表文件.
#author 徐能
#date 2013/3/24
import string
import re

#输入:dict_tmp.txt文件; 输出:dict.txt(已经去重复, 去特殊符号)
def create_dict(filename):
	print("读取文件......")
	src_data = open(filename,'r').read()
	data = src_data.split()#分割

	print("正在建立词表文件......")
	tmp = []
	for i in range(0,len(data)):
	   ok_data = re.compile(r'\]..').sub('',data[i]) #将类似的词']..埃特纳'前面的东西去掉
	   tmp.append(ok_data+'\n')

	print("去重复前的词数为:",len(tmp))
	set_data = set(tmp)	#去重复
	lalst_data = list(set_data) #set转换成list, 否则不能索引
	print("去除重复后总词数为:",len(lalst_data))

	open('dict.txt','w').writelines(lalst_data)
	print("最终词表文件建立完成! (dict.txt)")


#运行
if __name__ == '__main__':
    create_dict('dict_tmp.txt')
##    create_dict('testdict1.txt')
##    create_dict('testdict2.txt')
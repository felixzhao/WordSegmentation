# -*- coding: cp936 -*-
#�����ʱ��ļ�.
#author ����
#date 2013/3/24
import string
import re

#����:dict_tmp.txt�ļ�; ���:dict.txt(�Ѿ�ȥ�ظ�, ȥ�������)
def create_dict(filename):
	print("��ȡ�ļ�......")
	src_data = open(filename,'r').read()
	data = src_data.split()#�ָ�

	print("���ڽ����ʱ��ļ�......")
	tmp = []
	for i in range(0,len(data)):
	   ok_data = re.compile(r'\]..').sub('',data[i]) #�����ƵĴ�']..������'ǰ��Ķ���ȥ��
	   tmp.append(ok_data+'\n')

	print("ȥ�ظ�ǰ�Ĵ���Ϊ:",len(tmp))
	set_data = set(tmp)	#ȥ�ظ�
	lalst_data = list(set_data) #setת����list, ����������
	print("ȥ���ظ����ܴ���Ϊ:",len(lalst_data))

	open('dict.txt','w').writelines(lalst_data)
	print("���մʱ��ļ��������! (dict.txt)")


#����
if __name__ == '__main__':
    create_dict('dict_tmp.txt')
##    create_dict('testdict1.txt')
##    create_dict('testdict2.txt')
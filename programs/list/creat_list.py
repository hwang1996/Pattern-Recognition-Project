# -*- coding:utf-8 -*-
'''
author: Hao.Wang
date: 2017/11/17
'''

#����Python�Դ��ĺ�����ȡͼƬ�����������е��ļ�����list��

import os

def file_name(file_dir):   
    L=[]   
    for root, dirs, files in os.walk(file_dir):  
        for file in files:  
            if os.path.splitext(file)[1] == '.jpg':  
                L.append(os.path.join(root, file))  
    return L 


f1 = open("/data6/wanghao/pattern_recognition_project/list/list_train.txt", "w")

count = 0
list=file_name("/data6/wanghao/pattern_recognition_project/train/original")   #listΪ�ļ��������е�ͼƬ����list��
num = len(list)     #numΪlist�ĳ���
#д��TXT�ļ���
while num:
	f1.write(list[num-1]+'\n')
	num -= 1
	count += 1

print count
f1.close()
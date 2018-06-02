# -*- coding:utf-8 -*-
'''
author: Hao.Wang
date: 2017/11/17
'''

#利用Python自带的函数读取图片，并保存所有的文件名到list里

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
list=file_name("/data6/wanghao/pattern_recognition_project/train/original")   #list为文件夹下所有的图片名的list型
num = len(list)     #num为list的长度
#写入TXT文件内
while num:
	f1.write(list[num-1]+'\n')
	num -= 1
	count += 1

print count
f1.close()
# -*- coding:utf-8 -*-
'''
author: Hao.Wang
date: 2017/11/15
'''

from PIL import Image, ImageEnhance
from data_argumentation import DataAugmentation

#打开图像文件
f1 = open("/data6/wanghao/pattern_recognition_project/list/train/list_train_label_augmentation_flip.txt")
f2 = open("/data6/wanghao/pattern_recognition_project/list/train/list_train_label_augmentation_full.txt", "w")

line = f1.readline()
count = 0
#对list里的图片进行逐个处理
while line:
	arr = line.split(' ')[::1]
	im = Image.open(arr[0])
	f2.write(line)
	count += 1

	#利用自带的库函数以及自己编写好的函数，对图像进行数据增强
	#分别为左右翻转、上下翻转、随机颜色抖动、加入随机高斯噪声

	'''
	img_1 = im.transpose(Image.FLIP_LEFT_RIGHT)
	image_name = '/data6/wanghao/pattern_recognition_project/train/argumentation_more/'+'flip_horizontal_'+str(count)+'.jpg'
	img_1.save(image_name)
	f2.write(image_name+' '+arr[1])

	img_2 = im.transpose(Image.FLIP_TOP_BOTTOM)
	image_name = '/data6/wanghao/pattern_recognition_project/train/argumentation_more/'+'flip_vertical_'+str(count)+'.jpg'
	img_2.save(image_name)
	f2.write(image_name+' '+arr[1])
	'''

	img_1 = DataAugmentation.randomColor(im)
	image_name = '/data6/wanghao/pattern_recognition_project/train/argumentation_more/'+'randomColor_'+str(count)+'.jpg'
	img_1.save(image_name)
	f2.write(image_name+' '+arr[1])

	img_2 = DataAugmentation.randomGaussian(im)
	image_name = '/data6/wanghao/pattern_recognition_project/train/argumentation_more/'+'randomGaussian_'+str(count)+'.jpg'
	img_2.save(image_name)
	f2.write(image_name+' '+arr[1])
	

	line = f1.readline()

print count
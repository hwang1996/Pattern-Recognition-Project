# -*- coding:utf-8 -*-
'''
author: Hao.Wang
date: 2017/11/15
'''

from PIL import Image, ImageEnhance
from data_argumentation import DataAugmentation

#打开图像的列表文件
f1 = open("/data6/wanghao/pattern_recognition_project/list/train/list_train_original.txt")
f2 = open("/data6/wanghao/pattern_recognition_project/list/train/list_train_else.txt", "w")
line = f1.readline()
while line:
	arr = line.split('/')[::1]
	line = line[:-1]
	im = Image.open(line)

	#进行随机旋转处理
	img = DataAugmentation.randomRotation(im)
	img_name = arr[0]+'/'+arr[1]+'/'+arr[2]+'/'+arr[3]+'/'+arr[4]+'/'+'randomRotation'+'/'+arr[6]+'/'+arr[7][:-1]
	img.save(img_name)
	f2.write(img_name+'\n')

	#进行对比度改变处理
	enh_con = ImageEnhance.Contrast(im)  
	contrast = 1.5  
	image_contrasted = enh_con.enhance(contrast)  
	img_name = arr[0]+'/'+arr[1]+'/'+arr[2]+'/'+arr[3]+'/'+arr[4]+'/'+'contrast'+'/'+arr[6]+'/'+arr[7][:-1]
	image_contrasted.save(img_name)
	f2.write(img_name+'\n')

	#进行锐度改变处理
	enh_sha = ImageEnhance.Sharpness(im)  
	sharpness = 3.0  
	image_sharped = enh_sha.enhance(sharpness)  
	img_name = arr[0]+'/'+arr[1]+'/'+arr[2]+'/'+arr[3]+'/'+arr[4]+'/'+'sharpness'+'/'+arr[6]+'/'+arr[7][:-1]
	image_sharped.save(img_name)
	f2.write(img_name+'\n')

	#进行亮度改变处理
	enh_bri = ImageEnhance.Brightness(im)  
	brightness = 1.5  
	image_brightened = enh_bri.enhance(brightness)  
	img_name = arr[0]+'/'+arr[1]+'/'+arr[2]+'/'+arr[3]+'/'+arr[4]+'/'+'brightness'+'/'+arr[6]+'/'+arr[7][:-1]
	image_brightened.save(img_name)
	f2.write(img_name+'\n')

	line = f1.readline()

f1.close()
f2.close()
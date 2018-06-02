# -*- coding:utf-8 -*-
'''
author: Hao.Wang
date: 2017/11/15
'''

from PIL import Image, ImageEnhance
from data_argumentation import DataAugmentation

#��ͼ���ļ�
f1 = open("/data6/wanghao/pattern_recognition_project/list/train/list_train_label_augmentation_flip.txt")
f2 = open("/data6/wanghao/pattern_recognition_project/list/train/list_train_label_augmentation_full.txt", "w")

line = f1.readline()
count = 0
#��list���ͼƬ�����������
while line:
	arr = line.split(' ')[::1]
	im = Image.open(arr[0])
	f2.write(line)
	count += 1

	#�����Դ��Ŀ⺯���Լ��Լ���д�õĺ�������ͼ�����������ǿ
	#�ֱ�Ϊ���ҷ�ת�����·�ת�������ɫ���������������˹����

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
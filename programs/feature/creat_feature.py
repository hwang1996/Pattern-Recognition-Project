# -*- coding:utf-8 -*-
'''
author: Hao.Wang
date: 2017/11/15
'''

import numpy as np
import os, sys
sys.path.insert(0, "/data5/wanghao/caffe/python/")
import caffe 
import PIL 
from PIL import Image
import scipy.io as scio 

#读取图像名list，和预训练好的模型
IMAGE_TXT = '/data6/wanghao/pattern_recognition_project/list/train/list_train_label_augmentation_full.txt'
MODEL_FILE = '/data6/wanghao/pattern_recognition_project/net/alexnet_deploy.prototxt'
PRETRAINED = '/data6/wanghao/pattern_recognition_project/model/more_data_finetune_0.745358_160000.caffemodel';

#调取caffemodel
net = caffe.Net(MODEL_FILE,PRETRAINED,caffe.TEST)
caffe.set_mode_gpu()

image_width = 227
image_height = 227
count = 0

f = open(IMAGE_TXT,'r')

data  = np.zeros((1,3,image_width,image_height),np.float32)
label = np.zeros((1,1,1,1),np.float32)
net.set_input_arrays(data,label)
image_data = np.zeros((0, 4096), np.float32)
image_label = np.zeros((19710, 1), np.int)

for line in f:
	count += 1
	idx1 = line.find('.jpg')
	FullName = line[0:idx1+4]

	label_temp = line[idx1+5:]
	label = int(label_temp)
	image_label[count-1, 0] = label

	img  = Image.open(FullName)
	img = img.resize((image_height,image_width),PIL.Image.ANTIALIAS)
	try:
		r,g,b = img.split()
	except:
		pass
	data[0,0,:,:] = b
	data[0,1,:,:] = g
	data[0,2,:,:] = r

	prediction = net.forward()
	   
	image_data = np.vstack((image_data, net.blobs['fc7'].data))
	print 'Processing No.'+str(count)
	print image_data.shape
	
data = '/data6/wanghao/pattern_recognition_project/mat/19710_4096/train_data.mat'
scio.savemat(data, {'image_data': image_data}) 
label = '/data6/wanghao/pattern_recognition_project/mat/19710_4096/train_label.mat'
scio.savemat(label, {'image_label': image_label}) 
f.close()
print count
#-*- encoding: utf-8 -*-

import sys
import numpy as np
import os, sys
sys.path.insert(0, "/data5/wanghao/caffe/python/")
import os.path as osp
import caffe
import random
import cv2
import scipy.misc
from PIL import Image

class train_data_layer(caffe.Layer):

    def setup(self, bottom, top):
        self.top_names = ['data', 'label']

        # 读取输入的参数
        params = eval(self.param_str)
        print "init data layer"
        print params

        self.batch_size = params['batch_size']  # batch_size 
        self.source = params['source']
        self.crop_size = params['crop_size']

		#将图片转化为统一大小
        top[0].reshape(self.batch_size, 3, params['crop_size'], params['crop_size'])
        top[1].reshape(self.batch_size, 1)
        self.batch_loader = BatchLoader(self.source, self.batch_size, self.crop_size)

    def forward(self, bottom, top):
        image_data, label_list = self.batch_loader.get_mini_batch()
        image_data = image_data.reshape(self.batch_size, 3, self.crop_size, self.crop_size)
        top[0].data[...] = image_data
        top[1].data[...] = label_list

    def backward(self, bottom, top):
        pass

    def reshape(self, bottom, top):
        pass

class BatchLoader(object):

    def __init__(self, source, batch_size, crop_size):
        print "init batch loader"
        self.batch_size = batch_size
        self.crop_size = crop_size

		#创建元组，用来存储图像和标签信息
        self.image_label = {}  # key:image_name    value:label

        fp = open(source)
        line = fp.readline()
		#逐个处理图像
        while line:
            data = line.strip().split()
            image_name = data[0]
            label = data[-1]
            self.image_label[image_name] = label
            line = fp.readline()

		#按标签给图像排序
        self.image_label = sorted(self.image_label.items(), key=lambda item:item[1])

        print "init batch loader over"

    def get_mini_batch(self):
	    #创建存放数据的数据
        image_list, label_list = self._get_batch(self.batch_size)
        blob = np.zeros([self.batch_size, self.crop_size, self.crop_size, 3])
        label_blob = np.zeros([self.batch_size, 1])

		#存入图像数据
        for i in range(len(image_list)):
            im = np.asarray(Image.open(image_list[i]))
            im = scipy.misc.imresize(im, [self.crop_size, self.crop_size]) # resize
            # do a simple horizontal flip as data augmentation
            flip = np.random.choice(2)*2-1
            im = im[:, ::flip, :]
            blob[i, ...] = im
            label_blob[i, ...] = i

        #cv_image_list = map(lambda image_name: (cv2.imread(image_name).astype(np.float32, copy=False).transpose((2, 0, 1))), image_list)
        #blob = np.require(cv_image_list)
        #label_blob = np.require(label_list, dtype=np.float32).reshape((self.batch_size, 1))
        return blob, label_blob
    
    def _get_batch(self, batch_size):
        image_list = []
        label_list = []
        image_num = [0, 895, 965, 1200, 1345, 1520, 1865, 2190]

		#随机读取图像
        for i in range(batch_size):
            image_id = random.randint(0, image_num[i+1]-image_num[i]-1)
            image_list.append(self.image_label[image_id+image_num[i]][0])
            label_list.append(int(self.image_label[image_id+image_num[i]][1]))

        return image_list, label_list
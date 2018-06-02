# -*- coding:utf-8 -*-
'''
author: Hao.Wang
date: 2017/11/17
'''

import numpy as np
import os, sys
sys.path.insert(0, "/data5/wanghao/caffe/python/")
import caffe 
import PIL 
from PIL import Image

#读取图像名list，和预训练好的模型
IMAGE_TXT = '/data6/wanghao/pattern_recognition_project/list/test/list_test_label.txt'
PREDICT_RESULT = '/data6/wanghao/pattern_recognition_project/list/predict/list_test_aug_2_predict.txt'

MODEL_FILE = '/data6/wanghao/pattern_recognition_project/net/alexnet_deploy.prototxt'
PRETRAINED = '/data6/wanghao/pattern_recognition_project/net/model_res/model_res_iter_160000.caffemodel';

#调取caffe的网络
net = caffe.Net(MODEL_FILE,PRETRAINED,caffe.TEST)
caffe.set_mode_gpu()  #设置caffe的GPU工作模式

#进入的图片处理大小
image_width = 227
image_height = 227

f = open(IMAGE_TXT,'r')
fsave = open(PREDICT_RESULT,'w')

#变量置0
count=0;
diff_sum = 0;
diff_softmax_sum = 0.0;
num_right = 0.0;

#创建送入预测网络的data label数组 
data  = np.zeros((1,3,image_width,image_height),np.float32)
label = np.zeros((1,1,1,1),np.float32)

net.set_input_arrays(data,label)
test = 0
#对每个图像进行处理
for line in f:
   count = count +1;
   idx1 = line.find('.jpg')
   fullName = line[0:idx1+4]
   
   label_temp = line[idx1+5:]
   true_label = float(label_temp)
   
   FullName=fullName
  
  #分别获取图像RGB三通道的信息
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

   image_data = net.blobs['fc6'].data

   #获取神经网络prob层的数据，每一类的概率便可以得出
   predict_gender_data = net.blobs['prob'].data
   gender_prob0 = predict_gender_data[0][0]
   gender_prob1 = predict_gender_data[0][1]
   gender_prob2 = predict_gender_data[0][2]
   gender_prob3 = predict_gender_data[0][3]
   gender_prob4 = predict_gender_data[0][4]
   gender_prob5 = predict_gender_data[0][5]
   gender_prob6 = predict_gender_data[0][6]

   c = [gender_prob0, gender_prob1, gender_prob2, gender_prob3, gender_prob4, gender_prob5, gender_prob6]

   #取概率最大的那一类作为预测的输出
   predict_label = c.index(max(c))
   predict_probability = c[predict_label]
   if(predict_label==0):
         test+=1
   #打印出预测数据
   if(predict_label == true_label):
      num_right = num_right + 1
      print('Real Gender label:%f,Predict Gender label:%f, Predict Probability:%f, Gender classify right!' % (true_label,predict_label,predict_probability))
      print >> fsave,'%d %d %f' % (true_label, predict_label, predict_probability)
   else:
      print('Real Gender label:%f,Predict Gender label:%f, Predict Probability:%f, Gender classify error!' % (true_label,predict_label,predict_probability))
      print >> fsave,'%d %d %f' % (true_label, predict_label, predict_probability)

#计算出准确率并输出
Accuracy = num_right/count
print test
print('The accuracy of Gender Classification:  %f' % Accuracy)

f.close()  
fsave.close()
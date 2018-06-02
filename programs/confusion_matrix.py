# -*- coding: UTF-8 -*-
'''
author: Hao.Wang
date: 2017/11/17
'''

"""绘制混淆矩阵图"""
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
 
 
def confusion_matrix_plot_matplotlib(y_truth, y_predict, cmap=plt.cm.Reds):
    """Matplotlib绘制混淆矩阵图
    parameters
    ----------
        y_truth: 真实的y的值, 1d array
        y_predict: 预测的y的值, 1d array
        cmap: 画混淆矩阵图的配色风格, 使用cm.Blues，更多风格请参考官网
    """
    cm = confusion_matrix(y_truth, y_predict)
    plt.matshow(cm, cmap=cmap)  # 混淆矩阵图
    plt.colorbar()  # 颜色标签
 
    for x in range(len(cm)):  # 数据标签
        for y in range(len(cm)):
            plt.annotate(cm[x, y], xy=(x, y), horizontalalignment='center', verticalalignment='center')
 
    plt.ylabel('Predicted label')  # 坐标轴标签
    plt.xlabel('True label')  # 坐标轴标签
    plt.show()  # 显示作图结果
 
 
if __name__ == '__main__':
    y_truth = []
    y_predict = []
	#读取输出的预测文件数据
    f = open("/data6/wanghao/pattern_recognition_project/list/predict/list_test_aug_0.744032_predict.txt")
    line = f.readline()
    while line:
        arr = line.split(' ')[::1]
        y_truth.append(int(arr[0]))
        y_predict.append(int(arr[1]))
        line = f.readline()

    confusion_matrix_plot_matplotlib(y_truth, y_predict)
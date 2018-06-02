f1 = open("/data6/wanghao/pattern_recognition_project/list/predict/list_test_original_predict.txt")
f2 = open("/data6/wanghao/pattern_recognition_project/list/predict/list_test_finetune_predict.txt")
f3 = open("/data6/wanghao/pattern_recognition_project/list/predict/list_test_vote_predict.txt", "w")
f = open('/data6/wanghao/pattern_recognition_project/list/test/list_test_label.txt','r')

l1 = []
l2 = []
count = 0
num_right = 0
num = 0

line = f1.readline()
while line:
	arr = line.split(' ')[::1]
	l1.append(arr[1])
	line = f1.readline()

line = f2.readline()
while line:
	arr = line.split(' ')[::1]
	l2.append(arr[1])
	line = f2.readline()

for line in f:
	count = count +1;
   	idx1 = line.find('.jpg')
   	fullName = line[0:idx1+4]
   	
   	label_temp = line[idx1+5:]
   	true_label = int(label_temp)

   	if(l2[count-1]=='5'):
   		predict_label = 5
   	elif(l1[count-1]=='0'):
   		predict_label = 0
   	else:
   		predict_label = int(l2[count-1])

   	if(predict_label == true_label):
   		num_right = num_right + 1
   		print >> f3,'%d %d' % (true_label, predict_label)
   	else:
   		print >> f3,'%d %d' % (true_label, predict_label)

print num_right
print count
Accuracy = float(num_right)/float(count)
print('The accuracy of Gender Classification:  %f' % Accuracy)
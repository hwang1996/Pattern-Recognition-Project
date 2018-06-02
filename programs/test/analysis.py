f1 = open('/data6/wanghao/pattern_recognition_project/list/predict/list_test_aug_0.744032_predict.txt')

line = f1.readline()

f2 = open('/data6/wanghao/pattern_recognition_project/list/predict/right.txt', "w")

f3 = open('/data6/wanghao/pattern_recognition_project/list/predict/wrong.txt', "w")


while line:
	arr = line.split(' ')[::1]
	if arr[0] is not arr[1]:
		f3.write(line)
	if arr[0] is arr[1] and float(arr[2])>0.5:
		f2.write(line)
	line = f1.readline()

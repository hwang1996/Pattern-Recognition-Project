f0 = open("/data6/wanghao/pattern_recognition_project/list/train/category/0.txt", "w")
f1 = open("/data6/wanghao/pattern_recognition_project/list/train/category/1.txt", "w")
f2 = open("/data6/wanghao/pattern_recognition_project/list/train/category/2.txt", "w")
f3 = open("/data6/wanghao/pattern_recognition_project/list/train/category/3.txt", "w")
f4 = open("/data6/wanghao/pattern_recognition_project/list/train/category/4.txt", "w")
f5 = open("/data6/wanghao/pattern_recognition_project/list/train/category/5.txt", "w")
f6 = open("/data6/wanghao/pattern_recognition_project/list/train/category/6.txt", "w")

f = open("/data6/wanghao/pattern_recognition_project/list/train/list_train_label_full.txt")

line = f.readline()

while line:
	arr = line.strip().split()
	if(arr[1]=='0'):
		f0.write(line)
	if(arr[1]=='1'):
		f1.write(line)
	if(arr[1]=='2'):
		f2.write(line)
	if(arr[1]=='3'):
		f3.write(line)
	if(arr[1]=='4'):
		f4.write(line)
	if(arr[1]=='5'):
		f5.write(line)
	if(arr[1]=='6'):
		f6.write(line)
	line = f.readline()
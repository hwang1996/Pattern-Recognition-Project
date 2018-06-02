f1 = open("/data6/wanghao/pattern_recognition_project/list/train/category/0.txt")
f2 = open("/data6/wanghao/pattern_recognition_project/list/train/category/1.txt")
f3 = open("/data6/wanghao/pattern_recognition_project/list/train/category/2.txt")
f4 = open("/data6/wanghao/pattern_recognition_project/list/train/category/3.txt")
f5 = open("/data6/wanghao/pattern_recognition_project/list/train/category/4.txt")
f6 = open("/data6/wanghao/pattern_recognition_project/list/train/category/5.txt")
f7 = open("/data6/wanghao/pattern_recognition_project/list/train/category/6.txt")
f8 = open("/data6/wanghao/pattern_recognition_project/list/train/category/total.txt", "w")

line1 = f1.readline()
while line1:
	f8.write(line1)
	line1 = f1.readline()

line2 = f2.readline()
while line2:
	f8.write(line2)
	line2 = f2.readline()

line3 = f3.readline()
while line3:
	f8.write(line3)
	line3 = f3.readline()

line4 = f4.readline()
while line4:
	f8.write(line4)
	line4 = f4.readline()

line5 = f5.readline()
while line5:
	f8.write(line5)
	line5 = f5.readline()
	
line6 = f6.readline()
while line6:
	f8.write(line6)
	line6 = f6.readline()

line7 = f7.readline()
while line7:
	f8.write(line7)
	line7 = f7.readline()
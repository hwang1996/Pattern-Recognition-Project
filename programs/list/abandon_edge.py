f1 = open("/data6/wanghao/pattern_recognition_project/list/list_test_label.txt")
f2 = open("/data6/wanghao/pattern_recognition_project/list/list_test_label_without_edge.txt", "w")

line = f1.readline()

while line:
	arr = line.split('/')[::1]
	if(arr[5]!='edge_knot'):
		f2.write(line)
	line = f1.readline()

f1.close()
f2.close()

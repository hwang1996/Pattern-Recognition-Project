f1 = open("/data6/wanghao/pattern_recognition_project/list/train/list_train_else.txt")
f2 = open("/data6/wanghao/pattern_recognition_project/list/train/list_train_label_else.txt", "w")

line = f1.readline()
while line:
	arr = line.split('/')[::1]
	line = line[:-1]
	if(arr[6]=='sound_knot'):
		f2.write(line+' '+'0'+'\n')
	if(arr[6]=='decayed_knot'):
		f2.write(line+' '+'1'+'\n')
	if(arr[6]=='leaf_knot'):
		f2.write(line+' '+'2'+'\n')
	if(arr[6]=='encased_knot'):
		f2.write(line+' '+'3'+'\n')
	if(arr[6]=='horn_knot'):
		f2.write(line+' '+'4'+'\n')
	if(arr[6]=='dry_knot'):
		f2.write(line+' '+'5'+'\n')
	if(arr[6]=='edge_knot'):
		f2.write(line+' '+'6'+'\n')
	line = f1.readline()

f1.close()
f2.close()
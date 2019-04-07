#1、冒泡
def bubble(data):

	for i in range(len(data)-1,0,-1): #扫描次数
		flag = 0
		for j in range(i):
			if data[j]>data[j+1]:
				data[j],data[j+1] = data[j+1],data[j]
				flag += 1
		if flag = 0: #早已排好的，就不用再扫描了
			break
	return data

#2、选择
def select1(data):
	#利用辅助列表
	new = []
	while len(data)!=0:
		min_num = min(data)
		new.append(min_num)
		data.remove(min_num)
	return new

def select2(data):
	#在原列表交换
	for i in range(len(data)):
		for j in range(i+1,len(data)):
			if data[j] < data[i]: #data[i]作为当前最小值，指定位置
				data[i],data[j] = data[j],data[i]
	return data

#3、插入
def insert(data):
	for i in range(1,len(data)):
		tmp = data[i]
		j = i-1
		while j>=0 and tmp<data[j]:
			data[j+1] = data[j]
			j-=1
		data[j+1] = tmp #j在while中已经向前移了一位，但是原本位置j+1才是空出来的
	return data

#4、希尔,插入的升级版
def shell(data):
	gap = len(data)//2
	while gap!=0:
		for i in range(1,len(data),gap):
			tmp = data[i]
			j = i-gap
			while j>=0 and tmp<data[j]:
				data[j+gap] = data[j]
				j = j-gap
			data[j+gap] = tmp
		gap = gap//2
	return data

#5、合并排序
def merge_sort(data):
	if len(data)<2:
		return data
	else:
		mid = len(data)//2
		left = merge_sort(data[:mid])
		right = merge_sort(data[mid:])
		return merge(left,right)
def merge(left,right):
	# 从两个有顺序的列表里边依次取数据比较后放入result
	# 每次我们分别拿出两个列表中最小的数比较，把较小的放入result
	result = []
	while len(left)>0 and len(right)>0 :
		if left[0] <= right[0]:
			result.append( left.pop(0) )
		else:
			result.append( right.pop(0) )
	#while循环出来之后 说明其中一个数组没有数据了，我们把另一个数组添加到结果数组后面
	if len(right)==0:result += left
	if len(left)==0:result += right
	return result

#6、快速排序——递归实现
def quick(data):
	if len(data)<2:
		return data
	else:
		pivot = data[0] #基准值
		low = [i for i in data[1:] if pivot>i]
		high =[i for i in data[1:] if pivot<i]
		return quick(low) + pivot + quick(high) 

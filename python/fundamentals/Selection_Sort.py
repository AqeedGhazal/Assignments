
list = [5,2,6,7,9,1,4,8,3,0]
def selectionsort(some_list):
	for idx in range(len(some_list)-1):
		minimum = idx #  idx is 0 
		for i in range(idx+1,len(some_list)): # starts at i = 1 
			if list[i] < list[minimum]: # list[1] < list[0] = true 
				minimum=i # set minimum equal to i = 1 
				list[idx],list[minimum] = list[minimum] , list[idx] # do the swaping by putting list[0] ,list[1] = list[1] , list[0]
	return some_list
print(selectionsort(list))
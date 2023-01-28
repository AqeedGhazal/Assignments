#Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
#Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]

def biggie_size(list):
    for x in range(len(list)):
        if list[x]>0:
            list[x]="big"
    return list
#print(biggie_size([-1,3,5,-5,-3,-2,-1,1,2,3,4,5,6,7]))

#Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values.
#(Note that zero is not considered to be a positive number).
#Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
#Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it

def count_positives(nums_list):
    count = 0 
    for a in range(len(nums_list)):
        if nums_list[a]>=0:
            count+=1
    nums_list[len(nums_list)-1]=count
    return nums_list 
#print(count_positives([-1,1,1,1]))
#print(count_positives([1,6,-4,-2,-7,-2]))

#Sum Total - Create a function that takes a list and returns the sum of all the values in the list.
#Example: sum_total([1,2,3,4]) should return 10
#Example: sum_total([6,3,-2]) should return 7

def sum_total(nums_list):
    sum=0
    for s in range(len(nums_list)):
        sum+=nums_list[s]
    return sum

#print(sum_total([1,2,3,4,5,6,7,8,9,10]))
#print(sum_total([1,2,3,4]))
#print(sum_total([6,3,-2]))

#Average - Create a function that takes a list and returns the average of all the values.x
#Example: average([1,2,3,4]) should return 2.5

def average(nums_list):
    sum=0
    for a in range(len(nums_list)):
        sum+=nums_list[a]
    average =sum/len(nums_list)
    return average
#print(average([1,2,3,4])) # this will give 2.5 .
#print(average([1,2,3,4,5,6,7,8,9,10])) # this will give 5.5 .

#Length - Create a function that takes a list and returns the length of the list.
#Example: length([37,2,1,-9]) should return 4
#Example: length([]) should return 0

def length(any_list):
    return len(any_list)

#print(length([37,2,1,-9])) # this will give a list with length of 4 .
#print(length([])) # this will give a list with length of 0 . 

#Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
#Example: minimum([37,2,1,-9]) should return -9
#Example: minimum([]) should return False

def minimum(any_list):
    if len(any_list)==0:
        return "False"
    for m in range(len(any_list)): 
        minimum_value = min(any_list)
        return minimum_value
#print(minimum([]))
#print(minimum([6,2,1,-9]))

#Maximum - Create a function that takes a list and returns the maximum value in the list. If the list is empty, have the function return False.
#Example: maximum([37,2,1,-9]) should return 37
#Example: maximum([]) should return False

def minimum(any_list):
    if len(any_list)==0:
        return "False"
    for m in range(len(any_list)): 
        minimum_value = max(any_list)
        return minimum_value
#print(minimum([]))
#print(minimum([37,2,1,-9]))

#Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
#Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }

def ultimate_analysis(any_list):
    empty_dict={}
    empty_dict['sumTotal']=sum(any_list)
    empty_dict['average']=average(any_list)
    empty_dict['minimum']=min(any_list)
    empty_dict['maximum']=max(any_list)
    empty_dict['Length']=len(any_list)
    return empty_dict

#print(ultimate_analysis([37,2,1,-9]))

#Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
#Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]

def reverse_list(any_list):
    list_len = len(any_list)
    for x in range (int(list_len/2)):
        temp = any_list[list_len-1-x]
        any_list[list_len-1-x] =any_list[x]
        any_list[x] =temp
    return any_list

print(reverse_list([1,2,3,4,6,7,9]))


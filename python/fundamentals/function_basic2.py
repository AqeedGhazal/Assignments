#Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, 
#from the number (as the 0th element) down to 0 (as the last element).
#Example: countdown(5) should return [5,4,3,2,1,0]

def count_down(num):
    empty_list=[]
    for i in range(num,-1,-1):
        empty_list.append(i)
    return empty_list

print(count_down(5))

#Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.
#Example: print_and_return([1,2]) should print 1 and return 2

def print_and_return(newlist):
        print (newlist[0])
        return newlist[1]

print_and_return([11,22])
#print(print_and_return([11,22]))


#First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
#Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)

def first_plus_length(newlist):
    sum=newlist[0]+(len(newlist))
    return sum
print(first_plus_length([0,2,4,6,7,8,9,10,11,12]))

#Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original
#  list that are greater than its 2nd value.
#  Print how many values this is and then return the new list. 
# If the list has less than 2 elements, have the function return False
#Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
#Example: values_greater_than_second([3]) should return False

def value_greaterthan_second(orginal_list):
    new_list=[]
    count=0
    for i in range(len(orginal_list)):
        if orginal_list[i] > orginal_list[1]:
            new_list.append(orginal_list[i])
            count+=1
    print(count)
    return new_list
print(value_greaterthan_second([1,2,3,4,5,6,7,1,1,10]))

#This Length, That Value - Write a function that accepts two integers as parameters: size and value.
# The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
#Example: length_and_value(4,7) should return [7,7,7,7]
#Example: length_and_value(6,2) should return [2,2,2,2,2,2]

def length_and_value(size,value):
    new_list = []
    for k in range(size):
        new_list.append(value)
    return new_list
print(length_and_value(10,2))
print(length_and_value(20,1))


# Basic- print all integers from 0 to 150 .
for i in range(151):
    print(i)
# Multiples of Five .
for x in range(5,1001):
    if x % 5 ==0:
        print(x)
#Counting,the Dojo Way (print integer from 1 to 100. if divisible by 5 ,print "Coding , if divisible by 10 , print "Coding Dojo)
for x in range(1,101):
    if x % 5 ==0 and x % 10 != 0 :
        print("Coding")
    elif x % 10 ==0 :
        print("Coding Dojo")
    else:
        print(x)
# 4- Whoa .That Sucker's Huge - Add odd integer from 0 to 500,000 and print the final sum .
Count =0 
for r in range (1,500001,2):
    Count=Count+r
print(Count)

# 5- Flexible Counter - 
LowNum=5
highNum=65
Mult=7
for a in range (5,66):
    if a % Mult ==0 or a % Mult ==0:
        print(a)
#1
#1
def a():
    return 5
print(a())
# prediction is -- 5 


#2
def a():
    return 5
print(a()+a())
#pridection is 10 . 

#3
def a():
    return 5
    return 10
print(a())
#pridection is 5 .

#4
def a():
    return 5
    print(10)
print(a())
#pridection is 5 .

#5
def a():
    print(5)
x = a()
print(x)
#pridection is 5 , Non -- there is no return .

#6
#def a(b,c):
    #print(b+c)
#print(a(1,2) + a(2,3))
#pridection is 3 ,5 

#7
def a(b,c):
    return str(b)+str(c)
print(a(2,5))
#pridection is 25 . 

#8
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a())
#pridection is 100 ,10.

#9
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))
#pridection is 7 ,14 ,21 

#10
def a(b,c):
    return b+c
    return 10
print(a(3,5))

#pridection is 8 

#11
b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b)
#pridection is 500 , 500 , 300 ,500

#12
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b)
#pridection is 500 , 500 , 300 , 500 

#13
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b)
#pridection is 500 , 500 ,300 ,300

#14
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()
#pridection is 1 ,3 ,2 

#15
def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)
#pridection is ?????? 1 , 3 , 5 











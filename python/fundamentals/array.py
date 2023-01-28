# python code below!
arr = [1,3,5,7]
arr[0], arr[1] = arr[1], arr[0]
print(arr)

stack = 2 
print('coding dojo' if stack>=3 else 'you are not Dojo! ')

# define a function that takes one input that is a function
def invoker(callback):
    # invoke the input pass the argument 2
    print(callback(6))
invoker(lambda x: 2 * x)
invoker(lambda y: 5 + y)

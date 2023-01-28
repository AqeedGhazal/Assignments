

def beCheerful(name='a', repeat=2):		# set defaults when declaring the parameters
	print(f"good morning {name}\n" * repeat)
#beCheerful()				# output: good morning (repeated on 2 lines)
#beCheerful("tim")		        # output: good morning tim (repeated on 2 lines)
#beCheerful(name="john")			# output: good morning john (repeated on 2 lines)
#beCheerful(repeat=6)			# output: good morning (repeated on 6 lines)
#beCheerful('michael',5)	# output: good morning michael (repeated on 5 lines)
#NOTE: argument order doesn't matter if we are explicit when sending in our arguments!
#beCheerful(repeat=3, name="kb")		# output: good morning kb (repeated on 3 lines)


arr = [1,5,3,2,0,8]
def bubbleSort(arr):
	for i in range (len(arr)):
		print("\n","#"*80, "\nindex",i,"value",arr[i])
		print("comparing", arr[i],"to",arr[i+1])
		if arr[i] > arr[i+1]:
			arr[i] , arr[i+1] = arr[i+1] , arr[i]
			print ("swapped" , arr[i],arr[i+1])
		else:
			print("no need to swap" , arr[i],arr[i+1])

#bubbleSort(arr)



class User:
	def __init__(self, name, email_address,): # now our method has 2 parameters!
    		self.name = name			# and we use the values passed in to set the name attribute
    		self.email = email_address		# and the email attribute
    		self.account_balance = 0		# the account balance is set to $0, so no need for a third parameter
def make_deposit(self,amount):
		self.account_balance+=amount
guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")


#guido.make_deposit(100)
#print(guido.name)	# output: Guido van Rossum
#print(monty.name)	# output: Monty Python
#print(guido.account_balance)	

# import the library
import urllib.request
response = urllib.request.urlopen("http://www.codingdojo.com")
html = response.read()
print(html)


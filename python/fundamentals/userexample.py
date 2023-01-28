class User:
    def __init__(self,name,email_address): # self is always passed in implicitly
        self.name = name
        self.email = email_address
        self.account_balance =0 # this is a constant
    def make_deposit(self,amount): # don't forget that the first parameter of every method should be self 
        self.account_balance += amount
Aqeed = User("Aqeed","aqeedghazal@gmail.com")
khaled = User("Khaled","Khaledrabi@gmail.com")

print(Aqeed.name)
print(khaled.name)
khaled.make_deposit(100) # call the function from an instance of a class , it cant be called independently 
print(khaled.account_balance)
Aqeed.make_deposit(500)
print(Aqeed.account_balance)


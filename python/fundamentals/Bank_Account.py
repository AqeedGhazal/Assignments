class BankAccount:
	def __init__(self,int_rate = .02,balance = 0):
		self.balance = balance 
		self.int_rate = int_rate
	def deposit(self,amount):
		self.balance += amount
		return self 
	def withdraw(self,amount):
		if (self.balance-amount) > 0 :
			self.balance -= amount 
		else:
			print("insufficient funds: Charging a 5$ fee")
			self.balance -= 5 
		return self
	def display_account_info(self):
		self.balance = f"Balance: {self.balance} $ "
	def yield_interest(self):
		if self.balance > 0 : 
			self.balance = (self.balance *self.int_rate) + self.balance
		else: 
			print("your balance on nigative")
		return self

Aqeed = BankAccount(100)
Khaled = BankAccount(100)

Aqeed.deposit(100).deposit(100).deposit(100).withdraw(200).yield_interest().display_account_info()
Khaled.deposit(100).deposit(200).withdraw(50).withdraw(20).withdraw(30).yield_interest().display_account_info()

print (Aqeed.balance)
print (Khaled.balance)



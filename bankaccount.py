#!/usr/bin/env python3

class BankAccount():
	"""Represent a bank account."""
	
	def __init__(self, username, full_name, IC_number, contact_no, initial_savings):
		"""Initialize attributes for a bank account."""
		self.username = username
		self.fullname = full_name
		self.IC = IC_number
		self.contact = contact_no
		self.savings = initial_savings
		
	def customer_details(self):
		"""Return the details of the customer."""
		bank_details = self.username + ' ' + self.fullname + ' ' + str(self.IC) +  ' ' + str(self.contact) +  ' ' + str(self.savings)  
		return (bank_details)
	
	def deposit_money(self):
		"""Cash in some amount of money into the bank account."""
		amount = int(input("How much do you want to deposit?\n"))
		self.savings += amount
		print("You have deposited " + "RM" + str(amount) + " to your bank account.")
		return (print ("You have " + "RM" + str(self.savings) + " balance in your bank account!"))
	
	def withdraw_money(self):
		"""Cash out some amount of money.
		Reject the transaction if the bank account has lower than RM10."""
		amount = int(input("How much do you want to withdraw?\n"))
		self.savings -= amount
		
		if self.savings>=10:
			print ("You have withdrawn " + "RM" + str(amount) + " from your bank account.")
			return (print ("You have " + "RM" + str(self.savings) + " balance in your bank account!"))
		
		else:
			self.savings += amount
			print("Uh oh! You have an insufficient amount!")
			
			
	def check_balance(self):
		"""Print a statement showing the account balance."""
		print("You have " + "RM" + str(self.savings) + " in your bank account.")
		
		
	def close_account(self):
		"""Print the statement to close the bank account."""
		username = input("Please enter your username:\n")
		IC_number = input("Please enter your IC number:\n")
		if username == self.username and IC_number == str(self.IC):           
			print('You have successfully closed the bank account! Sorry to see you go.')
			del self.username
			del self.fullname
			del self.IC
			del self.contact
			del self.savings
		else:
			print('You have entered a wrong username/IC Number.')
			
			
"This would create the first customer of BankAccount class"
customer1 = BankAccount('yayan97', 'Nazian K', 970205035774, 60199059773, 5300)
"This would create the second customer of BankAccount class"
customer2 = BankAccount('amier.s', 'Amier Syafiq', 960212145213, 60145643322, 10567)
"This would create the third customer of BankAccount class"
customer3 = BankAccount('hazmieus', 'Hazmie Hadi', 970207065511, 60178657645, 2100)
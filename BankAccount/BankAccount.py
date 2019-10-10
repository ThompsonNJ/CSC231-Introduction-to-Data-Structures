#==========================================================================
# PROGRAM:... ....... Assignment 02 - Classes and Objects
# AUTHOR:............ Thompson, Nick
# COURSE:............ CSC 231 001
# TERM:.............. Spring 2018
# COLLABORATION:..... Documentation and tutoring lab for help with using classes;
#                     Documentation for help with using argv
#==========================================================================

class BankAccount:
    def __init__(self, acc_type, acc, first, last, bal):
        self.account_type = acc_type
        self.account_number = acc
        self.first_name = first
        self.last_name = last
        self.account_balance = bal
        
    def __repr__(self):
        return "{}, {,} {}, ${:,.2f}".format(self.account_number, self.last_name, self.first_name, self.account_balance)

    def __str__(self):
        return "{}, {}, {}, ${:,.2f}".format(self.account_number, self.last_name, self.first_name, self.account_balance)

    def deposit(self, amt):
        return amt + self.account_balance

    def withdraw(self, amt):
        return self.account_balance - amt

    def __lt__(self, other):
        return self.account_balance < other.account_balance
    
    def __eq__(self, other):
        return self.account_number == other.account_number

class CheckingAccount(BankAccount):
    def calculate_interest(self):
        return round((0.015*self.account_balance), 2)

class SavingsAccount(BankAccount):
    def calculate_interest(self):
        return round((0.025*self.account_balance), 2)

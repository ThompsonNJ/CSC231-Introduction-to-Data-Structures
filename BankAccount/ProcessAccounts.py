#==========================================================================
# PROGRAM:... ....... Assignment 02 - Classes and Objects
# AUTHOR:............ Thompson, Nick
# COURSE:............ CSC 231 001
# TERM:.............. Spring 2018
# COLLABORATION:..... Documentation and tutoring lab for help with using classes;
#                     Documentation for help with using argv
#==========================================================================
from BankAccount import *
import sys

def file_open():
    with open(sys.argv[1], 'r') as file:
        return file.readlines()
    

def convert(file_list):
    converted = []
    file_list = file_list[1:]
    checkings_count = 0
    savings_count = 0
    
    for i in file_list:
        line = i.split(',')
        if BankAccount(line[0], line[1], line[2], line[3], float(line[4].strip())) not in converted:
            if line[0] == "Checking":
                converted.append(CheckingAccount(line[0], line[1], line[2], line[3], float(line[4].strip())))
                checkings_count += 1
            else:
                converted.append(SavingsAccount(line[0], line[1], line[2], line[3], float(line[4].strip())))
                savings_count += 1
        else:
            print("Warning! Account number already exists: {} ".format(line[1]))

    return sorted(converted), checkings_count, savings_count


def outputs(converted, checkings_count, savings_count):
    mean = 0
    for i in converted:
        mean += i.account_balance

    mean /= len(converted)
    
    if len(converted) % 2 != 0:
        median = converted[len(converted)//2]

    else:
        median = (converted[len(converted)//2].account_balance+converted[len(converted)//2-1].account_balance) / 2

    print("Number of checking accounts: {}".format(checkings_count))
    print("Number of savings accounts: {}".format(savings_count))
    print("Average balance: ${:,.2f}".format(mean))
    print("Biggest balance: {}".format(converted[-1]))
    print("Median balance: ${:,.2f}".format(median))

def interest(converted):
    for i in range(0, len(converted)):
        converted[i].account_balance += converted[i].calculate_interest()

    mean = 0
    for i in converted:
        mean += i.account_balance

    mean /= len(converted)
    
    print("Average balance with interest: ${:,.2f}".format(mean))    
        

file_list = file_open()
converted, checkings_count, savings_count = convert(file_list)
outputs(converted, checkings_count, savings_count)
interest(converted)

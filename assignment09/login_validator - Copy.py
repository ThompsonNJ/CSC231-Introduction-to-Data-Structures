from stackpractice import *
import time

class UserInfo:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __str__(self):
        return str("username: "+self.username+",password: "+self.password)

    def __eq__(self, other):
        if type(self) == type(other):
            return (self.username and self.password) == (other.username and other.password)

    def __lt__(self,other):
        if type(self) == type(other):
            return self.username < other.username

    def __gt__(self,other):
        if type(self) == type(other):
            return self.username > other.username

stack = Stack()
with open('users_500.csv') as file:
    line = file.readline().strip()
    while line != '':
        fields = line.split(',', 1)
        stack.push(UserInfo(fields[0],fields[1]))
        line = file.readline().strip()

for x in stack:
    print(x)
                   
#############################################################################        
# EC code

##def format_time(t):
##    if t > 1:
##        return '{:.1f}s'.format(t)
##    if t * 1000 > 1:
##        return '{:.1f}ms'.format(t * 1000)
##    if t * 1000000 > 1:
##        return '{:.1f}{:}s'.format(t * 1000000, u'\u03BC')
##    return '<1{:}s'.format(u'\u03BC')
##
##start = time.time()
##ss_list = []
##with open('users_5000000.csv', 'r') as file:
##    while file.readline() != '':
##        fields = file.readline().strip().split(',', 1)
##        ss_list.append(UserInfo(fields[0], fields[1]))
##
##print("Store:", format_time(time.time()-start))
##
##start = time.time()
##'ZZZZZZZZZZZZZZZZ' in ss_list
##print("Search:", format_time(time.time()-start))
##
##start = time.time()
##bs_list = []
##
##with open('users_5000000.csv', 'r') as file:
##    while file.readline() != '':
##        fields = file.readline().strip().split(',', 1)
##        bs_list.append(UserInfo(fields[0], fields[1]))
##
##bs_list.sort()
##print("Store:", format_time(time.time()-start))
##
##def binarySearch(alist, item):
##    first = 0
##    last = len(alist)-1
##    found = False
##
##    while first <= last and not found:
##        midpoint = (first + last)//2
##        if alist[midpoint] == item:
##            found = True
##        else:
##            if item < alist[midpoint]:
##                last = midpoint-1
##            else:
##                first = midpoint+1
##
##    return found
##
##start = time.time()    
##binarySearch(bs_list, 'ZZZZZZZZZZZZZZZZZZ')
##print("Search:", format_time(time.time()-start))
##
##start = time.time()
##tree = BinarySearchTree()
##
##with open('users_5000000.csv', 'r') as file:
##    while file.readline() != '':
##        fields = file.readline().strip().split(',', 1)
##        tree.insert(UserInfo(fields[0], fields[1]))
##        
##print("Store:", format_time(time.time()-start))
##
##start = time.time()
##'zzzzzzzzzzzzzzzzzzzzzzz' in tree
##print("Search:", format_time(time.time()-start))
##
##print('height:', tree.height(tree.root))

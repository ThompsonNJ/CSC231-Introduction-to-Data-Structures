from lab_test import LabTest
from priority_queue import *

mylab = Queue()

lab1 = LabTest('Joe Schmoe', 5, 'cbc')
lab2 = LabTest('Hunky Dory', 10, 'ccccc')
lab3 = LabTest('Willifred Nurtz', 1, 'asd')
##print(lab1)
##print(lab2)
##print(lab3)

mylab.enqueue(lab1)
mylab.enqueue(lab2)
mylab.enqueue(lab3)

mylab.dequeue()
mylab.dequeue()
mylab.dequeue()

##with open('lab-orders.csv', 'r') as file:
##    for line in file.readline().strip():
##        lab = LabTest(line)






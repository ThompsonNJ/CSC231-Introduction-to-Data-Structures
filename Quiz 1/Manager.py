#
# This file provides instructions for what to do, and will help you test code.
#
# Complete Steps 1-8 below IN ORDER. Successfully completing each step will earn you more points.
#
# Uncomment the code at each step, then rerun this file to test your progress. Move on to the next step ONLY when
# the test code for the current step runs without errors.
#

from WaitingRoom import *

# 1. Create a file called WaitingRoom.py in the same directory as this script. Define the WaitingRoom class in
# the WaitingRoom.py file. Implement the class constructor for WaitingRoom to initialize an empty list that
# will eventually contain a list of patient names.
queue = WaitingRoom()



# 2. Implement a method add(name) in your class. The method adds 'name' (a string) to the END of the list. Your method
# must not return or print anything.
queue.add('Joe Smith')
queue.add('Slim Pickens')
queue.add('Martha Washington')



# 3. Implement the method is_empty(), which RETURNS True if the waiting list is empty, and False otherwise. Your method
# must not print anything.
print('is_empty should be False:', queue.is_empty())
queue = WaitingRoom()
print('is_empty should be True:', queue.is_empty())



# 4. Implement the size() method, which RETURNS the number of items in the waiting list. Your method must not print
# anything.
queue = WaitingRoom()
print('Waiting list size should be 0:', queue.size())
queue.add('Joe Smith')
queue.add('Slim Pickens')
queue.add('Martha Washington')
print('Waiting list size should be 3:', queue.size())



# 5. Implement the method display(), which prints the patient's position in line and their name.  The position
# counter starts at 1. For example:
#       1 Joe Smith
#       2 Slim Pickens
#       3 Martha Washington
queue.display()



# 6. Implement the read_from_file(filename) method. This method reads names from the specified filename, which
# contains one name on each line. This method must not return or print anything.
#   - The list of names from the file should REPLACE the existing patient list.
#   - You need to remove newline characters from the names
#   - The file is guaranteed to be there, so don't worry about error checking the filename.
queue.read_from_file('patients.txt')
queue.display()



# 7. Implement the remove(name) method, which removes the name from the list AND Returns it. This method must not
# print anything. If the name is not in the list, this method does not change the list and must return None.
queue = WaitingRoom()
queue.add('Roma Corbett')
print(queue.remove('Roma Corbett'), 'removed.')
print('queue.remove() should return None:', queue.remove('Nymphadora Tonks'))



# 8. Implement position(name), which RETURNS the position of the patient with 'name' in the list. The patient in the
# first position (head of the list) should return 1. If the patient is not in the list, return None. Your method must
# not print anything.
queue.add('Roma Corbett')
queue.add('Pasty Kent')
queue.add('Burt Brand')
queue.add('Dolores Cotton')
queue.add('Quinn Finley')

patient = 'Dolores Cotton'
print(patient, 'should be in position 4. Her position:', queue.position(patient))
not_in_list = 'Sidney Crosby'
print(not_in_list, 'is not in the list. Position should be None:', queue.position(not_in_list))



# # EC1. Override the __str__ method, which RETURNS a string representation of the waitlist for printing. Your method must
# # not print anything.
# #   - e.g., ['Roma Corbett', 'Pasty Kent', 'Burt Brand', 'Dolores Cotton', 'Quinn Finley']
# print(queue)
#
#
#
# # EC2. Override the __eq__ method, which RETURNS True when two WaitingRooms are equal, and False otherwise.
# # Two WaitingRooms are equal when they have the same length and the same string values in each position of the list.
# # Your method must not print anything.
# queue_1 = WaitingRoom()
# queue_1.add('Roma Corbett')
# queue_1.add('Pasty Kent')
# queue_1.add('Burt Brand')
# queue_1.add('Dolores Cotton')
# queue_1.add('Quinn Finley')
#
# queue_2 = WaitingRoom()
# queue_2.add('Roma Corbett')
# queue_2.add('Pasty Kent')
# queue_2.add('Burt Brand')
# queue_2.add('Dolores Cotton')
# queue_2.add('Quinn Finley')
#
# print('These two waitlists should be equal. queue_1 == queue_2:', queue_1 == queue_2)
# queue_2.remove('Roma Corbett')
# print('These two waitlists should not be equal. queue_1 == queue_2:', queue_1 == queue_2)
# print('These two objects should not be equal. queue_1 == \'Snuffleupagus\'', queue_1 == 'Snuffleupagus')

# Add item to a_list in the appropriate slot. Items must be in ascending order.
def add_in_order(a_list, item):
    i = 0
    while i < len(a_list) and a_list[i] < item:
        i += 1
    a_list.insert(i, item)  


# Add item to a_list in the appropriate slot. Items must be in ascending order.
# item is a string of the form '<priority>_<first name> <last_name>', e.g., '5_James Joyce'
# items with a higher number before the underscore _ must appear closer to index len(a_list-1)
# items with the same priority appear in the order they are added with the most recently added closer to index 0
def add_in_order_from_string(a_list, item):
    temp_item = int(''.join(x for x in item if x.isdigit()))
    i = 0
    while i < len(a_list):
        temp_a_list = int(''.join(y for y in a_list[i] if y.isdigit()))
        if temp_a_list > temp_item:
            break
        i += 1
    a_list.insert(i, item)


# Part 1: Finish implementing add_in_order() so that sorted_nums is sorted when it is printed
nums = [7, 1, 5, 6, 5, 8, 4, 2, 2, 9]
sorted_nums = []
for num in nums:
    add_in_order(sorted_nums, num)
print(sorted_nums)


# Part 2: Finish implementing add_in_order_from_string() so that sorted_names is sorted when it is printed
names = ['7_Roland Purkett', '1_Harold Flaum', '5_Andree Gateley', '6_Palma Fergerson', '5_Nichole Rudzik', '8_Blake Goos', '4_Jennell Maese', '2_Mallory Blaich', '2_Laverne Gowens', '9_Sanjuanita Petramale']
sorted_names = []
for name in names:
    add_in_order_from_string(sorted_names, name)
print(sorted_names)

sorted_names = []

# Part 3: Write code below this space to read names from priority_customers.txt (same format as Part 2) and add them to
# a list in order using the add_in_order_srom_string() function

with open('priority_customers.txt', 'r') as file:
    names = []
    for line in file:
        print(line)
        add_in_order_from_string(names, line.strip())

print(names)



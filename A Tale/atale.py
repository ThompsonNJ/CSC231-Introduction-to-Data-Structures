with open("ATale.txt", 'r') as file:
    List_lines = file.readlines()

[print(x) for x in List_lines]

print("\n"+List_lines[9])

'''This program computes the count, average, min, max, and median for the files provided.'''

# MAIN
def fileSelection():
    '''This function serves as a file selection menu.'''    
    filedict = {1 : "numbers.txt"}
    for n in range(2,6):
        filedict[n] = "numbers{}.txt".format(n)

    print("===============================\n"
        "Main Menu")
    for i in sorted(filedict):
        print("{} - {}".format(i, filedict[i]))
    print("{} - EXIT".format(len(filedict)+1))
    
    print("===============================\n")

    while True:
        try:
            selection = int(input("Please make a selection: "))
            if selection in filedict:
                return filedict[selection]
            elif selection == len(filedict)+1:
                raise SystemExit
            
            else:
                print("**Invalid Entry!")
                
        except ValueError:
            print("**Invalid Entry!")


# OUTPUTS
def outputs(selection):
    '''This function takes the file selected from fileSelection() and
    calculates the count, average, min, max, and median'''
    added = 0
    converted = []
    
    # opens file, strips new line char, and converts str to int
    with open(selection, 'r') as file:
        converted = [int(line.strip()) for line in file]

    # sum of integers
    for i in converted:
        added += i        

    # changes for output
    converted.sort()
    length = len(converted)
    mean = added / length
    low = converted[0]
    high = converted[-1]

    # calc median
    middle = length // 2
    if length % 2 != 0:
        median = converted[middle]

    else:
        median = ((converted[middle]+converted[middle-1]) / 2)

    # output
    print("\nCount: {}".format(length))
    print("Average: {}".format(mean))
    print("Min: {}".format(low))
    print("Max: {}".format(high))
    print("Median: {}\n".format(median))


# TERMINATE
def terminate():
    '''This function serves the main loop for the program by calling fileSelection() and outputs(selection)'''
    selection = fileSelection()
    outputs(selection)
    while True:
        try:
            cont = input("Would you like to read another file? y/n: ")
            if cont == 'y':            
                selection = fileSelection()
                outputs(selection)
                
            elif cont == 'n':
                raise SystemExit
            
            else:
                print("**Invalid Entry!")
                
        except ValueError:
            print("**Invalid Entry!")
            terminate()


terminate()

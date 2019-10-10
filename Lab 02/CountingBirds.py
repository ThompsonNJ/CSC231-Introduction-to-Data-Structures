bird_dict = {}
count = 0


with open('bird_observations_large.txt', 'r') as rfile:
    line = rfile.readline().strip()
    while line != '':
        if line not in bird_dict:
            count += 1
            bird_dict[line] = count

        else:
            count = bird_dict[line] + 1
            bird_dict[line] = count

        line = rfile.readline().strip()
        count = 0
        

sorted_bird_list = sorted(bird_dict.items())


with open('bird_observations_large.csv', 'w') as wfile:
    for line in sorted_bird_list:
        wfile.write('{}, {}\n'.format(line[0],line[1]))


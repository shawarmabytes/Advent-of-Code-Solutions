#Day 2 - Advent of Code 2021

def part1():
    with open ('input2.txt') as f:
        lines = f.readlines()

    #print(type(lines[2][-2]))
    #print(lines[0][0])

    #this block of code separates the commands and the numbers
    numbers = []
    commands = []
    for i in range(0, len(lines)):
        numbers.append(lines[i][-2])
        commands.append(lines[i][0])

    # convert the whole list into integers
    numbers = list(map(int, numbers))

    #horizontal position counter
    horizontal = 0
    #depth position counter
    depth = 0

    #this block of code scans the commands list and increases horizontal or increases/decreases depth 
    for i in range(0,len(commands)):
        if commands[i] == 'f':
            horizontal += numbers[i]
        if commands[i] == 'u':
            depth -= numbers[i]
        if commands[i] == 'd':
            depth += numbers[i]

    #answer
    multiply = horizontal*depth

    print("Part 1 Answer:", multiply)


def part2():
    with open ('input2.txt') as f:
        lines = f.readlines()

    #print(type(lines[2][-2]))
    #print(lines[0][0])

    #this block of code separates the commands and the numbers
    numbers = []
    commands = []
    for i in range(0, len(lines)):
        numbers.append(lines[i][-2])
        commands.append(lines[i][0])

    # convert the whole list into integers
    numbers = list(map(int, numbers))

    #horizontal position counter
    horizontal = 0
    #depth position counter
    depth = 0
    #aim counter
    aim = 0

    #sample input
    '''
    commands = ['f','d','f','u','d','f'] 
    numbers = [5, 5, 8, 3, 8, 2]
    '''

    #this block of code scans the commands list and increases horizontal or increases/decreases depth 
    for i in range(0,len(commands)):
        if commands[i] == 'f':
            horizontal += numbers[i]
            depth += numbers[i]*aim #the plus sign was crucial because without it, every forward iteration replaces the depth instead of adding to it
        if commands[i] == 'u':
            #depth -= numbers[i] #turns out up command doesn't change depth for part 2
            aim -= numbers[i]
        if commands[i] == 'd':
            #depth += numbers[i] #turns out down command doesn't change depth for part 2
            aim += numbers[i]
        #logs for easy debugging
        print("horizontal: ",horizontal,"|", "aim: ",aim,"|","depth: ",depth)

    #answer
    multiply = horizontal*depth

    print("Part 2 Answer:", multiply)

part1()
part2()
    
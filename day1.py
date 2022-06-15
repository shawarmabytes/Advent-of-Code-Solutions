#Day 1 - Advent of Code 2021

def part1():

    with open ('input1.txt') as f:
        lines = f.readlines()

    #convert str list to int list for comparison    
    for i in range(0, len(lines)):
        lines[i] = int(lines[i])

    #counter for counting the number of measurements larger than the previous measurement
    count = 0 
    try:
        for i in range(0,len(lines)):
            if lines[i+1] > lines[i]:
                count +=1
    except IndexError:
        pass

    print("Part 1 Answer:",count)

def part2():
    with open ('input1.txt') as f:
        lines = f.readlines()

    #convert str list to int list for comparison    
    for i in range(0, len(lines)):
        lines[i] = int(lines[i])

    #makes a list containing three-measurement sums
    try:
        three = []
        for i in range(0,len(lines)):
            three.append(lines[i]+lines[i+1]+lines[i+2])
    except IndexError:
        pass

    #print(three)

    #counter for counting number of sums are larger than the previous sum
    count = 0 
    try:
        for i in range(0,len(three)):
            if three[i+1] > three[i]:
                count +=1
    except IndexError:
        pass
    
    print("Part 2 Answer:",count)

part1()
part2()
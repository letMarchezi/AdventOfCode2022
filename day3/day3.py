# Advent of Code 2022 solutions
# day 3
inFile = "input.txt"
with open(inFile,'r') as i:
    lines = i.readlines()
    
# steps:
# split string using spaces and \n
lines_proc = [x.split() for x in lines]

print(lines_proc)
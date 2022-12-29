# Advent of Code 2022 solutions
# day 3
inFile = "input.txt"
with open(inFile,'r') as i:
    lines = i.readlines()
    
# steps:
# split string using spaces and \n
lines_proc = [x.split()[0] for x in lines]

priority = lambda x: ord(x)-96 if x.islower() else ord(x)-38

def countOcurrences(line):
    half = len(line)//2
    occurences = {}
    for index,char in enumerate(line):
        if(index<=half):
            occurences[char] = line.count(char,half)
        else:
            occurences[char] = line.count(char,0,half) 
        if(occurences[char]): 
            result = char
    return priority(result)

priorities = [countOcurrences(x) for x in lines_proc]
print(sum(priorities))
# Advent of Code 2022 solutions
# day 2
inFile = "input.txt"
with open(inFile,'r') as i:
    lines = i.readlines()
    
# steps:
# split string using spaces and \n
lines_proc = [x.split() for x in lines]
#print(lines_proc)

# switching letters to score points
shapes = lambda x: 1 if x=='X' or x=='A' else 2 if x=='Y' or x=='B' else 3
scores = [[shapes(x[0]),shapes(x[1])] for x in lines_proc]

# comparing winners in every round
def matchResult(round):
    match round:
        case [1,1] | [2,2] | [3,3]:
            return 3
        case [1,2] | [2,3] | [3,1]:
            return 6
        case [1,3] | [3,2] | [2,1]:
            return 0
results = [matchResult(x) for x in scores]
# sum scores
me = [x[1] for x in scores]
total = sum(results) + sum(me)
print(total)

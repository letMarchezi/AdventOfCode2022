# Advent of Code 2022 solutions
# day 2 part 2
inFile = "input.txt"
with open(inFile,'r') as i:
    lines = i.readlines()
    
# split string using spaces and \n
lines_proc = [x.split() for x in lines]

# switching letters from opponent to score points
shapes = lambda x: 1 if x=='A' else 2 if x=='B' else 3 if x=='C' else x
scores = [[shapes(x[0]), shapes(x[1])] for x in lines_proc]

# X: Defeat
# Y: Draw
# Z: Victory

# A - 1: Rock
# B - 2: Paper
# C - 3: Scissors

# Receives the opponent play and the final result
# Returns the score of the chosen 
def matchShape(round):
    match round:
        case [1,'Y'] | [2,'X'] | [3,'Z']:
            return 1
        case [2,'Y'] | [3,'X'] | [1,'Z']:
            return 2
        case [3,'Y'] | [1,'X'] | [2,'Z']:
            return 3
score_shape = [matchShape(x) for x in scores]

result = lambda x: 0 if x=='X' else 3 if x=='Y' else 6
score_turn = [result(x[1]) for x in lines_proc]

score_total = sum(score_shape) + sum(score_turn)
print(score_total)

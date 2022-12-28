# Advent of Code 2022 solutions
# day 1
inFile = "input.txt"
with open(inFile,'r') as i:
    lines = i.readlines()
    
lines_proc = [x.split("\n",1)[0] for x in lines]

def forloop(inputs):
    j=0
    sums=[0]
    for i in inputs:
        if i == '':
            j+=1
            sums.append(0)
        else:
            sums[j] += int(i)
    return sums     

sorted_calories = sorted(forloop(lines_proc), reverse=True)

# Answer part 1:
print(sorted_calories[0])

# Answer part 2:
print(sum(sorted_calories[0:3]))
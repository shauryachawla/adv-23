f = open("./inputs/input1-1.txt")

sum = 0

for line in f:
    digits = []
    for i, c in enumerate(line):
        if(c.isdigit()): 
            digits.append(int(c))
        for j, val in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
            if(line[i:].startswith(val)): 
                digits.append(j+1)
    sum += int(str(digits[0]) + "" + str(digits[-1]))
    
print(sum)
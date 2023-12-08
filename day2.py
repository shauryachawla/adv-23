
red = 12
blue = 14
green = 13

f = open("inputs/input2-1.txt")

sum = 0

for i, line in enumerate(f, 1): 
    ok = True
    line = line.split(":")[1]
    for event in line.split(";"):
        for balls in event.split(","):
            n,color = balls.split()
            match color:
                case 'red':
                    if(int(n)>red): 
                        ok = False  
                case 'green':
                    if(int(n)>green): 
                        ok = False
                case 'blue':
                    if(int(n)>blue): 
                        ok = False
    if(ok == True): 
        sum += i
    
print(sum)
                
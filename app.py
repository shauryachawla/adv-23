f = open("./inputs/input1-1.txt", "r")

sum = 0

for line in f:
    digits = [x for x in line if x.isdigit()]
    cal_value = int(digits[0] + "" + digits[-1])
    sum += cal_value

print(sum)
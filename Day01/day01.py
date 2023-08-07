with open('Day01/adventofcode.com_2022_day_1_input.txt', 'r') as f:
    line=f.readlines()

cal=[]
sumcal=0

for l in line:
    if l !='\n':
        sumcal += int(l.replace('\n',''))
        cal.append(sumcal)
    else:
        sumcal=0
        cal.append(sumcal)
print(sorted(cal)[-1])

# part 2
print(sum(sorted(cal)[-3:]))
import string

#part1
lowercase=dict(zip(string.ascii_lowercase, range(1,27)))
uppercase=dict(zip(string.ascii_uppercase, range(27, 53)))

allcase={**lowercase, **uppercase}


with open('Day03/adventofcode.com_2022_day_3_input.txt', 'r') as f:
    line=f.readlines()

common=[]

for l in line:
    l=repr(l.strip()).replace("'","")
    length=len(l)
    first=l[:(length//2)]
    second=l[(length//2):]

    for letter in first:
        if letter in second:
            common.append(allcase[letter])
            break

#print(sum(common))

#part2

newline=[repr(l.strip()).replace("'","") for l in line]
comb_line=[newline[i-2]+'\\'+newline[i-1]+'\\'+newline[i] for i in range(2, len(newline), 3)]

common_comb=[]
for n in comb_line:
    one=n.split('\\')[0]
    two=n.split('\\')[1]
    three=n.split('\\')[2]

    for chr in one:
        if chr in two and chr in three:
            common_comb.append(allcase[chr])
            break


print(sum(common_comb))



    

        




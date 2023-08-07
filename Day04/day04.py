with open('Day04/adventofcode.com_2022_day_4_input.txt', 'r') as f:
    line=f.readlines()

sum_ful=0
sum_lap=0
for l in line:
    first_1=l.replace('\n','').split(',')[0].split('-')[0]
    first_2=l.replace('\n','').split(',')[0].split('-')[1]
    second_1=l.replace('\n','').split(',')[1].split('-')[0]
    second_2=l.replace('\n','').split(',')[1].split('-')[1]

    range_1=list(range(int(first_1), int(first_2)+1))
    range_2=list(range(int(second_1), int(second_2)+1))

    if list(set(range_1)-set(range_2))==[] or list(set(range_2)-set(range_1))==[]:
        sum_ful+=1
    
    for flr in range_1:
        if flr in range_2:
            sum_lap+=1
            break
    
print(sum_ful)
print(sum_lap)


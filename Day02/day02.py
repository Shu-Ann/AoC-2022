# rock:1 paper:2 scissors:3
# won:6 draw:3 lost:0

oppdic={'A':1, 'B':2, 'C':3}
mydic={'X':1, 'Y':2, 'Z':3}

#my-opp
win=[1, -2]
lost=[2,-1]

with open('Day02/adventofcode.com_2022_day_2_input.txt', 'r') as f:
    line=f.readlines()   

score=0

for l in line:
    opp=oppdic[l.replace('\n','').split(' ')[0]]
    my=mydic[l.replace('\n','').split(' ')[1]]
    if my-opp in win:
        total=6+my
        score+=total
    elif my-opp==0:
        total=my+3
        score+=total
    elif my-opp in lost:
        score+=my

print(score)

#part 2

# X:lose Y:draw Z:win
win_guide={'A':2, 'B':3, 'C':1}
lose_guide={'A':3,'B':1,'C':2}

new_score=0
for s in line:
    opp=oppdic[s.replace('\n','').split(' ')[0]]
    opp_rep=s.replace('\n','').split(' ')[0]
    my_rep=s.replace('\n','').split(' ')[1]
    if my_rep=='X': #lose
        total=0+lose_guide[opp_rep]
        new_score+=total
    elif my_rep=='Y': #draw
        total=opp+3
        new_score+=total
    elif my_rep=='Z': #win
        total=6+win_guide[opp_rep]
        new_score+=total

print(new_score)

    











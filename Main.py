
x=[]
#each line is saved
with open('data.txt') as f:
    lines = [line.rstrip() for line in f]

#converting sequences to color names

for line in lines:
    if line=="0,0,1,0":
        x.append('green')
    elif line=="1,0,0,0":
        x.append('red')
    elif line=="0,0,0,1":
        x.append('arrow')
    elif line=="0,1,0,0":
        x.append('yellow')
    elif line=="0,0,0,0":
        x.append('no')
    else:
        print("not correct sequence ")
        

#print(x)
    
for i in range(len(x)-1):
    
    current=x[i]
    later=x[i+1]
    print("current:",current)
    print("next:",later)
    
    if current=="green" and (later=='green' or later=='yellow' or later=='no'):
        
            continue

    elif current=="red" and (later=='yellow'or  later=='red' or later=='no'):
        
            continue

    elif current=="yellow" and (later=='green'or  later=='arrow'or later=='no' or later=='yellow'):
        
            continue
    elif current=='no':
        continue

    else:
        print("breaking")
        break
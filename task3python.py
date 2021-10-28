from math import sqrt
def om(x=0,y=0):
    listt=[]
    for i in range(x,y+1):
        z=sqrt(i)
        if z%1==0:
            listt.append(i)
    return listt
x=int(input ())
y=int (input())
print(om(x,y))


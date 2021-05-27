n=int(input('Enter a number '))
i=0
j=1
while(j<n):
    print(j,end=',')
    k=j+i
    i=j
    j=k
    
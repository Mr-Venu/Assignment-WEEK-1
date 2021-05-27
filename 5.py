a=[1,-3,5,-9,14,-8]
n,s1,s2=0,0,0
while n<len(a):
    if a[n]>0:
        s1=s1+a[n]
    else:
        s2=s2+a[n]
    n=n+1
 
if s1>-(s2):
    print('POSITIVE')
else:
    print('NEGATIVE')
     



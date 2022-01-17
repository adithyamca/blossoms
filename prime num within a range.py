n=int(input("enter 1st limit"))
m=int(input("eneter 2nd limit"))

while(n<=m):
    i=1
    c=0
    while(i<=n):
        
        if(n%i==0):
            c=c+1
        i=i+1

    if(c==2):
            print(n)
    n=n+1

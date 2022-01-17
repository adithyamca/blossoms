x=int(input("enter the nmber"))
a=0
b=1
c=a+b
print(a)

for i in range(1,x+1,1):
    print(c)
    c=a+b
    a=b
    b=c
 


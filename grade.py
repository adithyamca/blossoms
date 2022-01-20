m1=int(input("enter the mark 1"))
m2=int(input("enter the mark 2"))
m3=int(input("enter the mark 3"))
m4=int(input("enter the mark 4"))
m5=int(input("enter the mark 5"))
sum=m1+m2+m3+m4+m5
print("sum= ",sum)
avg=(m1+m2+m3+m4+m5)/5
print("average=",avg)
if avg>80:
    print("A GRADE")
elif avg>=70:
    print("B GRADE")
elif avg>=50:
    print("C GRADE")
elif avg>=40:
    print("D GRADE")
else:
    print("failed")

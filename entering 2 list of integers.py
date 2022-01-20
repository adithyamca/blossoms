a=[1,2,3,4,5]
b=[5,7,8,9,10]
sum1=sum2=0
if len(a)==len(b):
    print("the two lists are equal")
elif len(a)> len(b):
    print("length of a is greater")
elif len(b)> len(a):
    print("length of b is greater")
for i in a:
    sum1+=i
print("the first list sum is: ",sum1)
for j in b:
    sum2+=j
print("the second list sum is: ",sum2)
if(sum1==sum2):
    print("sums are equal")
else:
    print("sums are not equal")
for i in a:
    for j in b:
        if i==j:
            print(j, " is common")
    

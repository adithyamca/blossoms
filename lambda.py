h=int(input("enter the value of height"))
b=int(input("enter the value of base"))
triangle=lambda h,b:(.5*h*b)
print("area of a triangle:",triangle(h,b))
a=int(input("enter the value of square side"))
square=lambda a:(a*a)
print("area of a square:",square(a))
b=int(input("enter the value of base"))
l=int(input("enter the value of length"))
rectangle=lambda b,l:(l*b)
print("area of a rectangle: ",rectangle(l,b))

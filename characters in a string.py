Str=list(input("enter a string")) 
for i in Str:
    if(i!="#"):
        
        
        c=0
        for j in range (0,len(Str)):
            
             if (i==Str[j]):
                 c=c+1
                 Str[j]="#"
        print(i,"=",c)
      

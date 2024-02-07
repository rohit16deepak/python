a=int(input())
rev=0
i=0
while i<3:
    z=a%10
    rev= (rev*10)+z
    z=0
    a=a//10
    i+=1
    
print(rev)


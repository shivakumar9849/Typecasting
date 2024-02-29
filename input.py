n=int(input())
c=0
print(n)
while n!=0:
    d=n%10
    c+=1
    if d==7 or n%7==0:
        print('Buzz number')
    else:
        print('not a Buzz number')
    n=n//10
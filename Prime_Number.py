n=int(input('Enter number :'))
fact=True
if n<=1 :
    fact=False
else:
    for i in range(2,n):
        if n%i==0:
            fact=False
            break
if fact:
    print('It is a prime number')
else:
    print('It is not a prime number')                 
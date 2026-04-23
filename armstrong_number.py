n=int(input('Enter Number :'))
temp=n
i=len(str(n))
total=0
while temp>0:
    num=temp%10
    total+=num**i
    temp//=10
if total==n:
    print('it is armstrong number')
else:
    print('it is not armstrong number')    
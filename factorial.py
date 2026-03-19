num=int(input('Enter factorial number :'))
fact=1
for i in range(num,0,-1):
    fact*=i
print(f'Factorial of the number is {fact}')    
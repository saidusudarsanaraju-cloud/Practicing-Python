n=int(input('starting number :'))
end=int(input('Ending number :'))
for num in range(n,end+1):
    if num>1 :
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)        
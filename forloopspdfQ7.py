num=int(input("enter the number"))
for i in range(2,num//2):
    if num%i==0:
        print(num,"is not prime number")
        break
    else:
        print(num,"is prime number")

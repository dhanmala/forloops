n=int(input("enter the number"))
a=2
sum=0
for i in range(0,n):
    print(a,end="+")
    sum=sum+a
    a=a*10+2
print("sum of series:",sum) 
   
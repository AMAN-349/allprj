a=int(input("enter number"))
prime=True
for i in range(2,a):
    if(a%i==0):
        prime=False
        break
if prime:
    print("number is prime")
else:
    print("not prime")
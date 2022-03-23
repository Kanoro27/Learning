from re import I


n=int(input("Enter the value : "))
for i in range(1,5) :
    s=n**i #Here s is the exponential value and ** operator is exponential operator we can even use pow()
    print(n,"^",i,"=",s)
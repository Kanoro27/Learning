#code for calculating simple and compund interest   
p=float(input("Enter the Principle Amount : "))
r=float(input("Enter the Rate of Interest : "))
t=float(input("Enter the Duration in months : "))
n=int(input("Enter 1 for Simple interest \nEnter 2 for Compund interest \nChoose Your Opetion : "))
if n==1 : 
    si=0
    si=p*r*t #simple interest is given as si and si=prt
    print("Simple Interest = ",si)
elif n==2 :
    ci=0
    ci=[p*(pow(1+r,t))]-(p) #compound interest is given as ci and the formula is given as it is
    print("Compound Interest = ",ci)
else :
    print("Enter a Valid Option.")

n1=int(input("enter the first number:"))
n2=int(input("enter the second number:"))
x=n1
y=n2
while(n2!=0):
         t=n2
         n2=n1%n2
         n1=t
gcd = n1
print("GCD of {0} and {1}={2}".format(x,y,gcd))
lcm = (x*y)/gcd
print("lcm of {0} and {1}={2}".format(x,y,lcm))
       

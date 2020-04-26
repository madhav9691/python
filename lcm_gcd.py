def gcd(x,y):
    while y>0:
        x,y=y,x%y
    return(x)
def lcm(a,b):
    return(a*b)//gcd(a,b)


num1,num2=map(int,input("Enter two numbers seperated by\
space:").split())
print("GCD of given numbers= ",gcd(num1,num2))
print("LCM of given numbers= ",lcm(num1,num2))

                    
              

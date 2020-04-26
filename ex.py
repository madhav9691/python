a=int(input("Enter a :"))
b=int(input("Enter b :"))
try:
    c=a/b
    print("Division=",c)

except Exception: 
    print("You can't divide a number by zero")

print("Thank you")

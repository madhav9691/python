try:
    a=int(input("Enter a:"))
    b=int(input("Enter b:"))
    c=a/b
    print("Division =",c)
    
except ArithmeticError:
    print("you can't divide a number by zero")
except ValueError:
    print("Invalid data type entered")
except Exception:
    print("Something went wrong")
else:
    print("This is else block execution since there is no exception")
finally:
    print("Thank You,bye")
    

    

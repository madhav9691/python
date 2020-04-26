x=int(input("Enter age: "))
try:
    if x<18:
        raise ValueError("Not eligible to vote")
    
except ValueError as e:
    print("Exception raised:",e)
else:
    print("You are eligible to vote")

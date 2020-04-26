class My_Exception(Exception):
    pass

age=int(input("Enter age :"))
try:
    if age<18:
        raise My_Exception("invalid age for voting")

except My_Exception as e:
    print("User defined exception raised:",e)

else:
    print("You are eligible for voting")

finally:
    print("Thank You")

def nearly_equal(s1,s2):
    char_diff=0
    for x,y in zip(s1,s2):
        if x!=y:
            char_diff+=1
            if char_diff==2:
                break
    if char_diff==1:
        print("Strings are nearly equal")
    else:
        print("Strings are nearly not equal")

string1=input("Enter first string: ")
string2=input("Enter second string: ")
if len(string1)==len(string2):
    nearly_equal(string1,string2)
else:
    print("length of two string is not equal")

            

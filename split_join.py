s=input("Enter string: ")
print("Given String s=",s)

#usage of split()
s1=s.split()
print("After splitting s1=",s1)

#for i in s1:
 #   print(i)
 
#usage of join()    
s2="-".join(s1)
print("After joining s2=",s2)

bd="15-08-1947"
l1=['Date','Month','Year']
l2=bd.split("-")
# print(l2)
dict1={i:j for i,j in zip(l1,l2)}
print(dict1)

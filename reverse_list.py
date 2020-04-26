def reverse(l):
    n=len(l)
    print("Given list: \n",l)
#for i in range(n-1,-1,-1):
 #   print(l[i])
    l1=l[::-1]
    print("Reverse of given list\n",l1)

list1=[]
n=int(input("Enter range: "))
print("Enter elements")
for i in range(n):
    list1.append(int(input()))
reverse(list1)

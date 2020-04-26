def dups_and_unique(list2):
   n=len(list2)
   dup_list=[]
   unique_list=[]
   for i in range(n):
    for j in range(i+1,n):
     if list2[i]==list2[j] and \   #line continuation
                    list2[i] not in dup_list:
               dup_list.append(list2[i])
   if len(dup_list)>0:
     print("list of Duplicate elements")
     print(dup_list)
     print("list of unique elements")
     for i in list2:
        if i not in dup_list:
           unique_list.append(i)
     print(unique_list)
   else:
       print("There are no duplicate elements in the list")
       print("list of unique elements")
       print(list2)

list1=[]
n=int(input("Enter range: "))
print("enter elements of list:")
for i in range(n):
    element=list1.append(int(input()))
dups_and_unique(list1)
    
    
      

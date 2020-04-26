def unique(list2):
       n=len(list2)
       unique_list=[]
       list3=[]
       list4=[]
       for i in range(n):
           flag=0
           for j in range(i+1,n):
               if list2[i]==list2[j] and \
                           list2[i] not in list3:
                   list3.append(list2[i])
                   break
       for i in list3:
           if i not in list2:
               list4.append(i)
       print(list4)

list1=[]
n=int(input("Enter range: "))
print("Enter numbers of list")
for i in range(n):
    list1.append(int(input()))
unique(list1)
    
      

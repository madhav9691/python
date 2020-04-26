def dups_list():
    l1=[]
    n= int(input("enter list size"))
    print("Enter the elements")
    for i in range(n):
        ele=input()
        l1.append(ele)
    l2=[]
    l3=[]
    l4=[]
    print("given list",l1)
    for i in l1:
        #print("given list",i)
        if i in l2:
            l3.append(i)
            print("Duplicate elements",l3)
           # print("Duplicates",l3)
        else:
             
             l2.append(i)
        
    
    for i in l2:
            if i not in l3:
                l4.append(i)
    print("unique elements:",l4)
    #print(l3)

dups_list()


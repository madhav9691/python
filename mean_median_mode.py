l=[]
n=int(input("enter range of list:"))
print("Enter elements:")
s=0
for i in range(n):
    element=int(input())
    l.append(element)
    s+=element
print("Given list =",l)

# finding mean 
mean=s/n
print("Mean of the list =",mean)

# finding median
l.sort()
print("Sorted list=",l)
if n%2!=0:
    median=l[n//2]
else:
    median=(l[n//2]+l[n//2-1])/2
print("median of the list =",median)

#finding mode
d={i:l.count(i) for i in l}
print(d)
mode_list=[]
big=2
for i in d.keys():
    if d[i]==big:
        mode_list.append(i)
        big=d[i]
    elif d[i]>big:
        mode_list=[i]
        big=d[i]
if len(mode_list)>0:
    print("list of mode values:")
    for i in mode_list:
         print(i)
else:
    print("There is no mode in the list")







        













      

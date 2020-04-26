s1=set()
s2=set()
m=int(input("Enter range of set1: "))
print("Enter elements of set1:")
for i in range(m):
    e=int(input())
    s1.add(e)

n=int(input("Enter range of set2: "))
print("Enter elements of set2:")
for i in range(n):
    e=int(input())
    s2.add(e)
print("set1=",s1,"set2=",s2)
print("Union of s1 & s2: ", s1.union(s2))
print("Intersection of s1 & s2: ", s1.intersection(s2))
print("Difference of s1 & s2: ", s1.difference(s2))
print("symmetric difference of s1 &s2: ", s1^s2)

    

d={}
s=input("enter string:")
for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print("Dictionary Structure=",d)


'''d={i:s.count(i) for i in s}
print(d)'''


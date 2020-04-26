f=open("rev_file.txt","w")
print("Enter data into file")
s=input()
while(s!='end'):
    f.write(s+"\n")
    s=input()
f.close()
print("Data in the file in reverse order")
f=open("rev_file.txt","r")

l=f.readlines()
l.reverse()
for line in l:
    print(line)
f.close()

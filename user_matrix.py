def create_matrix(m,row,col):
    for i in range(row):
        m.append([])    # adding rows 
    for i in range(row):
        for j in range(col):
            m[i].append(0)   #adding columns to each row
   
def enter_elements(n,r1,c1):
    for i in range(r1):
        for j in range(c1):
            n[i][j]=int(input())
a=[]
b=[]
add=[]
r=int(input("enter no of rows: "))
c=int(input("enter no of columns: "))
create_matrix(a,r,c)
create_matrix(b,r,c)
create_matrix(add,r,c)
print("enter elements of matrix a")
enter_elements(a,r,c)
print("enter elements of matrix b")
enter_elements(b,r,c)
#addition
for i in range(r):
    for j in range(c):
        add[i][j]=a[i][j]+b[i][j]
print("addtion of two matrices")
for i in range(r):
    for j in range(c):
        print(add[i][j], end=" ")
    print()
    










'''
print("Enter elements:")
for i in range(r):
    for j in range(c):
        a[i][j]=int(input())
for k in a:
    print(k)

'''

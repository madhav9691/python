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
c=[]
r1=int(input("enter no of rows of matrix a: "))
c1=int(input("enter no of columns of matrix a: "))
r2=int(input("enter no of rows of matrix b: "))
c2=int(input("enter no of columns of matrix b: "))
if c1!=r2:
    print("matrix multiplication is not possible")
else:
    create_matrix(a,r1,c1)
    create_matrix(b,r2,c2)
    create_matrix(c,r1,c2)
    print("enter elements of matrix a")
    enter_elements(a,r1,c1)
    print("enter elements of matrix b")
    enter_elements(b,r2,c2)
#multiplication
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
              c[i][j]+=a[i][k]*b[k][j]

    print("Multiplication of two matrices")
    for i in range(r1):
        for j in range(c2):
            print(c[i][j], end=" ")
        print()

class student:
    def __init__(self,x,y):   #constructor method
        self.no=x
        self.name=y
    def display(self):
        print("No=",self.no,"Name=",self.name)

s1=student(1,'abc')
s1.display()
s2=student(2,'xyz')
s2.display()

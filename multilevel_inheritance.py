class A:
    def method1(self):
        print("I am from class A")
class B(A):
    def method2(self):
        print("I am from class B")
class C(B):
    def method3(self):
        print("I am from class C")

obj=C()
obj.method1()
obj.method2()
obj.method3()

class A:
    def method1(self):
        print("I am from class A")
class B(A):
    def method2(self):
        print("I am from class B")

obj=B()
obj.method1()
obj.method2()

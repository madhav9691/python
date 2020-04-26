class A:
    def sample(self):
        print("I am from class A")
class B(A):
    def sample(self):
        print("I am Madhav from Class B")

obj=B()
obj.sample()   #calls subclass version of sample()

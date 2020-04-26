class student:
    college_name="Aditya college"
    def __init__(self,x,y):       #instance method
        self.no=x
        self.name=y
    def display(self):
        print("no=",self.no,"name=",self.name) #instance

    @classmethod
    def get_college(cls):
        return(cls.college_name)
    @staticmethod
    def get_info():
        print("Thank you Aditya college,kakinada")

s1=student(123,'pqr')
s1.display()
print("college:",student.get_college())
student.get_info()

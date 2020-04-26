class marks_info:
    def get_marks(self,x,y,z):
        self.m1=x
        self.m2=y
        self.m3=z
        self.total=self.m1+self.m2+self.m3
    def display_marks(self):
        print("m1=",self.m1,"m2=",self.m2,"m3=",self.m3)
        print("Total marks=",self.total)
class attendance_info:
    def get_attendance(self,t_days,a_days):
        self.att_per=(a_days/t_days)*100
    def display_attendance(self):
        print("Attendance percentage=",self.att_per)

class student_info(marks_info,attendance_info):
    def __init__(self,n1,n2):
        self.no=n1
        self.name=n2
    def display_personal(self):
        print("No=",self.no,"Name=",self.name)

s=student_info(8,"MADHAVA")
s.get_marks(99,66,58)
s.get_attendance(96,91)
s.display_personal()
s.display_marks()
s.display_attendance()



        
    
    
        

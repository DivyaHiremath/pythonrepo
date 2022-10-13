#polymorphism in python
class Ise :
    def studentDetail(self,usn,name,age,marks):
        #local variables 
        self.usn =usn
        self.name=name
        self.age=age
        self.marks=marks
        print("The usn:{},name:{},age:{},marks:{}".format(self.usn,self.name,self,age,self.marks))
s1=Ise()
s1.studentDetails('is18','divya','34','32')
s2=Ise()
s2.studentDetails('is01','sham','87','88')


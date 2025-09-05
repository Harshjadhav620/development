class Employee:
    def __init__(self,empid=None,name=None,salary=None):
        self.empid=empid
        self.name=name
        self.salary=salary
    def setEmpid(self,empid):
        self.empid=empid    
    def setname(self,name):
        self.name=name 
    def setsalary(self,salary):
        self.salary=salary
    def getEmpid(self):
        return self.empid 
    def getName(self):
        return self.name 
    def getSalary(self):
        return self.salary             
    

e1=Employee()
e2=Employee(124,"Harsh",20000)
e1.setEmpid(345)
e1.setname("sagar")
e1.setsalary(25000)  

print(e1.getEmpid(),e1.getName(),e1.getSalary())
print(e2.getEmpid(),e2.getName(),e2.getSalary())
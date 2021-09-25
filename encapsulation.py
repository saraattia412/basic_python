class employee():
    def setsalary(self,salary):
        self.salary=salary
    def getsalary(self):
        return self.salary
empl_1=employee()
empl_1.setsalary(2500)
print("salary = ", empl_1.getsalary())
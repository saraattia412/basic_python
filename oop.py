x=5
print(type(x))
class myclass:
    def tesst(self):
        print('welcome')
        print(self)
thhis=myclass()
thhis.tesst()
print(thhis)
print("------------------")
class student():
    def __init__(self,name):
        self.name=name
        self.marks=[]
        print('welcome  {} to the school  '.format(name))
    def add_marks(self,mark):
        self.marks.append(mark)
    def avg(self):
        return sum(self.marks)/len(self.marks)
s1=student('sara')
print(s1.marks)
s1.add_marks(40)
s1.add_marks(50)
s1.add_marks(60)
s1.add_marks(70)
s1.add_marks(80)
s1.add_marks(90)
s1.add_marks(100)
print(s1.marks)
print(s1.avg())
print('----------------------')
class calculator():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a + self.b
    def mull(self):
        return self.a * self.b
class scientific(calculator):
    def power(self):
        return self.a ** self.b
x=scientific(2,3)
print(x.power())
print(x.add())
print(x.mull())


'''
calculator:
calc=calculator(2,3)
print(calc.add())
print(calc.mull())
'''
print('-------------------------------')




def printstr(str) :
    "this is a function to print string"
    print(str)
    return
printstr('sara atia')
def summ(x,y):
    print(x+y)
    return
summ(2,5)
def printme(name,age=1):
    print("name :", name)
    print("age :", age)
    return
printme('sara',20)
printme('dima')
def printnum(arg,*vartuble):
    print('output')
    print(arg)
    for var in vartuble:
        print(var)
    return
printnum(10)
printnum(70,60,50)
summm=lambda arg1,arg2 :arg1+arg2
print("total : ",summm(10,2))



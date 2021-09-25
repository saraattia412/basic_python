'''x=0
while x<10 :
    print(x)
    x += 1
else:
    print('x>=10')
'''
x=0
while x<10 : print(x) ; x += 1

x=0
while x<5 :
    y=0
    while y<3 :
        print(x,y)
        y +=1
    x += 1
for letter in 'python' :
    print(letter)
for x in 'python' :
    print(x)
    print('-----------------------------------------------')
    for y in 'sara' :
        print(y)
        print('------')
a=0
b=0
while a<4 :
    a=a+1
    b=0
    while b<4 :
        b=b+1
        print(a,b)
for a in range(1,5) :
    for b in range(1,5) :
        print(a,b)

print(list(range(20)))
for letter in 'python' :
    if letter == 'h' :
        break
    print('current leetter',letter)
var=10
while var>0 :
    print('current var vahue',var)
    var=var-1
    if var == 5 :
        break
print('end')
for letter in 'python':
    if letter=='h':
        continue
    print(letter)
#example 1 :
print("number  \t  square")
print("------------------------------------")
for i in range(1,11,1):
    square=i*i#square=i**2
    print(i,  '\t' ,'\t' ,'\t',square)

#example 1 :
print('---------------------------------------')
start=int(input('enter the start number :'))
end=int(input('enter the end number :'))
print("number     square")
print("------------------------------------")
for i in range(start,end+1):
    square=i*i#square=i**2
    print(i,  '\t','\t' ,square)
print('-------------------------------------------')
#example 2 :
rows=int(input('entre rows :'))
cols=int(input('enter cols :'))
for r in range(rows) :
    for c in range(cols) :
        print('*' , end=' ')
    print()

print('-----------------------------------------')
#example 3 :
for r in range(8) :
    for c in range(r+1) :
        print('*' , end=' ')
    print()
print('---------------------------------------------')
list_of_lists=[[1,2,3],[4,5,6],[7,8,9]]
for list in list_of_lists:
    for x in list:
        print(x)
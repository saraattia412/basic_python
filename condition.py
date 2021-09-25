x=5
if x==5 :
    print(x)

name='sara'
age=20
if name=='sara' and age==20 :
    print('your name is sara , and your are also 20 years old')

if name=='sara' or name=='aya' :
    print('your name is either sara or aya')

username='sara atia'
password='12345'
if username=='sara atia' and password=='12345' :
    print('login success ,welcome sara' )
y=500
if y>600 :
    print('y is bigger than 600')
else:
    print('y is smalle than 600')
x=100
if x==100 :
    print('x=100')
elif x==200 :
    print('x=200')
else:
    print('x=0')
x=100
if x<200 :
    print('value less than 200')
    if x==150 :
        print('which is 150')
    elif x==100 :
        print('which is 100')
    elif x==50 :
        print('which is 50')
elif x<50 :
    print('value less than 50')
else:
    print('could not find true value')
print('end..')
x=5
if x==5 : print('x=5')
name='sara'
print('welcome sara') if name=='sara' else print('who are you')
#example 1
x=5
y=6
z=3
r=2
if all([x==5 , y==6 , z==3 , r==2]):
    print('done')
elif any([x==6 , y==5 , z==2 , r==3]):
    print('error')
#example 2
players ={'treka':1 , 'brakate':2 }
if 'treka' in players :
    print('found')
#example 3
a=1
b=2
if a==1 and b==2 :
    print(True)
if a==0 or b==2 :
    print(True)
if not (a==1 and b==3) :
    print(True)
if a!=0 and b!=3 :
    print(True)
#example 4
players ={'treka':1 , 'brakate':2 }
if 'sara' not in players :
    print('not found')








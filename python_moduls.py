import os
#writing
'''
file=open('1.txt','wb')
print(file.name)
print(file.closed)
print(file.mode)
'''
#read
'''
file=open('1.txt','rb')
words=file.read(10)
print(words)
'''
#position
'''
file=open('1.txt','r+')
print(file.tell())
words=file.read(10)
print(words)
position=file.tell()
print(position)
'''
#writing into text file
'''
file=open('1.txt','r+')
file.write('hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh')
file.close()
'''
#renaming file
'''
os.rename('1.txt','text.txt')
'''

print(os.getcwd())
import time
print('welcome')
time.sleep(3)
print('after 3 sec')

import calendar
print(calendar.month(2020,7))





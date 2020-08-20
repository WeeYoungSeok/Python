# -*- coding:utf-8 -*-

'''
*
**
***
****
*****
'''
a = str('*')
for i in range(0,5):
    print(a*(i+1))

print('----')

'''
*****
****
***
**
*
'''
for i in range(5,0,-1):
    print(a*(i))

print('-----')
'''
    *
   **
  ***
 ****
*****
'''
for i in range(0,5):
    print('{0:>5s}'.format(a * (i+1)))

    
print('-----')

'''
*****
 ****
  ***
   **
    *
'''
for i in range(4,-1,-1):
    print(a*(i+1))
    
print('-----')
'''
    *
   ***
  *****
 *******
*********
'''

for i in range(1, 11, 2):
    print('{0:^10s}'.format(a*i))
    
    
for i in range(5):
    print(' ' * (4 - i) + '*'*(2 * i + 1))

    
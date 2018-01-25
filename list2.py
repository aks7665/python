Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:54:40) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> list = [1,3,6,8,9,0,2,4]
>>> list
[1, 3, 6, 8, 9, 0, 2, 4]
>>> list[1:?:3]
SyntaxError: invalid syntax
>>> list[1::3]
[3, 9, 4]
>>> list[:1]
[1]
>>> list[2:]
[6, 8, 9, 0, 2, 4]
>>> list[:5]
[1, 3, 6, 8, 9]
>>> list[:2:2]
[1]
>>> list[:7:2]
[1, 6, 9, 2]
>>> list[:]
[1, 3, 6, 8, 9, 0, 2, 4]
>>> len(list)
8
>>> list[8] = 15
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    list[8] = 15
IndexError: list assignment index out of range
>>> list[7] = 15
>>> list
[1, 3, 6, 8, 9, 0, 2, 15]
>>> list.append(78)
>>> list
[1, 3, 6, 8, 9, 0, 2, 15, 78]
>>> list[-3]
2
>>> list[2:]
[6, 8, 9, 0, 2, 15, 78]
>>> nl = [[1,2,3],['a','b','c','d'],[7,8,9,4,5,6]]
>>> n1
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    n1
NameError: name 'n1' is not defined
>>> nl
[[1, 2, 3], ['a', 'b', 'c', 'd'], [7, 8, 9, 4, 5, 6]]
>>> 9 in list
True
>>> 65 in list
False
>>> m in ['amit'}
SyntaxError: invalid syntax
>>> m in ['amit']
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    m in ['amit']
NameError: name 'm' is not defined
>>> m in ['a','m','i',t'}
	  
SyntaxError: EOL while scanning string literal
>>> m in ['a','m','i','t']
	  
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    m in ['a','m','i','t']
NameError: name 'm' is not defined
>>> 'm' in ['a','m','i',t'}
	    
SyntaxError: EOL while scanning string literal
>>> m in ['a','m','i','t'}
	    
SyntaxError: invalid syntax
>>> m in ['a','m','i','t']
	    
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    m in ['a','m','i','t']
NameError: name 'm' is not defined
>>> 'm' in ['a','m','i','t']
	    
True
>>> list[1:2:6]
	    
[3]
>>> list[1:7:2]
	    
[3, 8, 0]
>>> l1 = [1,2,3,4,5,6,7,8]
	    
>>> l1
	    
[1, 2, 3, 4, 5, 6, 7, 8]
>>> l2 = [11,12,13,14]
	    
>>> l1 - l2
	    
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    l1 - l2
TypeError: unsupported operand type(s) for -: 'list' and 'list'
>>> l1 + l2
	    
[1, 2, 3, 4, 5, 6, 7, 8, 11, 12, 13, 14]
>>> l3 = l1 + l2
	    
>>> l3
	    
[1, 2, 3, 4, 5, 6, 7, 8, 11, 12, 13, 14]
>>> l3 - l2
	    
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    l3 - l2
TypeError: unsupported operand type(s) for -: 'list' and 'list'
>>> l3
	    
[1, 2, 3, 4, 5, 6, 7, 8, 11, 12, 13, 14]
>>> l2
	    
[11, 12, 13, 14]
>>> l3 -l1
	    
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    l3 -l1
TypeError: unsupported operand type(s) for -: 'list' and 'list'
>>> l3 - l1
	    
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    l3 - l1
TypeError: unsupported operand type(s) for -: 'list' and 'list'
>>> l1 + 4
	    
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    l1 + 4
TypeError: can only concatenate list (not "int") to list
>>> l1[:] + 4
	    
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    l1[:] + 4
TypeError: can only concatenate list (not "int") to list
>>> l1[:]
	    
[1, 2, 3, 4, 5, 6, 7, 8]
>>> 

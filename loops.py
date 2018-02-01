Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:54:40) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> list = [0,1,2,3,4,5,6,7,8,9]
>>> if list[0]==0;
SyntaxError: invalid syntax
>>> if list[0]==0:
	print("this no is zero")

	
this no is zero
>>> if list[0]==0:
	print("zeor")
	else
	
SyntaxError: invalid syntax
>>> if list[0]==0:
	print("zeor")
	else:
		
SyntaxError: invalid syntax
>>> if list[0]==0:
	print("zeor")

zeor
>>> if list[0]==0:
	print("zero")
	elif list[1]==1;
	
SyntaxError: invalid syntax
>>> for n in list:
	print(n)

	
0
1
2
3
4
5
6
7
8
9
>>> range(10)
range(0, 10)
>>> for n in range(10):
	
	print(n)

0
1
2
3
4
5
6
7
8
9
>>> name = "hi this amit sharma"
>>> name
'hi this amit sharma'
>>> for n in name:
	print(n)

	
h
i
 
t
h
i
s
 
a
m
i
t
 
s
h
a
r
m
a
>>> range(2, 12, 3)
range(2, 12, 3)
>>> for n in range(10):
	if n == 6:
		break
	print(n, end-',')

	
Traceback (most recent call last):
  File "<pyshell#26>", line 4, in <module>
    print(n, end-',')
NameError: name 'end' is not defined
>>> for n in range(10):
	if n == 6:
		break
	print(n, end=',')

	
0,1,2,3,4,5,
>>> for n in range(10):
	if n == 6:
		continue
	print(n)

	
0
1
2
3
4
5
7
8
9
>>> list
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list.append(10)
>>> list
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> list.insert(4,12)
>>> list
[0, 1, 2, 3, 12, 4, 5, 6, 7, 8, 9, 10]
>>> list.remove(12)
>>> list
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> list.pop(9)
9
>>> list
[0, 1, 2, 3, 4, 5, 6, 7, 8, 10]
>>> list.count(2)
1
>>> list.append(2)
>>> list
[0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 2]
>>> list.count(2)
2
>>> list.sort()
>>> list
[0, 1, 2, 2, 3, 4, 5, 6, 7, 8, 10]
>>> list.reverse()
>>> list
[10, 8, 7, 6, 5, 4, 3, 2, 2, 1, 0]
>>> list2 = list.copy()
>>> list2
[10, 8, 7, 6, 5, 4, 3, 2, 2, 1, 0]
>>> 

Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:54:40) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = 'amit'
>>> a
'amit'
>>> b = "sharma"
>>> b
'sharma'
>>> a + b
'amitsharma'
>>> a[0]
'a'
>>> a[2]
'i'
>>> a[5]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    a[5]
IndexError: string index out of range
>>> a[-1]
't'
>>> a[0]
'a'
>>> # slicing
>>> a[0:2]
'am'
>>> a[2:]
'it'
>>> b[1:5:2]
'hr'
>>> # type casting
>>> c = "12"
>>> c
'12'
>>> int(c)
12
>>> c
'12'
>>> 

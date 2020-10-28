Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> round(2.1)
2
>>> round(1.5)
2
>>> import math
>>> round(1.5)
2
>>> math.floor(1.5)
1
>>> math.ceil(2.1)
3
>>> math.sin(math.pi/2)
1.0
>>> math.sin(math.pi)
1.2246467991473532e-16
>>> math.floor(math.sin(math.pi))
0
>>> math.cos(0)
1.0
>>> math.int(cos(0))
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    math.int(cos(0))
AttributeError: module 'math' has no attribute 'int'
>>> math.acos(0)
1.5707963267948966
>>> A = "part"
>>> B = 1
>>> print(""+A+""+B)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    print(""+A+""+B)
TypeError: can only concatenate str (not "int") to str
>>> print("part"+B)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    print("part"+B)
TypeError: can only concatenate str (not "int") to str
>>> A + str(B)
'part1'
>>> "{} - {}".format(A,B)
'part - 1'
>>> 

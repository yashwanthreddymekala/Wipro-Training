Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> dict1={1:10,2:20,3:30}
>>> dict1[2]
20
>>> dict1[3]
30
>>> dict2={'a':20,'b':30,'c':50}
>>> dict2['b']
30
>>> dict.keys()
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    dict.keys()
TypeError: unbound method dict.keys() needs an argument
>>> dict1.keys()
dict_keys([1, 2, 3])
>>> dict2.keys()
dict_keys(['a', 'b', 'c'])
>>> dict2.values()
dict_values([20, 30, 50])

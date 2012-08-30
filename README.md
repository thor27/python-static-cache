python-static-cache
===================

About
-----

Simple permanent in memory cache for Methods and Functions in Python.
Usefull for methods and functions that are slow to execute but
always has the same return value for each arguments used.

There are more sofisticated cache solutions for python if you have
more complex needs. This one can be simple incorporated into your project
without needing to add any extra dependencies to it.

Example usages
--------------
```
@cache
def my_function(my_arg1, my_arg2):
    #My code goes here
```
or, if args can't be cPickled:

```
@cache(key_function=lambda my_complex_arg: my_complex_arg.unique_key)
def my_complex_function(my_complex_arg):
    #My code goes her
```
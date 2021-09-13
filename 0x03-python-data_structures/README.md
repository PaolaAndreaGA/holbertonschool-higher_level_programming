
# Python Lists Vs Tuples

In this article we will learn key differences between the List and Tuples and how to use these two data structure.

[Lists](https://www.programiz.com/python-programming/list)  and  [Tuples](https://www.programiz.com/python-programming/tuple)  store one or more objects or values in a specific order. The objects stored in a list or tuple can be of any type including the nothing type defined by the None Keyword.

Lists and Tuples are similar in most context but there are some differences which we are going to find in this article.

----------

## Syntax Differences

Syntax of list and tuple is slightly different. Lists are surrounded by square brackets  `[]`  and Tuples are surrounded by parenthesis  `()`.

#### Example 1.1: Creating List vs. Creating Tuple

```
list_num = [1,2,3,4]
tup_num = (1,2,3,4)

print(list_num)
print(tup_num)
```

Output:

[1,2,3,4]
(1,2,3,4)

Above, we defined a variable called  list_num which hold a list of numbers from  `1`  to  `4`.The list is surrounded by brackets  `[]`. Also, we defined a variable  tup_num; which contains a tuple of number from  `1`  to  `4`. The tuple is surrounded by parenthesis  `()`.

In python we have  `type()`  function which gives the type of object created.

#### Example 1.2: Find type of data structure using type() function

```
type(list_num)
type(tup_num)
```

Output:

list
tuple

----------

## Mutable List vs Immutable Tuples

List has mutable nature i.e., list can be changed or modified after its creation according to needs whereas tuple has immutable nature i.e., tuple t be changed or modified after its creation.

#### Example 2.1: Modify an item List vs. Tuple

```
list_num[2] = 5
print(list_num)

tup_num[2] = 5
```

Output:

[1,2,5,4] Traceback (most recent call last): 
 File "python", line 6, in <module> 
TypeError: 'tuple' object does not support item assignment

In above code we assigned  `5`  to  list_num  at index  `2`  and we found  `5`  at index  `2`  in output. Also, we assigned  `5`  to  tup_num  at index  `2`  and we got  `type error`. We can't modify the tuple due to its immutable nature.

Note: As the tuple is immutable these are fixed in size and list are variable in size.

----------

## Available Operations

Lists has more builtin function than that of tuple. We can use `dir([object])`  inbuilt function to get all the associated functions for list and tuple.

#### Example 3.1: List Directory

```
dir(list_num)
```

Output:

['__add__',
'__class__',
'__contains__',
'__delattr__',
'__delitem__',
'__dir__',
'__doc__',
'__eq__',
'__format__',
'__ge__',
'__getattribute__',
'__getitem__',
'__gt__',
'__hash__',
'__iadd__',
'__imul__',
'__init__',
'__init_subclass__',
'__iter__',
'__le__',
'__len__',
'__lt__',
'__mul__',
'__ne__',
'__new__',
'__reduce__',
'__reduce_ex__',
'__repr__',
'__reversed__',
'__rmul__',
'__setattr__',
'__setitem__',
'__sizeof__',
'__str__',
'__subclasshook__',
'append',
'clear',
'copy',
'count',
'extend',
'index',
'insert',
'pop',
'remove',
'reverse',
'sort']

#### Example 3.2: Tuple Directory

```
dir(tup_num)
```

Output:

['__add__',
'__class__',
'__contains__',
'__delattr__',
'__dir__',
'__doc__',
'__eq__',
'__format__',
'__ge__',
'__getattribute__',
'__getitem__',
'__getnewargs__',
'__gt__',
'__hash__',
'__init__',
'__init_subclass__',
'__iter__',
'__le__',
'__len__',
'__lt__',
'__mul__',
'__ne__',
'__new__',
'__reduce__',
'__reduce_ex__',
'__repr__',
'__rmul__',
'__setattr__',
'__sizeof__',
'__str__',
'__subclasshook__',
'count',
'index']

We can clearly see that, there are so many additional functionalities associated with a list over a tuple.We can do insert and pop operation, removing and sorting elements in the list with inbuilt functions which is not available in Tuple.

----------

## Size Comparison

Tuples operation has smaller size than that of list, which makes it a bit faster but not that much to mention about until you have a huge number of elements.

#### Example 5.1: Calculate size of List vs. Tuple

```
a= (1,2,3,4,5,6,7,8,9,0)
b= [1,2,3,4,5,6,7,8,9,0]

print('a=',a.__sizeof__())
print('b=',b.__sizeof__())
```

Output:

a= 104
b= 120

In above code we have tuple  a and list  b with same items but the size of tuple is less than the list.

----------

## Different Use Cases

At first sight, it might seem that lists can always replace tuples. But tuples are extremely useful data structures

1.  Using a tuple instead of a list can give the programmer and the interpreter a hint that the data should not be changed.  
    
2.  Tuples are commonly used as the equivalent of a dictionary without keys to store data. For Example,
    
    [('Swordfish', 'Dominic Sena', 2001), ('Snowden', ' Oliver Stone', 2016), ('Taxi Driver', 'Martin Scorsese', 1976)]
    
    Above example contains tuples inside list which has a list of movies.  
    
3.  Reading data is simpler when tuples are stored inside a list. For example,
    
    [(2,4), (5,7), (3,8), (5,9)]
    
    is easier to read than
    
    [[2,4], [5,7], [3,8], [5,9]]
    

Tuple can also be used as key in dictionary due to their hashable and immutable nature whereas Lists are not used as key in a dictionary because list t handle  `__hash__()`  and have mutable nature.

```
key_val= {('alpha','bravo'):123} #Valid
key_val = {['alpha','bravo']:123} #Invalid
```cancan
# Data Structures
https://www.edureka.co/blog/data-structures-in-python/

**Python**  has been used worldwide for different fields such as making  [websites](https://www.edureka.co/blog/django-tutorial/),  [artificial intelligence](https://www.edureka.co/blog/pros-and-cons-of-ai/)  and much more. But to make all of this possible,  **data**  plays a very important role which means that this data should be stored efficiently and the access to it must be timely. So how do you achieve this? We use something called Data Structures. With that being said, let us go through the topics we will cover in  **Data Structures**  in  [Python](https://www.edureka.co/blog/python-basics/).

The article has been broken down into the following parts:

![Data structures in python](https://www.edureka.co/blog/wp-content/uploads/2019/10/Data-Structures-in-Python-300x169.png)

-   [What is a Data Structure?](https://www.edureka.co/blog/data-structures-in-python/#datastructure)
-   [Types of Data Structures in Python](https://www.edureka.co/blog/data-structures-in-python/#types)
-   [Built-in Data Structures](https://www.edureka.co/blog/data-structures-in-python/#builtin)
    -   [List](https://www.edureka.co/blog/data-structures-in-python/#list)
    -   [Dictionary](https://www.edureka.co/blog/data-structures-in-python/#dictionary)
    -   [Tuple](https://www.edureka.co/blog/data-structures-in-python/#tuple)
    -   [Sets](https://www.edureka.co/blog/data-structures-in-python/#set)
-   [User-Defined Data Structures](https://www.edureka.co/blog/data-structures-in-python/#user)
    -   [Arrays vs. List](https://www.edureka.co/blog/data-structures-in-python/#arrayvslist)
    -   [Stack](https://www.edureka.co/blog/data-structures-in-python/#stack)
    -   [Queue](https://www.edureka.co/blog/data-structures-in-python/#queue)
    -   [Trees](https://www.edureka.co/blog/data-structures-in-python/#tree)
    -   [Linked Lists](https://www.edureka.co/blog/data-structures-in-python/#linkedlist)
    -   [Graphs](https://www.edureka.co/blog/data-structures-in-python/#graph)
    -   [HashMaps](https://www.edureka.co/blog/data-structures-in-python/#hashmap)

So, s get started :)  

## **What is a Data Structure?**

**Organizing**,  **managing**  and  **storing**  data is important as it enables easier access and efficient modifications. Data Structures allows you to organize your data in such a way that enables you to store collections of data, relate them and perform operations on them accordingly.

## **Types of Data Structures in Python**

Python has  **implicit**  support for Data Structures which enable you to store and access data. These structures are called  [List](https://www.edureka.co/blog/lists-in-python/),  [Dictionary](https://www.edureka.co/blog/dictionary-in-python/),  [Tuple](https://www.edureka.co/blog/tuple-in-python/)  and  [Set](https://www.edureka.co/blog/sets-in-python/).

Python allows its users to create their own Data Structures enabling them to have  **full control**  over their  [functionality](https://www.edureka.co/blog/python-functions). The most prominent Data Structures are Stack, Queue, Tree, Linked List and so on which are also available to you in other programming languages. So now that you know what are the types available to you, why t we move ahead to the Data Structures and implement them using Python.

![](https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2019/10/TreeStructure-Data-Structures-in-Python-Edureka1.png)

## **Built-in Data Structures**

As the name suggests, these Data Structures are built-in with  [Python which makes programming easier](https://www.edureka.co/blog/python-basics/)  and helps programmers use them to obtain solutions faster. s discuss each of them in detail.

### **Lists**

[Lists](https://www.edureka.co/blog/lists-in-python/)  are used to store data of different data types in a sequential manner. There are addresses assigned to every element of the list, which is called as Index. The index value starts from 0 and goes on until the last element called the  **positive index**. There is also  **negative indexing**  which starts from -1 enabling you to access elements from the last to first. Let us now understand lists better with the help of an example program.

#### **Creating a list**

To create a list, you use the square brackets and add elements into it accordingly. If you do not pass any elements inside the square brackets, you get an empty list as the output.

1

2

3

4

`my_list` `=` `[]` `#create empty list`

`print``(my_list)`

`my_list` `=` `[``1``,` `2``,` `3``,` `'example'``,` `3.132``]` `#creating list with data`

`print``(my_list)`

**Output:**  
[]  
[1, 2, , 3.132]

#### **Adding Elements**

Adding the elements in the list can be achieved using the append(), extend() and insert() functions.

-   The append() function adds all the elements passed to it as a single element.
-   The extend() function adds the elements one-by-one into the list.
-   The insert() function adds the element passed to the index value and increase the size of the list too.

1

2

3

4

5

6

7

8

`my_list` `=` `[``1``,` `2``,` `3``]`

`print``(my_list)`

`my_list.append([``555``,` `12``])` `#add as a single element`

`print``(my_list)`

`my_list.extend([``234``,` `'more_example'``])` `#add as different elements`

`print``(my_list)`

`my_list.insert(``1``,` `'insert_example'``)` `#add element i`

`print``(my_list)`

**Output:**  
[1, 2, 3]  
[1, 2, 3, [555, 12]]  
[1, 2, 3, [555, 12], more_]  
[insert_, 2, 3, [555, 12], more_]

#### **Deleting Elements**

-   To delete elements, use the  _del_  keyword which is built-in into Python but this does not return anything back to us.
-   If you want the element back, you use the pop() function which takes the index value.
-   To remove an element by its value, you use the remove() function.

**Example:**

1

2

3

4

5

6

7

8

9

`my_list` `=` `[``1``,` `2``,` `3``,` `'example'``,` `3.132``,` `10``,` `30``]`

`del` `my_list[``5``]` `#delete element at index 5`

`print``(my_list)`

`my_list.remove(``'example'``)` `#remove element with value`

`print``(my_list)`

`a` `=` `my_list.pop(``1``)` `#pop element from list`

`print``(``'Popped Element: '``, a,` `' List remaining: '``, my_list)`

`my_list.clear()` `#empty the list`

`print``(my_list)`

**Output:**  
[1, 2, , 3.132, 30]  
[1, 2, 3, 3.132, 30]  
Popped Element: 2 List remaining: [1, 3, 3.132, 30]  
[]

#### **Accessing Elements**

Accessing elements is the same as accessing  [Strings in Python](https://www.edureka.co/blog/what-is-string-in-python/). You pass the index values and hence can obtain the values as needed.

1

2

3

4

5

6

7

`my_list` `=` `[``1``,` `2``,` `3``,` `'example'``,` `3.132``,` `10``,` `30``]`

`for` `element` `in` `my_list:` `#access elements one by one`

`print``(element)`

`print``(my_list)` `#access all elements`

`print``(my_list[``3``])` `#access index 3 element`

`print``(my_list[``0``:``2``])` `#access elements from 0 to 1 and exclude 2`

`print``(my_list[::``-``1``])` `#access elements in reverse`

**Output:**  
1  
2  
3  
example  
3.132  
10  
30  
[1, 2, , 3.132, 10, 30]  
example  
[1, 2]  
[30, 10, 3., 3, 2, 1]

#### **Other Functions**

You have several other functions that can be used when working with lists.

-   The len() function returns to us the length of the list.
-   The index() function finds the index value of value passed where it has been encountered the first time.
-   The count() function finds the count of the value passed to it.
-   The sorted() and sort() functions do the same thing, that is to sort the values of the list. The sorted() has a return type whereas the sort() modifies the original list.

1

2

3

4

5

6

7

`my_list` `=` `[``1``,` `2``,` `3``,` `10``,` `30``,` `10``]`

`print``(``len``(my_list))` `#find length of list`

`print``(my_list.index(``10``))` `#find index of element that occurs first`

`print``(my_list.count(``10``))` `#find count of the element`

`print``(``sorted``(my_list))` `#print sorted list but not change original`

`my_list.sort(reverse``=``True``)` `#sort original list`

`print``(my_list)`

### Output:

6 3 2 [1, 2, 3, 10, 10, 30]
[30, 10, 10, 3, 2, 1]

### **Dictionary**

[Dictionaries](https://www.edureka.co/blog/dictionary-in-python/)  are used to store  **key-value**  pairs. To understand better, think of a phone directory where hundreds and thousands of names and their corresponding numbers have been added. Now the constant values here are Name and the Phone Numbers which are called as the keys. And the various names and phone numbers are the values that have been fed to the keys. If you access the values of the keys, you will obtain all the names and phone numbers. So that is what a key-value pair is. And in Python, this structure is stored using Dictionaries. Let us understand this better with an example program.


#### **Creating a Dictionary**

Dictionaries can be created using the flower braces or using the dict() function. You need to add the key-value pairs whenever you work with dictionaries.

1

2

3

4

`my_dict` `=` `{}` `#empty dictionary`

`print``(my_dict)`

`my_dict` `=` `{``1``:` `'Python'``,` `2``:` `'Java'``}` `#dictionary with elements`

`print``(my_dict)`

**Output:**  
{}  
{, }

#### **Changing and Adding key, value pairs**

To change the values of the dictionary, you need to do that using the keys. So, you firstly access the key and then change the value accordingly. To add values, you simply just add another key-value pair as shown below.

1

2

3

4

5

6

`my_dict` `=` `{``'First'``:` `'Python'``,` `'Second'``:` `'Java'``}`

`print``(my_dict)`

`my_dict[``'Second'``]` `=` `'C++'` `#changing element`

`print``(}

#### **Deleting key, value pairs**

-   To delete the values, you use the pop() function which returns the value that has been deleted.
-   To retrieve the key-value pair, you use the popitem() function which returns a tuple of the key and value.
-   To clear the entire dictionary, you use the clear() function.

1

2

3

4

5

6

7

8

9

`my_dict` `=` `{``'First'``:` `'Python'``,` `'Second'``:` `'Java'``,` `'Third'``:` `'Ruby'``}`

`a` `=` `my_dict.pop(``'Third'``)` `#pop element`

`print``(``'Value:'``, a)`

`print``(``'Dictionary:'``, my_dict)`

`b` `=` `my_dict.popitem()` `#pop the key-value pair`

`print``(``'Key, value pair:'``, b)`

`print``(``'Dictionary'``, my_dict)`

`my_dict.clear()` `#empty dictionary`

`print``(``'n'``, my_dict)`

**}

}

{}

#### **Accessing Elements**

You can access elements using the keys only. You can use either the get() function or just pass the key values and you will be retrieving the values.

1

2

3

`my_dict` `=` `{``'First'``:` `'Python'``,` `'Second'``:` `'Java'``}`

`print``(my_dict[``'First'``])` `#access elements using keys`

`print``(my_dict.get(``'Second'``))`

**Output:**  
Python  
Java

#### **Other Functions**

You have different functions which return to us the keys or the values of the key-value pair accordingly to the keys(), values(), items() functions accordingly.

1

2

3

4

5

`my_dict` `=` `{``'First'``:` `'Python'``,` `'Second'``:` `'Java'``,` `'Third'``:` `'Ruby'``}`

`print``(my_dict.keys())` `#get keys`

`print``(my_dict.values())` `#get values`

`print``(my_dict.items())` `#get key-value pairs`

`)])  
Python

### **Tuple**

[Tuples](https://www.edureka.co/blog/tuple-in-python/)  are the same as lists are with the exception that the data once entered into the tuple cannot be changed no matter what. The only exception is when the data inside the tuple is mutable, only then the tuple data can be changed. The example program will help you understand better.

#### **Creating a Tuple**

You create a tuple using parenthesis or using the tuple() function.

1

2

`my_tuple` `=` `(``1``,` `2``,` `3``)` `#create tuple`

`print``(my_tuple)`

**Output:**  
(1, 2, 3)

#### **Accessing Elements**

Accessing elements is the same as it is for accessing values in lists.

1

2

3

4

5

6

7

`my_tuple2` `=` `(``1``,` `2``,` `3``,` `'edureka'``)` `#access elements`

`for` `x` `in` `my_tuple2:`

`print``(x)`

`print``(my_tuple2)`

`print``(my_tuple2[``0``])`

`print``(my_tuple2[:])`

`print``(my_tuple2[``3``][``4``])`

**Output:**  
1  
2  
3  
edureka  
(1, 2, )  
1  
(1, 2, )  
e

#### **Appending Elements**

To append the values, you  operator which will take another tuple to be appended to it.

1

2

3

`my_tuple` `=` `(``1``,` `2``,` `3``)`

`my_tuple` `=` `my_tuple` `+` `(``4``,` `5``,` `6``)` `#add elements`

`print``(my_tuple)`

**Output:**  
(1, 2, 3, 4, 5, 6)

#### **Other Functions**

These functions are the same as they are for lists.

1

2

3

4

5

`my_tuple` `=` `(``1``,` `2``,` `3``, [``'hindi'``,` `'python'``])`

`my_tuple[``3``][``0``]` `=` `'english'`

`print``(my_tuple)`

`print``(my_tuple.count(``2``))`

`print``(my_tuple.index([``'english'``,` `'python'``]))`

**Output:**  
(1, ])  
1  
3

[](https://www.edureka.co/advanced-java-sp "Advanced Java Certification Training")


### **Sets**

[Sets](https://www.edureka.co/blog/sets-in-python/)  are a collection of unordered elements that are unique. Meaning that even if the data is repeated more than one time, it would be entered into the set only once. It resembles the sets that you have learnt in arithmetic. The operations also are the same as is with the arithmetic sets. An example program would help you understand better.

#### **Creating a set**

Sets are created using the flower braces but instead of adding key-value pairs, you just pass values to it.

1

2

`my_set` `=` `{``1``,` `2``,` `3``,` `4``,` `5``,` `5``,` `5``}` `#create set`

`print``(my_set)`

**Output:**  
{1, 2, 3, 4, 5}

#### **Adding elements**

To add elements, you use the add() function and pass the value to it.

1

2

3

`my_set` `=` `{``1``,` `2``,` `3``}`

`my_set.add(``4``)` `#add element to set`

`print``(my_set)`

**Output:**  
{1, 2, 3, 4}

#### **Operations in sets**

The different operations on set such as union, intersection and so on are shown below.

1

2

3

4

5

6

7

8

`my_set` `=` `{``1``,` `2``,` `3``,` `4``}`

`my_set_2` `=` `{``3``,` `4``,` `5``,` `6``}`

`print``(my_set.union(my_set_2),` `'----------'``, my_set | my_set_2)`

`print``(my_set.intersection(my_set_2),` `'----------'``, my_set & my_set_2)`

`print``(my_set.difference(my_set_2),` `'----------'``, my_set` `-` `my_set_2)`

`print``(my_set.symmetric_difference(my_set_2),` `'----------'``, my_set ^ my_set_2)`

`my_set.clear()`

`print``(my_set)`

-   The union() function combines the data present in both sets.
-   The intersection() function finds the data present in both sets only.
-   The difference() function deletes the data present in both and outputs data present only in the set passed.
-   The symmetric_difference() does the same as the difference() function but outputs the data which is remaining in both sets.

**Output:**  
{1, 2, 3, 4, 6, 5- {1, 2, 3, 4, 5, 6}  
{4, 3- {3, 4}  
{2, 1- {1, 2}  
{1, 2, 6, 5- {1, 2, 5, 6}  
set()

Now that you have understood the built-in Data Structures, s get started with the user-defined Data Structures. User-defined Data Structures, the name itself suggests that users define how the Data Structure would work and define functions in it. This gives the user whole control over how the data needs to be saved, manipulated and so forth.

Let us move ahead and study the most prominent Data Structures in most of the programming languages.

## **User-Defined Data Structures**

### **Arrays vs. Lists**

Arrays and lists are the same structure with one difference. Lists allow heterogeneous data element storage whereas  [Arrays](https://www.edureka.co/blog/arrays-in-python/)  allow only homogenous elements to be stored within them.

### **Stack**

[Stacks](https://www.edureka.co/blog/stack-in-python/)  are linear Data Structures which are based on the principle of Last-In-First-Out (LIFO) where data which is entered last will be the first to get accessed. It is built using the array structure and has operations namely, pushing (adding) elements, popping (deleting) elements and accessing elements only from one point in the stack called as the TOP. This TOP is the pointer to the current position of the stack. Stacks are prominently used in applications such as Recursive Programming, reversing words, undo mechanisms in word editors and so forth.

![initial-stack-data-structure](https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2019/08/intial-stack-data-structure.png)

### **Queue**

A  [queue](https://www.edureka.co/blog/queue-data-structure-in-python/)  is also a linear data structure which is based on the principle of First-In-First-Out (FIFO) where the data entered first will be accessed first. It is built using the array structure and has operations which can be performed from both ends of the Queue, that is, head-tail or front-back. Operations such as adding and deleting elements are called En-Queue and De-Queue and accessing the elements can be performed. Queues are used as Network Buffers for traffic congestion management, used in Operating Systems for Job Scheduling and many more.

![queue](https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2019/09/priority-queue-in-c.png)  

### **Tree**

Trees are non-linear Data Structures which have root and nodes. The root is the node from where the data originates and the nodes are the other data points that are available to us. The node that precedes is the parent and the node after is called the child. There are levels a tree has to show the depth of information. The last nodes are called the leaves. Trees create a hierarchy which can be used in a lot of real-world applications such as the  [HTML](https://www.edureka.co/blog/what-is-html/)  pages use trees to distinguish which tag comes under which block. It is also efficient in searching purposes and much more.

![](https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2019/09/Perfect-Tree-300x214.png)  

### **Linked List**

[Linked lists](https://www.edureka.co/blog/linked-list-in-python/)  are linear Data Structures which are not stored consequently but are linked with each other using pointers. The node of a linked list is composed of data and a pointer called next. These structures are most widely used in image viewing applications, music player applications and so forth.

![SinglyLinkedList - Java Collections - Edureka](https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2017/05/Singly-LinkedList-1.jpg)  

### **Graph**

Graphs are used to store data collection of points called vertices (nodes) and edges (edges). Graphs can be called as the most accurate representation of a real-world map. They are used to find the various cost-to-distance between the various data points called as the nodes and hence find the least path. Many applications such as Google Maps, Uber, and many more use Graphs to find the least distance and increase profits in the best ways.




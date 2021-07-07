# VARIABLES

## Declaration  

To declare a variable in python, unlike other languages like C, C++, Java, etc there is no need to specify the type of data stored by the variable in advance! We can directly assign the value to the variable and its data and type can easily be changed during runtime by other assignments.


    a = 'I am a string'  
    b = '100' # This is an integer  
    a = 10.34 # Changes variable 'a' value.  


## Variable types  

To find the type of the variable we can use `type()` function


    x = 5
    print(type(x))


### Integers  

This value is represented by **int class.** It contains **positive or negative** whole numbers (without fraction or decimal). In Python there is **no limit** to how long an integer value can be.

### Float  

This value is represented by **float class**. It is a **real number with floating point** representation. It is specified by a **decimal point**. Optionally, the character `e` or `E` followed by a **positive or negative** integer may be appended to specify scientific notation.

### **Complex Numbers**

Complex number is represented by **complex class**. It is specified as *(real part) + (imaginary part)j* . For example – `2+3j`

### Boolean  

**Boolean** can have a value of either `True` or `False`. Boolean is represented by the **bool class**

### Strings  

In Python, strings are **arrays of bytes** representing **Unicode characters**. A string is a collection of **one or more characters put in a single quote, double-quote or triple quote.** In python there is no character data type, a character is a string of length one. It is represented by **str class**.

#### **String index**  

Each character in the string can be accessed by using its index  

<table style="border: 10px; margin-left: 10px;">
        <th>V</th>
        <th>A</th>
        <th>C</th>
        <th>H</th>
        <th>A</th>
        <th>N</th>
    <tr>
        <td>0</td>
        <td>1</td>
        <td>2</td>
        <td>3</td>
        <td>4</td>
        <td>5</td>
    </tr>
    <tr>
        <td>-6</td>
        <td>-5</td>
        <td>-4</td>
        <td>-3</td>
        <td>-2</td>
        <td>-1</td>
    </tr>
</table>

    print(string[2])
    string = "Vachan"
    print(string[2])  

    Output: c


### Lists  

In Python, **Lists** are like the **arrays**, declared in other languages which is an **ordered collection of data.** It is very flexible as the items in a list do not need to be of the same type.

#### Declaration  

**Lists** in Python can be created by just placing the sequence inside the square brackets `[]`.

    list = ["hi", 4, 24.082]  
    print(list)

    output: ["hi", 4, 24.082]

#### List Index  
 Lists can be indexed in python similar to strings.

    list = ["hi", 4, 24.082]
    print(list[1]) # Accessing the value at the index 1 of the list

    output: 4

### Tuples  

**Tuple** is an **ordered collection of Python objects**. The only difference between type and list is that tuples are immutable i.e. **tuples cannot be modified after it is created**. It is represented by **tuple class**.  

#### Declaration  

**tuples** are created by placing a sequence of values separated by `comma` with or without the use of parentheses for grouping of the data sequence. Tuples can contain any number of elements and of any type

    tuple = (1, "string", 102.45)
    print(tuple) 

    output: (1, 'string', 102.45)

#### Tuple Index  

Tuples can be accessed the same way as lists or strings.  

    tuple = (1, "string", 102.45)
    print(tuple[2])

    output: 102.45

### Set  

 **Set** is an **unordered collection of data types** that is `iterable`, `mutable` and has `no duplicate elements`. The order of elements in a set is undefined though it may consist of various elements.  
 
#### Declaration  

Sets can be created by using the built-in `set()` function with an iterable object or a sequence by placing the sequence inside curly braces `{}`, separated by `comma`. Type of elements in a set need not be the same, various mixed-up data type values can also be passed to the set. 
 
    set = set([10, "string", 586.283])
    print(set)

    output: {'string', 10, 586.283}

#### Set Index  

Set items cannot be accessed by referring to an index, since sets are unordered the items has no index

### Dictionary  

**Dictionary** in Python is an **unordered collection of data values**, used to store data values like a map, which unlike other Data Types that hold only single value as an element, Dictionary holds `key:value` pair. Key-value is provided in the dictionary to make it more optimized. Each key-value pair in a Dictionary is separated by a colon :, whereas each key is separated by a `comma`.

#### Creating a Dictionary

In Python, a Dictionary can be created by placing a sequence of elements within curly {} braces, separated by ‘comma’. Values in a dictionary can be of any datatype and can be duplicated, whereas keys can’t be repeated and must be immutable. Dictionary can also be created by the built-in function dict(). An empty dictionary can be created by just placing it to curly braces{}.

> Note – Dictionary keys are case sensitive, same name but different cases of Key will be treated  distinctly.

    Dict = {1: 'String', "hello": 5, 34.2: 2394.902}
    print(Dict)  

    Output: Dict = {1: 'String', "hello": 5, 34.2: 2394.902}

#### Dictionary Index

In order to access the items of a dictionary, we refer to its key name. Key can be used inside square brackets. There is also a method called get() that will also help in accessing the element from a dictionary.

    Dict = {1: 'String', "hello": 5, 34.2: 2394.902}
    print(Dict['hello'])

    Output: 5

    print(Dict.get(1))

    Output: String
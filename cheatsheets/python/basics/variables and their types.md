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

Lists in Python can be created by just placing the sequence inside the square brackets[].

    list = ["hi", 4, 24.082]  

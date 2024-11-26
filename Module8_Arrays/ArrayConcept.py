'''
Created on Nov 25, 2024

@author: fraidoon
'''
'''
Array concept (general)
A typical variable stores one data item, like the number 59 or the 
character 'a'. Instead, sometimes a list of data items should be stored. 
Ex: A program recording points scored in each quarter of a basketball 
game needs a list of 4 numbers. Requiring a programmer to declare 
4 variables is annoying; 200 variables would be ridiculous. 
An array is a special variable having one name, but storing 
a list of data items, with each item being directly accessible. 
Some languages use a construct similar to an array called a vector. 
Each item in an array is known as an element.

In programming, lists, arrays, and vectors are examples of 
abstract data types (ADTs), which are abstractions used by 
a computer to represent collections of data or the relationships 
between the data.

You might think of a normal variable as a truck, and an array variable 
as a train. A truck has just one car for carrying "data", 
but a train has many cars, each of which can carry data.

Arrays
Array declarations and accessing elements
A programmer commonly needs to maintain a list of items, 
just as people maintain a list of items like a grocery list 
or a course roster. An array variable is an ordered list of 
items of a given data type and size. Each item in an array is called an element. 
For array x, each element is accessed as x[0], x[1], ... In an 
array access, the number in brackets is called the index of that element. 
In Coral, the first array element is at index 0.

Iterating through arrays
Iterating through an array using loops
Iterating through arrays using loops is common and is an important 
programming skill to master.

An array's indices are numbered 0 to size-1, not 1 to size. 
Thus, when iterating through an array, programmers use the 
standard loop form shown below, starting with i = 0, and 
iterating while i < size.

Such a loop will iterate with i = 0, 1, ..., size - 1, 
thus matching the array's indices. If size is 5, the loop 
iterates with i = 0, 1, 2, 3, 4, as desired.

Swapping two variables (general)
Sometimes a program must swap values among two variables. 
Swapping two variables x and y means to assign y's value with x, 
and x's value with y. If x is 33 and y is 55, then after swapping 
x is 55 and y is 33.

A common method for swapping uses a temporary third variable. 
To understand the intuition of such temporary storage, 
consider a person holding a book in one hand and a phone in the other, 
wishing to swap the items. The person can temporarily place the 
phone on a table, move the book to the other hand, then pick up the phone.


Code: Arrays
Array declarations
In code, a variable that is an array has a special keyword "array" added, 
with the size indicated too. The code below declares userVals to be 
an array with 4 elements.


Functions with array parameters
Array parameters and arguments
A function's parameter may be defined as an array, by including the 
word array just as in a variable declaration. To call such a function, 
the function call's argument passes only an array's name. 
The function's statements typically use the array.size value.



'''
#!/usr/bin/env python
# coding: utf-8

# 1) . What is the difference between enclosing a list comprehension in square brackets and parentheses?

# ans: Enclosing a list comprehension in square brackets returns a list.but where as enclosing a list comprehension in parentheses returns a generator object
# 

# In[2]:


l = [ele for ele in range(10)]
print(l, type(l))
g = (ele for ele in range(10))
print(g, type(g))


# 2) What is the relationship between generators and iterators?

# ans:- An iterator is an object which contains a countable number of values and it is used to iterate over iterable objects like list, tuples etc
# Using an iterator- iter() keyword is used to create an iterator containing an iterable object. next() keyword is used to call the next element in the iterable object.
# 
# Generator
# It is another way of creating iterators in a simple way where it uses the keyword “yield” instead of returning it in a defined function Generators are implemented using a function Here, the yield function returns the data without affecting or exiting the function. It will return a sequence of data in an iterable format where we need to iterate over the sequence to use the data as they won’t store the entire sequence in the memory By using next() function we can iterate the output of generator function
#         

# In[3]:


# iterator
iter_list = iter([1, 2 ,3])
print(next(iter_list))
print(next(iter_list))
print(next(iter_list))


# In[5]:


# GEnerator 

def sq(n):
    for i in range(1, n+1):
        yield i*i


# In[10]:


sq(2)
lst = sq(2)
print(next(lst))
print(next(lst))


# 3) What are the signs that a function is a generator function?

# ans:- If a function contains at least one yield statement (it may contain other yield or return statements), it becomes a generator function. Both yield and return will return some value from a function.

# 4) What is the purpose of a yield statement?

#  ans:- yield statement looks much like a return statement, except that instead of stopping execution of the function and returning, yield instead provides a value to the code looping over the generator and pauses execution of the generator function

# 5) What is the relationship between map calls and list comprehensions? Make a comparison and contrast between the two.

# ans:- 
# 1.List comprehension is more concise and easier to read as compared to map.
# 2.List comprehension allows filtering. In map, we have no such facility. For example, to print all odd numbers in range of 50, we can write [n for n in range(50) if n%2 != 0]. There is no alternate for it in map
# 3.List comprehension are used when a list of results is required as final output.but map only returns a map object. it needs to be explicitly coverted to desired datatype.
# 4.List comprehension is faster than map when we need to evaluate expressions that are too long or complicated to express
# 5.Map is faster in case of calling an already defined function on a set of values.

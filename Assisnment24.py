#!/usr/bin/env python
# coding: utf-8

# 1. What is the relationship between def statements and lambda expressions ?

# ans:- Keyword def that marks the start of the function header. A function name to uniquely identify the function. Function naming follows the same rules of writing identifiers in Python
# 
# Lambdas are one-line methods without a name or we can say anonymous Func. They work practically the same as any other method in Python Lambdas differ from normal Python methods because they can have only one expression, can't contain any statements and their return type is a function object

# 2. What is the benefit of lambda?

# ans:- 1.Can be used to create Nameless/Anonymous functions inside some complex functions if we are planning to use it only once.
# 2.Moderate to small functions can be created in a single line
# 3.Fuctions created using lambda expressions can be assigned to a variable and can be used by simply calling the variable

# 3. Compare and contrast map, filter, and reduce.

# ans:- 1. map(): The map() function is a type of higher-order. This function takes another function as a parameter along with a sequence of iterables and returns an output after applying the function to each iterable present in the sequence.
# 2. filter(): The filter() function is used to create an output list consisting of values for which the function returns true.
# 3. reduce(): The reduce() function, as the name describes, applies a given function to the iterables and returns a single value

# In[1]:


from functools import reduce
# map function
print('Map ->',list(map(lambda x:x+x, [1,2,3,4])))
# fitler function
print('Filter ->',list(filter(lambda x:x%2 !=0, [1,2,3,4])))
# reduce function
print('Reduce ->',reduce(lambda x,y:x+y, [1,2,3,4,5,6]))


# 4. What are function annotations, and how are they used?

# ans:- Function annotations provide a way of associating various parts of a function with arbitrary pythoncexpressions at compile time.
# Annotations of simple parameters def func(x: expression, y: expression = 20):
# Whereas the annotations for excess parameters are as − def func (**args: expression, **kwargs: expression):

# 5. What are recursive functions, and how are they used?

# ans:- A recursive function is a function that calls itself during its execution. 
# This means that the function will continue to call itself and repeat its behavior until some condition is met to return a result

# In[2]:


def fact(x):
    if x == 1 :
        return 1
    else :
        return x * fact(x-1) 
    
fact(3)


# 6. What are some general design guidelines for coding functions?

# ans:- 
# 1.Use 4-space indentation and no tabs.
# 2.Use docstrings
# 3.Wrap linethat they don’t exceed 79 characters
# 4.Use of regular and updated comments are valuable to both the coders and users
# 5.Use of trailing commas : in case of tuple -> ('good',)
# 6.Use Python’s default UTF-8 or ASCII encodings and not any fancy encodings
# 7.Naming Conventions

# 7. Name three or more ways that functions can communicate results to a caller.

# ans:-
# 1.print
# 2.return
# 3.yield

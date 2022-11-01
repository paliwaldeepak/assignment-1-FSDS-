#!/usr/bin/env python
# coding: utf-8

# #1. What exactly is []?

# ans:- it is a list value that contain no item or a empty list value 

# #2. In a list of values stored in a variable called spam, how would you assign the value 'hello' as the third value? (Assume [2, 4, 6, 8, 10] are in spam.)

# In[3]:


spam  = [2, 4, 6, 8, 10]
spam[2] = "hello"
print(spam)


# #Let's pretend the spam includes the list ['a', 'b', 'c', 'd'] for the next three queries.

# #3. What is the value of spam[int(int('3' * 2) / 11)]?

# In[4]:


#ans:'d' ('3' * 2 is the string '33', which is passed to int() before being divided by 11. This eventually evaluates to 3. Expressions can be used wherever values are used.)
spam = ['a', 'b', 'c', 'd']
spam[int(int('3' * 2) / 11)]


# #4. What is the value of spam[-1]?

# In[5]:


#ans: 'd' (Negative indexes count from the end.)
spam[-1]


# #5. What is the value of spam[:2]?

# In[6]:


#ans:-['a', 'b']
spam[:2]


# #Let's pretend bacon has the list [3.14, 'cat,' 11, 'cat,' True] for the next three questions.

# #6. What is the value of bacon.index('cat')?

# In[10]:


#ans:- 1
bacon = [3.14, 'cat', 11, 'cat', True]
bacon.index('cat')


# #7. How does bacon.append(99) change the look of the list value in bacon?

# In[14]:


#ans:- [3.14, 'cat', 11, 'cat', True, 99]
bacon.append(99)


# In[15]:


bacon


# #8. How does bacon.remove('cat') change the look of the list in bacon?

# In[16]:


#ans:- [3.14, 11, 'cat', True, 99, 99, 99, 99]
bacon.remove('cat')
print(bacon)


# #9. What are the list concatenation and list replication operators?

# #ans:- The operator for list concatenation is +, while the operator for replication is *

# #10. What is difference between the list methods append() and insert()?

# #ans:- While append() will add values only to the end of a list, insert() can add them anywhere in the list.

# #11. What are the two methods for removing items from a list?

# #ans:- pop() , and remove() 

# #12. Describe how list values and string values are identical.

# #ans:- Lists are similar to strings, which are ordered collections of characters, except that the elements of a list can have any type and for any one list, the items can be of different types.

# #13. What's the difference between tuples and lists?

# ans:- Lists are mutable; they can have values added, removed, or changed. Tuples are immutable; they cannot be changed at all. Also, tuples are written using parentheses, (), while lists use the square brackets[]

# #14. How do you type a tuple value that only contains the integer 42?

# #ans:- (42)

# #15. How do you get a list value's tuple form? How do you get a tuple value's list form?

# #ans:- The tuple() and list() functions, respectively

# #16. Variables that "contain" list values are not necessarily lists themselves. Instead, what do they contain?

# #ans:-They contain references to list values

# #17. How do you distinguish between copy.copy() and copy.deepcopy()?

# #ans:- The copy.copy() function will do a shallow copy of a list, while the copy.deepcopy() function will do a deep copy of a list. That is, only copy.deepcopy() will duplicate any lists inside the list.

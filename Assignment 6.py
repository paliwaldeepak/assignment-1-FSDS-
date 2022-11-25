#!/usr/bin/env python
# coding: utf-8

# #1. What are escape characters, and how do you use them?

# In[ ]:


#ans:- Escape characters represent characters in string values that would otherwise be difficult or impossible to type into code


# #2. What do the escape characters n and t stand for?

# In[ ]:


#ans:- \n is a newline and \t is a tab


# #3. What is the way to include backslash characters in a string?

# In[ ]:


#ans:- The \\ escape character will represent a backslash character


# #4. The string "Howl's Moving Castle" is a correct value. Why isn't the single quote character in the word Howl's not escaped a problem?

# In[ ]:


#ans:- The single quote in Howl's is fine because you've used double quotes to mark the beginning and end of the string.


# #5. How do you write a string of newlines if you don't want to use the n character?

# In[ ]:


#ans:- Multiline strings allow you to use newlines in strings without the \n escape character.


# #6. What are the values of the given expressions?
# 'Hello, world!'[1]
# 'Hello, world!'[0:5]
# 'Hello, world!'[:5]
# 'Hello, world!'[3:]
# 

# #ans:- he expressions evaluate to the following:
# 
# 'e'
# 
# 'Hello'
# 
# 'Hello'
# 
# 'lo world!

# #7. What are the values of the following expressions?
# 'Hello'.upper()
# 'Hello'.upper().isupper()
# 'Hello'.upper().lower()
# 

# In[ ]:


#ans:- The expressions evaluate to the following:

'HELLO'

True

'hello'


# #8. What are the values of the following expressions?
# 'Remember, remember, the fifth of July.'.split()
# '-'.join('There can only one.'.split())
# 

# In[ ]:


#ans:- The expressions evaluate to the following:

['Remember,', 'remember,', 'the', 'fifth', 'of', 'November.']

'There-can-be-only-one.


# In[1]:


'Remember, remember, the fifth of July.'.split()


# In[2]:


'-'.join('There can only one.'.split())


# #9. What are the methods for right-justifying, left-justifying, and centering a string?

# In[ ]:


#ans:- The rjust(), ljust(), and center() string methods, respectively


# #10. What is the best way to remove whitespace characters from the start or end?

# In[ ]:


#ans:- The lstrip() and rstrip() methods remove whitespace from the left and right ends of a string, respectively.


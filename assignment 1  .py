#!/usr/bin/env python
# coding: utf-8

# # 1. In the below elements which of them are values or an expression? eg:- values can be integer or string and expressions will be mathematical operators

# ans- 'hello' , -87.8, 6 are values and
#       *,  - , / , + are mathmatical expression

# # 2. What is the difference between string and variable?

# ans- Variable just a character or symbol that can be use to store a data in your program and string is a type of information that can be store in a variable, A String is usually define enclosed with "" 
# examp.- 

# In[1]:


x = "hello"


# In[2]:


type(x)


# In[ ]:


here x is variable and "hello" is string


# # 3. Describe three different data types.
ans:- 1. integer data type
      2. string data type
      3. floating data type
examp.-
# In[4]:


y = 2
type(y)


# In[5]:


a = "hii"
type(a)


# In[6]:


z = 2.5
type(z)


# # 4. What is an expression made up of? What do all expressions do?

# ans- Expression is made up some veriable, mathmatical operation and operator that give give some information and evaluate to a single output. 

# In[8]:


#exmp/
a= 2
b= 3
c = a+b
print(c)


# # 5. This assignment statements, like spam = 10. What is the difference between an expression and a statement?

# ans:- Expression is combination of  veriable, mathmatical operation and operator that give give some information and evaluate to a single output. but statement just a conversation that not return anything

# # 6. After running the following code, what does the variable bacon contain?
# bacon = 22
# bacon + 1
# 

# In[11]:


bacon = 22
bacon + 1
print(bacon)


# In[13]:


bacon = 22
bacon = bacon + 1
print(bacon)


# # 7. What should the values of the following two terms be?
# 'spam' + 'spamspam'
# 'spam' * 3
# 

# In[15]:


'spam' + 'spamspam'


# In[16]:


'spam' * 3


# In[17]:


'spam' + 'spamspam'
'spam' * 3


# # 8. Why is eggs a valid variable name while 100 is invalid?

# In[ ]:


ans- variable name can not begin with a number so 100 is invalid and eggs is valid variable.


# # 9. What three functions can be used to get the integer, floating-point number, or string version of a value?

# In[ ]:


ans- for integar = int()
     for floating-point number = float()
     for string = str()


# # 10. Why does this expression cause an error? How can you fix it?
# 'I have eaten ' + 99 + ' burritos.'

# In[18]:


'I have eaten ' + 99 + ' burritos.'


# In[19]:


# expression cause an error because 99 is a int we can not concatenate str with int, the right code is
'I have eaten ' + "99" + ' burritos.'


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# 1. Assign the value 7 to the variable guess_me. Then, write the conditional tests (if, else, and elif) to print the string 'too low' if guess_me is less than 7, 'too high' if greater than 7, and 'just right' if equal to 7.

# In[19]:


#ans:-
guess_me = int(input("value"))
if guess_me <7:
    print('too low')
elif guess_me >7:
    print('too high')
else :
    print('just right') 


# 2. Assign the value 7 to the variable guess_me and the value 1 to the variable start. Write a while loop that compares start with guess_me. Print too low if start is less than guess me. If start equals guess_me, print 'found it!' and exit the loop. If start is greater than guess_me, print 'oops' and exit the loop. Increment start at the end of the loop.

# In[20]:


#ans:- 
guess_me = 7
start = 1
while True:
    if start < guess_me:
        print('too low')
    elif start == guess_me:
        print('found it')
        break
    else:
        print('oops')
        break
    start += 1


# 3. Print the following values of the list [3, 2, 1, 0] using a for loop.

# In[21]:


#ans:-
l = [3, 2, 1, 0]
for i in l:
    print(i)


# 4. Use a list comprehension to make a list of the even numbers in range(10)

# In[43]:


#ans:- 
l = []
for i in range(10):
    if i%2 ==0:
        l.append(i)
print(l)


# 5. Use a dictionary comprehension to create the dictionary squares. Use range(10) to return the keys, and use the square of each key as its value.

# In[44]:


#ans:-
print({x:x**2 for x in range(10)})


# 6. Construct the set odd from the odd numbers in the range using a set comprehension (10).

# In[48]:


#ans:- 
l = []
for i in range(10):
    if i%2 !=0:
        l.append(i)
print(l)


# 7. Use a generator comprehension to return the string 'Got ' and a number for the numbers in range(10). Iterate through this by using a for loop.

# In[51]:


#ans:
generator = ('Got '+str(x) for x in range(10))
for i in generator:
    print(i, end=' ')


# 8. Define a function called good that returns the list ['Harry', 'Ron', 'Hermione'].

# In[53]:


#ans:=
def good():
    x= ['Harry', 'Ron', 'Hermione']
    return x


# 9. Define a generator function called get_odds that returns the odd numbers from range(10). Use a for loop to find and print the third value returned.

# In[61]:


#ans:
def get_odds():
    output = []
    for i in range(10):
        if i%2 != 0:
            output.append(i)
    yield output

next(get_odds())[2]


# 10. Define an exception called OopsException. Raise this exception to see what happens. Then write the code to catch this exception and print 'Caught an oops'

# In[62]:


#ans:-
class OopsException(Exception):
    pass

def test(input):
    if input <0:
        raise OopsException(a)
try:
    test(-100)
except Exception as e:
    print('Caught in Oops ->',e)


# 11. Use zip() to make a dictionary called movies that pairs these lists: titles = ['Creature of Habit', 'Crewel Fate'] and plots = ['A nun turns into a monster', 'A haunted yarn shop'].

# In[63]:


#ans:- 

titles = ['Creature of Habit', 'Crewel Fate']
plots = ['A nun turns into a monster', 'A haunted yarn shop']
output = dict(zip(titles,plots))
print(output)


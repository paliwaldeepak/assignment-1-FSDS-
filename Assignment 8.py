#!/usr/bin/env python
# coding: utf-8

# 1. Is the Python Standard Library included with PyInputPlus?

# #ans:- PyInputPlus is not a part of the Python Standard Library, we must install it separately using Pip.

# 2. Why is PyInputPlus commonly imported with import pyinputplus as pypi?

# #ans:- You can import the module with import pyinputplus as pyip so that you can enter a shorter name when calling the module’s functions

# 3. How do you distinguish between inputInt() and inputFloat()?

# #ans:- The difference is in the data-type when you use the first one the program expects an integer value as input but in the latter it expects a float value i.e number containing a decimal

# 4. Using PyInputPlus, how do you ensure that the user enters a whole number between 0 and 99?

# #ans:- By using pyip.inputint(min=0, max=99)

# 5. What is transferred to the keyword arguments allowRegexes and blockRegexes?

# #ans:- A list of regex strings that are either explicitly allowed or denied

# 6. If a blank input is entered three times, what does inputStr(limit=3) do?

# #ans:- The function will raise RetryLimitException.

# 7. If blank input is entered three times, what does inputStr(limit=3, default='hello') do?

# #ans:- The function returns the value 'hello'

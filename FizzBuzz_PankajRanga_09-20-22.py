#!/usr/bin/env python
# coding: utf-8

# In[ ]:


FizzBuzz is a game that has gained in popularity as a programming assignment to weed out non-programmers during job interviews. The object of the assignment is less about solving it correctly according to the below rules and more about showing the programmer understands basic, necessary tools such as if-/else-statements and loops. The rules of FizzBuzz are as follows:

For numbers 1 through 100,

    if the number is divisible by 3 print Fizz;
    if the number is divisible by 5 print Buzz;
    if the number is divisible by 3 and 5 (15) print FizzBuzz;
    else, print the number.


# In[2]:


for i in range (1,101):
    if (i%3==0 and i%5==0):
        print("FizzBuzz")
    elif(i%3==0):
        print("Fizz")
    elif(i%5==0):
        print("Buzz")
    else:
        print(i)
        


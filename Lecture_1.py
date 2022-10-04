#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 13:04:20 2022

Write description of the script here! 
Include updates here and instructions here as well. 
If you have a bug you can mention that here as well.
Write the outline for the program here BEFORE you start to code.
This part is like a long comment.

@author: inf-31-2022
"""
#This is a comment and will not be executed. 
print("Hello World!") #The script prints Hello World! in the terminal.

"""
Use this for long comments!

Upload your scripts to your Github

Use #%% to divide the script into chunks (cells).

Press Ctrl + enter to run only one line or chunk.
Press F9 to just one line.
Press F5 to run the entire script.
Run the script from the Linux terminal by typing:
    python Lecture_1.py
You can also use the terminal in Spyder, but try to avoid that.
"""

#%%
print("How do I feel today?")
for i in range(0,10):
    if i > 5:
        print("I feel happy!")
    else:
        print("I feel sad.")
print("End of test")

#%%
print(type(1))
print(type("GATCCT"))
print(type("TRUE"))
print(type(True))
print(type('TruE'))
"print(type(TruE))" #Error, you need to type it as True.
print(type('XX$12'))
print(type(-1.22))
print(type(0))
print(type(0.00))

#%%
"""
You can't use - or __ (double underscore) for variables. You shouldn't use True or False either.
It becomes easier if the variables have clear, descriptive names.
"""

x = 5
y = 90
print(x, y)
print(x+y)

x = '5'
y = 'Hus'
print(x, y)
print(x+y)

#%%
print(2 + 2)
print(6 - 9)
print(8 / 3.0)
print(9 * 3)
print(6 ** 2) #The same as 6²

#%%
import math
print(math.log10(100)) #math.log is a function from the module math.
"print(log10(100))" #Log10 is not a function in Python.

#%%
"Exercise: solve with Python"

"1. Second power of five"
print(5 ** 2)

"2. Square root of 16"
print(16 ** 0.5)
print(math.sqrt(16))

"3. The remainder of 7 divided by 3"
print(7%3) #The number 3 fits into 7 two times, the remainder is then one (two of three fits).

"4. Absolute value of -0.777"
print(abs(-0.777))

"5. Round 5.4 and 5.5"
print(round(5.4))
print(round(5.5))

"6. Round 6.7777888 to the third decimal point."
print(round(6.7777888, 3))

"7. Convert 7.7 to integer plus 8 to it."
print(round(7.7)+8)

"8. What is the minimum of 5,2,7 and maximum of 3,5,0.9"
print(min(5,2,7))
print(max(3,5,0.9))

"9. What is log10 of 100"
print(math.log10(100))

"10. What is the sixth digit of pi?"
print(str(math.pi)[6]) #Last digit = 9

x = "123456"
print(x[0])

#%%
import random

print(random.random()) #A random float between 0 and 1.
print(random.randrange(1,10)) #A random integer between 1 and 10.
print(random.choice('abcd'))

number_list = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]
print("Original list:", number_list)

random.shuffle(number_list) #Shuffle the list.
print("List after first shuffle:", number_list)

random.shuffle(number_list)
print("List after second shuffle:", number_list)

#%%
"""
You can't change elements in a string but you can remake the whole string.

Splicing excercise:
"""
Seq = "ABCDEFGHIJKLMNOP"
print(Seq[0])
print(Seq[0:3])
print(Seq[-1])
print(Seq[-1:-3]) #No output.
print(Seq[-3:-1]) #The third last and second last elements.
print(Seq[-2:]) #The two last elements.
print(Seq[::2]) #Each second element from the beginning, including Seq[0].
print(Seq[::-2]) #Each second element from the end, including Seq[-1].

#%%
mystring = "I'm a DNA sequence"
print('DNA' in mystring) #Prints True.

#%d for integers, %f for floats, %s for string. For adding variables in strings for printing.

print("This is a really long string\nso we will break it into two lines.")

#%%
myDNA = "ACGTAGCTAGCTAGTGT"
yourDNA = "AAACCCGGGTTT"

'1.'
print(myDNA.count('G'))


#!/usr/bin/env python
# coding: utf-8

# <H2> FUNCTIONS </H2>

# In[22]:


import sympy
import numpy


# INSERT THE REGISTRATION BELOW
REGISTRATION = 931

C = REGISTRATION % 10




def get_function_1(variable, C):
    '''
    Function to return the function 1 based on the variable and the constant received as arguments.
    @Receives: The function's variable; The function's constant.
    @Return: The function.
    '''
    
    return sympy.exp(VARIABLE-3) + sympy.exp(VARIABLE-1) + sympy.exp(VARIABLE) - C - 1




def get_function_2(variable, C):
    '''
    Function to return the function 2 based on the variable and the constant received as arguments.
    @Receives: The function's variable; The function's constant.
    @Return: The function.
    '''
    
    return VARIABLE**4 - (4*VARIABLE**3) + 3*VARIABLE - C




def get_function_3(variable, C):
    '''
    Function to return the function 3 based on the variable and the constant received as arguments.
    @Receives: The function's variable; The function's constant.
    @Return: The function.
    '''
    
    return 4*sympy.sin( (C+1) * VARIABLE ) + 2 




def calculate_function(function):
    '''
    Function to calculate and return the result of the function received as argument.
    @Receives: The function.
    @Returns: The result of the function.
    '''
    
    result = sympy.solve(function)
    
    return result





# DEFINING THE FUNCTION'S VARIABLE
VARIABLE = sympy.Symbol('x')


# DEFINING THE FUNCTIONS
function_1 = get_function_1(VARIABLE, C)

function_2 = get_function_2(VARIABLE, C)

function_3 = get_function_3(VARIABLE, C )


functions = [function_1, function_2, function_3]


# CALCULATING THE FUNCTIONS
results = []

for function in functions:
    result = calculate_function(function)
    
    results.append(result)
    


# PRINTING THE RESULT
for i in range( len(results) ):
    try:
        result = float(results[i][0])
    except:
        result = complex(results[i][0])
    
    print(f'Exercise {i+1}: Calculating the function: {result}\n')


#!/usr/bin/env python
# coding: utf-8

# <H2> CALCULATING INTEGRAL </H2>

# In[6]:


import sympy


# INSERT THE REGISTRATION BELOW
REGISTRATION = 931

C = REGISTRATION % 10



def function(x, C):
    '''
    Function to return the function to calculate the integral of, based on the variable and the constant received as arguments.
    @Receives: The function's variable; The function's constant.
    @Return: The function.
    '''
    
    # DEFINING THE FUNCTION
    return x**3 - 4*x**2 + 5*x - C




def calculate_integral(function, variable, limits=None):
    '''
    Function to calculate and return the integral of the function received as argument based on the variable received as argument.
    @Receives: The function to calculate the integral of; The function's variable;
    @Optional_Receive: The limits of the integral.
    @Returns: The results of the calculated integral.
    '''    
  
    # SETTING UP THE RESULTS
    results = []
    
    
    # IF LIMITS WAS PASSED, CALCULATE THE INTEGRAL BETWEEN THEM
    if limits:
        integral = sympy.Integral(function, (variable, limits['min'], limits['max']) )
        
    else:
        integral = sympy.Integral(function, variable)
    
    
    # CALCULATING THE INTEGRAL
    result = integral.doit()        
    
    
    # RETURNING THE RESULT
    return result




# DEFINING THE FUNCTION'S VARIABLE
VARIABLE = sympy.Symbol('x')


# GETTING THE FUNCTION
FUNCTION = function(VARIABLE, C)


# SETTING UP THE ARGUMENTS (LIMITS MIN & MAX)
limits = {'min' : 0, 'max' : 5}


# CALLING THE DERIVATIVE FUNCTION
result = calculate_integral(FUNCTION, VARIABLE, limits)

    
# PRINTING THE RESULT
print(f'Exercise {1}: Calculating the integral of the function: {result}\n')


# In[ ]:





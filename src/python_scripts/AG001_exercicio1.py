#!/usr/bin/env python
# coding: utf-8

# <H2> CALCULATING LIMIT </H2>

# In[1]:


import sympy


# INSERT THE REGISTRATION BELOW
REGISTRATION = 931

C = REGISTRATION % 10




def function(x, C):
    '''
    Function to return the function to calculate the limit of, based on the variable and the constant received as arguments.
    @Receives: The function's variable; The function's constant.
    @Return: The function.
    '''
    
    # DEFINING THE FUNCTION
    return ( (3*x**3 - 3) / (4*x**2 - 4) ) * (C + 1)




def calculate_limit(function, variable, tendencies):
    '''
    Function to calculate and return the limit of the function received as argument based on the variable and the tendencies received as arguments.
    @Receives: The function to calculate the limit of; The function's variable; The tendencies of the limit.
    @Returns: The result of the calculated limits.
    '''
    
    # DEFINING THE RESULTS
    results = []
    
    
    # LOOPING FOR EACH TENDENCY
    for tendency in tendencies:
        
        # SETTING UP THE LIMIT
        limit = sympy.Limit(function, variable, tendency)
    
    
        # CALCULATING THE LIMIT
        result = limit.doit()
        
        
        # APPENDING THE RESULT
        results.append(result)

        
    # RETURNING THE RESULTS
    return results





# DEFINING THE FUNCTION'S VARIABLE
VARIABLE = sympy.Symbol('x')



# GETTING THE FUNCTION
FUNCTION = function(VARIABLE, C)



# DEFINING INFINITY CONSTANTS
INFINITY = sympy.S.Infinity

NEGATIVE_INFINITY = - sympy.S.Infinity



# DEFINING THE LIMIT TENDENCY
TENDENCIES = [1, INFINITY, NEGATIVE_INFINITY]



# CALLING THE FUNCTION
results = calculate_limit(FUNCTION, VARIABLE, TENDENCIES)


# PRINTING THE RESULTS
for i in range(len(results)):
    print(f'Exercise {i+1}: Calculating the limit of the function when {VARIABLE} tends to {TENDENCIES[i]}: {results[i]}\n')


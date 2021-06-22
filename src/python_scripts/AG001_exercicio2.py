#!/usr/bin/env python
# coding: utf-8

# <H2> CALCULATING DERIVATIVE </H2>

# In[22]:


import sympy


# INSERT THE REGISTRATION BELOW
REGISTRATION = 931

C = REGISTRATION % 10



def function(t, C):
    '''
    Function to return the function to calculate the derivative of, based on the variable and the constant received as arguments.
    @Receives: The function's variable; The function's constant.
    @Return: The function.
    '''
    
    # DEFINING THE FUNCTION
    return (-t**3 / 3) + (2*t**2) - C




def calculate_derivative(function, variable, order=1, point=None):
    '''
    Function to calculate and return the derivative of the function received as argument based on the order, the variable and the point received as arguments.
    @Receives: The function to calculate the derivative of; The function's variable;
    @Optional_Receive: The derivative's order; The derivative's points.
    @Returns: The results of the calculated derivatives.
    '''    
  
    # SETTING UP THE RESULTS
    results = []
    
     
    # SETTING UP THE DERIVATIVE
    derivative = sympy.Derivative(function, variable, order)
    
    
    # CALCULATING THE DERIVATIVE
    result = derivative.doit()
    
    
    # IF A POINT WAS PASSED, CALCULATE THE DERIVATIVE ON THAT POINT
    if point:
        result = result.subs({variable:point})
        
        
    # RETURNING THE RESULT
    return result




# DEFINING THE FUNCTION'S VARIABLE
VARIABLE = sympy.Symbol('t')


# GETTING THE FUNCTION
FUNCTION = function(VARIABLE, C)


# SETTING UP THE ARGUMENTS (ORDERS & POINTS)
calc_1 = {'order' : 1, 'point' : None}
calc_2 = {'order' : 1, 'point' : 3}
calc_3 = {'order' : 2, 'point' : None}
calc_4 = {'order' : 2, 'point' : 5}

arguments = [calc_1, calc_2, calc_3, calc_4]



# CALLING THE DERIVATIVE FUNCTION
results = []

for argument in arguments:
    result = calculate_derivative(FUNCTION, VARIABLE, argument['order'], argument['point'])
    results.append(result)

    
# PRINTING THE RESULT
for i in range( len(results) ):
    print(f'Exercise {i+1}: Calculating the derivative of the function: {results[i]}\n')


# In[ ]:





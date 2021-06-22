#!/usr/bin/env python
# coding: utf-8

# <H2> SYSTEM & MATRIX </H2>

# In[46]:


import numpy
import matplotlib


# INSERT THE REGISTRATION BELOW
REGISTRATION = 931

C = REGISTRATION % 10



def calculate_voltage(function_constant, C):
    '''
    Function to return the result of the voltage based on the constant received as argument.
    @Receives: The function; The function's constant.
    @Return: The result of the function.
    '''
    
    # DEFINING THE FUNCTION
    return function_constant + 2 * C




def generate_matrix(dict_matrix):
    '''
    Function to generate and return a matrix, based on the dict received as argument.
    @Receive: The dict containing all the matrix lines.
    @Return: The matrix.
    '''
    
    matrix = numpy.matrix([
        dict_matrix['line_1'],
        dict_matrix['line_2'],
        dict_matrix['line_3']
    ])
    
    
    return matrix




def calculate_system(dict_A, dict_B):
    '''
    Function to calculate and return the result of the system, based on the dicts received as argument.
    @Receives: The dicts to convert into a matrix and calculate the system.
    @Returns: The results of the calculated system.
    '''
    
    # GENERATING MATRICES
    A = generate_matrix(dict_A)
    
    B = generate_matrix(dict_B)
    
    
    # INVERTING MATRIX A
    A_inv = numpy.linalg.inv(A)
    
    
    # MULTIPLYING MATRIX A BY MATRIX B
    X = A_inv * B
    
    # RETURNING THE RESULT
    return X





# DEFINING MATRIX A (Literal part)
matrix_A = {}

matrix_A['line_1'] = [1, 1, 1]
matrix_A['line_2'] = [25, -10, 0]
matrix_A['line_3'] = [0, -10, 20]



# DEFINING MATRIX X (Coefficients)
matrix_B = {}

matrix_B['line_1'] = [0]
matrix_B['line_2'] = [calculate_voltage(10, C)]
matrix_B['line_3'] = [calculate_voltage(5, C)]



# GETTING THE MATRIX X (Results)
matrix_X = calculate_system(matrix_A, matrix_B)



# PRINTING THE RESULT
eng_format = matplotlib.ticker.EngFormatter()

for i in range( len(matrix_X) ):
    current_value = eng_format( float(matrix_X[i]) )
    
    current_value = current_value.replace('m', '[mA]')
    
    print(f'I{i+1}: {current_value}\n')


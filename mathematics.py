# MATHEMATICS

# Find which math expression matches the answer that you are given, if you have an integer answer, and a list of math expressions.

# Task: 
# Test each math expression to find the first one that matches the answer that you are given.

# Input Format: 
# Two inputs: an integer and a space separated string of math expressions. The following operations need to be supported: addition +, subtraction -, multiplication , division /. 
# An expression can include multiple operations.

# Output Format: 
# A string that tells the index of the first math expression that matches. If there are no matches, output 'none'.

# Sample Input: 
# 15
# (2+100) (53) (14+1)

# Sample Output: 
# index 1


# Solved using eval() for 6/6 test cases

def math_operators_eval(answer = int(input()), expressions = input().split(' ')): # answer = 46, expressions = (99+1+4) (51-4-1) (50/2/5)

    for i in range(len(expressions)):
        if int(eval(expressions[i])) == answer: # evaluate each expression and compare to answer
            return f'index {i}' #print out the index if it exists, else 'none'
    return 'none'

print(math_operators_eval()) # index 1

# --------------------------------------------------------------------------------------------------------------------------------------

# TEST WITHOUT eval()
# Passed 4/6 test cases and can handle multiple operators in the same expression
# as long as they are the same operator ie (1+1+1+1) but not (1+1-1)

import operator

def math_operators(answer = int(input()), eq = input().strip("()")): # answer = 46, expressions = (99+1+4) (51-4-1) (50/2/5)

    eq_list = eq.split(') (')
    op_list = ['+', '-', '*', '/']
    ops = { "+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv } # assigns operator functions to symbols
    output = []

    for i in range(0, len(eq_list)):

        for j in op_list: # +, -, *, /

            if j in eq_list[i]: # if operator found at index i
                eq_list[i] = eq_list[i].split(j) #splits list using the operator ie "+"
                total = int(eq_list[i][0]) #sets initial total to equal the first element

                for k in eq_list[i][1: len(eq_list)]:
                    total = ops[j](total, int(k)) # adds/subtracts/multiplies/divides each element to the total starting at index 1
                output.append(total) #adds total to new list

    print(output) #[104, 46, 25.0]
    return f'index {output.index(answer)}' if answer in output else 'none'

print(math_operators()) # index 1




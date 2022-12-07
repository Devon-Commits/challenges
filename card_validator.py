# CREDIT CARD VALIDATOR
# You need to verify if the given credit card number is valid. For that you need to use the Luhn test.

# Here is the Luhn formula:
# 1. Reverse the number.
# 2. Multiple every second digit by 2. 
# 3. Subtract 9 from all numbers higher than 9.
# 4. Add all the digits together.
# 5. Modulo 10 of that sum should be equal to 0. 

# Task: 
# Given a credit card number, validate that it is valid using the Luhn test. Also, all valid cards must have exactly 16 digits.

# Input Format:
# A string containing the credit card number you need to verify.

# Output Format:
# A string: 'valid' in case the input is a valid credit card number (passes the Luhn test and is 16 digits long), or 'not valid', if it's not.


def validation(card_string = input()): # 4091131560563988 example input
    if len(card_string) != 16 or card_string.isdigit() == False: #if length of input string isn't 16 or string isn't all digits, return "not valid"
        return print("not valid")
        
    reverse_num = card_string[::-1] # reverses string
    num_list = [int(i) for i in reverse_num] # creates list of integers

    for i in range(1, len(num_list), 2): # multiplies every 2nd list value by 2
        num_list[i] *=  2

    for i in range(0, len(num_list)): # subtracts 9 from list value if greater than 9
        if num_list[i] > 9:
            num_list[i] -= 9

    if sum(num_list) % 10 == 0: # checks if the final sum is divisible by 10
        print("valid")
    else:
        print("not valid")

validation() # 4091131560563988 is valid
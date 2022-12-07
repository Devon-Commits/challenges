# NO NUMERALS

# You write a phrase and include a lot of number characters (0-9), but you decide that for
# numbers 10 and under you would rather write the word out instead. Can you go in and edit
# your phrase to write out the name of each number instead of using the numeral? 

# Task: 
# Take a phrase and replace any instances of an integer from 0-10 and replace it with the 
# English word that corresponds to that integer.

# Input Format: 
# A string of the phrase in its original form (lowercase).

# Output Format: 
# A string of the updated phrase that has changed the numerals to words.

# Sample Input: 
# i need 2 pumpkins and 3 apples

# Sample Output: 
# i need two pumpkins and three apples

def number_swap(string_in = input()): # there are 6 apples, 4 bananas, and 10 pears

    num_list = ['0','1','2','3','4','5','6','7','8','9']
    word_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for char in string_in:
        if '10' in string_in: # handles finding '10' in the string, if not handled will put 'onezero' instead of 'ten'
            string_in = string_in.replace('10', 'ten')

        elif char in num_list: # if the current character is found in num_list
            x = num_list.index(char) # finds the index of the character in num_list
            string_in = string_in.replace(num_list[x], word_list[x]) #replaces character at char index by the element at same index in the word list

    return string_in # there are six apples, four bananas, and ten pears

print(number_swap()) 
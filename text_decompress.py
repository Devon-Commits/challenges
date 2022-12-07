# TEXT DECOMPRESSOR

# You need to decompress text. The compressed version has a number next to each symbol/letter, representing the amount of time that symbol should appear. 
# For example, a2b3 is the compressed version of aabbb

# Task: 
# Write a program that takes the compressed text as input and outputs the decompressed version.

# Input Format: 
# A single string with letters/symbols, each followed by a number.

# Output Format: 
# A string, representing the decompressed text.


def decompressor(string_in = input()): # v3&4b2 example input
    string_in = list(string_in) # turns string into a list
    string_char = string_in[0:len(string_in): 2] # slices every 2nd character starting at index 0 to create a list of characters to be multiplied
    string_num = string_in[1:len(string_in): 2] # slices every 2nd character starting at index 1 to create a list of numbers to multiply with
    result = [] # create empty list
    
    for x in range(0, len(string_char)):
        result.append(string_char[x] * int(string_num[x])) # multiply character list by int value of number list ie 'k' * 2 = 'kk' and add to result

    print(''.join(result)) # turns the result list into a string

decompressor() # output vvv&&&&bb

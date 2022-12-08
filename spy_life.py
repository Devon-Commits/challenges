# The Spy Life

# You are a secret agent, and you receive an encrypted message that needs to be decoded. The code that is being used flips the message backwards and inserts non-alphabetic characters in the message to make it hard to decipher.

# Task: 
# Create a program that will take the encoded message, flip it around, remove any characters that are not a letter or a space, and output the hidden message.

# Input Format:
# A string of characters that represent the encoded message.

# Output Format: 
# A string of character that represent the intended secret message.

# Sample Input: 
# d89%l++5r19o7W *o=l645le9H

# Sample Output: 
# Hello World

class SpyTools(): # 1t8s5%e=W d74=l14i3!W

    def decode(self, message):
        reverse_message = message[::-1] # slice to reverse message
        decoded_list = []
        for i in reverse_message:
            if i.isalpha() == True or i == " ": # append to list if character is a-z or " "
                decoded_list.append(i)
        print("".join(decoded_list)) # turn list back into string

s1 = SpyTools()
s1.decode(message=input()) # Wild West


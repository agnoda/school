# from Python.DongaPythonProject1 import lower_limit, upper_limit, number_guessed
#
import math

# Create a dictionary to map uppercase and lowercase letters to its alphabetical order number
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
uppercase_dict = {i+1:j for i,j in enumerate(uppercase)}     # numerical order of the letter is the key in this dictionary
rev_uppercase_dict = {i:j+1 for j,i in enumerate(uppercase)} # letters being the key in this dictionary
#print(uppercase_dict) self check to verify dictionary contents were correct
#print(rev_uppercase_dict) self check to verify dictionary contents were correct

lower_limit = 1
upper_limit = 100
number_guessed = int((lower_limit+upper_limit)/2) # use binary search
letter_guessed = uppercase_dict[int((1+26)/2)]
print(f"Think of a number between {lower_limit} and {upper_limit}, or think of a character between A-Z or a-z!")
print(f"Is your number greater (>), equal (=), or less (<) than {number_guessed}?")
print(f"or is your letter before (-), equal (o), or after (+) than the letter {letter_guessed}/{letter_guessed.lower()}?")
user_input = input('Please answer (<, =, >, +, o, -):')
# A different set of symbols should be used as the input to distinguish whether it is a number or letter based on the user input
# Otherwise, there is no way to tell if it is a number or a letter when the guessing range is within 1-26
# The user also doesn't input anything to differentiate upper/lowercase since there is no input and it cannot be told by the alphebatic order of the the letter
# It seems that the listed requirements may make more sense when the user is guessing a random number or random character provided by the program

count = 1 # to be used for recording how many attempts have been conducted

while user_input == ">" or user_input == "=" or user_input == "<"  or user_input == "+"  or user_input == "o" or user_input == "-" :
    ## If user input is >, =, <, we're making a guess for a number from the user
    if user_input == ">" or user_input == "=" or user_input =="<":
        while user_input != "=":
            if user_input == "<":
                if (upper_limit-lower_limit)<=1: #No more integer can be found between the lower/upper limit
                    print("Inconsistent answers! Exiting the program.")
                    break
                else:
                    upper_limit = number_guessed-1 #reset the upper limit to an integer less than the number guessed
                    number_guessed = int((upper_limit+lower_limit)/2)
                    print(f"Is your number greater (>), equal (=), or less (<) than {number_guessed}?")
            elif user_input == ">":
                if (upper_limit-lower_limit)<=1: #No more integer can be found between the lower/upper limit
                    print("Inconsistent answers! Exiting the program.")
                    break
                else:
                    lower_limit = number_guessed+1 #reset the lower limit to an integer larger than the number guessed
                    number_guessed = int((upper_limit+lower_limit)/2)
                    print(f"Is your number greater (>), equal (=), or less (<) than {number_guessed}?")
            else:
                print("You did not enter a valid value. Please re-enter.")
                print(f"Is your number greater (>), equal (=), or less (<) than {number_guessed}?")
            user_input = input('Please answer (<, =, >):')
            count += 1
        else:
            print(f"I have guessed it! The final answer is {number_guessed}")
            print(f"It took {count} step(s)!")
    #If the user input +, o, -, we're guessing a letter from the user
    elif user_input == "+" or user_input == "o" or user_input =="-":
        upper_limit = 26 # since we're guessing a letter here; set the upper limit to 26
        while user_input != "o":
            if user_input == "-":
                if (upper_limit-lower_limit)<=1: #No more integer can be found between the lower/upper limit
                    print("Inconsistent answers! Exiting the program.")
                    break
                else:
                    upper_limit = rev_uppercase_dict[letter_guessed]-1 #reset the upper limit to an integer less than the numerical order of the lettered guessed
                    letter_guessed = uppercase_dict[int(math.ceil((upper_limit + lower_limit)/2))] #looks at A-Z dictionary and define what number it corresponds to
                    print(f"Is your character before (-), equal (o), or after (+) the character {letter_guessed}?")
            elif user_input == "+":
                if (upper_limit - lower_limit) <= 1:  # No more integer can be found between the lower/upper limit
                    print("Inconsistent answers! Exiting the program.")
                    break
                else:
                    lower_limit = rev_uppercase_dict[letter_guessed] + 1  # reset the lower limit to an integer larger than the number guessed
                    letter_guessed = uppercase_dict[int(math.ceil((upper_limit + lower_limit)/2))]
                    print(f"Is your character before (-), equal (o), or less (+) than {letter_guessed}?")
            else:
                print("You did not enter a valid value. Please re-enter.")
                print(f"Is your number before (-), equal (o), or after (+) the character {letter_guessed}?")
            user_input = input('Please answer (-, o, +):')
            count += 1
        else:
            print(f"I have guessed it! The final answer is {letter_guessed}")
            print(f"It took {count} step(s)!")
    break
else:
    # Cannot confirm if the we're guessing a letter or a number
    print("You did not enter a valid value. Please re-enter.")
    user_input = input('Please answer (<, =, >, -, o, +):')
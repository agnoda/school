

lower_limit = 1
upper_limit = 100 # defines number range, makes it easy to change
number_guessed = int((upper_limit+lower_limit)/2) # a binary search, or half bracketing, is the fastest way to guess a number within a range
print(f"Think of a number between {lower_limit} and {upper_limit}")

print(f"Is your number greater (>), equal (=), or less (<) than {number_guessed}?")
user_input = input('Please answer (<, =, >):') # user input on the number they picked

count = 1 # to be used for recording how many steps have been attempted
while user_input != "=":
    if user_input == "<":
        if (upper_limit-lower_limit)<=1: #No more integer can be found between the lower/upper limit have been reached, the user is lying
            print("Inconsistent answers! Exiting the program.") # The program should spot if the information the user provided is inconsistent
            break
        else:
            upper_limit = number_guessed-1 #resets the upper limit to an integer less than the number guessed
            number_guessed = int((upper_limit+lower_limit)/2)
            print(f"Is your number greater (>), equal (=), or less (<) than {number_guessed}?")
    elif user_input == ">":
        if (upper_limit-lower_limit)<=1: #No more integer can be found between the lower/upper limit have been reached, the user is lying
            print("Inconsistent answers! Exiting the program.") # The program should spot if the information the user provided is inconsistent
            break
        else:
            lower_limit = number_guessed+1 #reset the lower limit to an integer larger than the number guessed
            number_guessed = int((upper_limit+lower_limit)/2)
            print(f"Is your number greater (>), equal (=), or less (<) than {number_guessed}?")
    else:
        print("You did not enter a valid value. Please re-enter.")
        print(f"Is your number greater (>), equal (=), or less (<) than {number_guessed}?")
    user_input = input('Please answer (<, =, >):')
    count += 1 # variable to count the amount times while loop has been conducted
else:
    print(f"I have guessed it! The final answer is {number_guessed}")
    print(f"It took {count} step(s)!")
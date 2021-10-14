#ord() method converts a character into its Unicode code. 
# The ord() method takes one argument: a string containing a 
# single Unicode character. This method returns an integer that 
# represents that character in Unicode
print("Program started!")
print("Please a standard character:")
character = input()
if len(character) == 1:
    print(f"The ASCII code for {character} is {ord(character)}")
else:
    print("A single character was expected")
print("Program ended!")

#ASCII is short for American Standard Code for Information 
# Interchange.  It is used to represent characters such as 
# letters of the alphabet as numbers as the latter can be stored 
# by computers.  For example, the lower case letter 'a' is
#  represented as the decimal number 97.  
#ask the user for hte age
print("Please neter your age")
# read the user's response
age = int(input())
# chehck if the user is an adult 
if age >=18: # the column means do the following
     print("You are an adult")
     print("Because you are 18 years old or greater")
elif age >= 13:
    print("You are a teneger")
else: # again the column means do the following 
    print("You are not a child")
    print("Because you are below 18")
print("End of the program")

# # This is a single line comment

# """
# This is a multi line comment
# we can write many lines here
# as much as you want
# no matter
# This all above lines are consider as
# comment in python
# """

# # this is a print function in python
# #which provide output to the console
# print("Hello! Batch 33B")

# print(2+2)


#name = input("Enter your name ")
#age = int(input("Enter your age"))
#print(f"Hi! your name is {name} and your age is {age} years old)


#college_name = input("Enter your collegename")
#classroom = (input("Enter your classroom"))
#print(f"Hi! your college name is {college_name} and your classroom is {classroom} room no")


age=int(input("Please provide your age:"))

# conditional statement
# if block only

print("code started ......")
if age>18:
    print(f("you are play this game because you are above 18"))

    print("code ended ......")

# if-else block
if age>18:
    print(f("you xan play this game because you are above {age}"))
else:      
     print("you need to be above 18 years old to play this game")

## proper use of if-elif-else block
if age<0:
    print("Please inter your valid age")
elif 0<age<=10:
    print("so your are kid, your movie ticket is Nrs.100")
elif 10<age<20: 
    print("your movie ticket is Nrs.20o")
else:
    print("your movie ticket is Nrs.300")


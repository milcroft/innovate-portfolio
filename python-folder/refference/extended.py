# var = "3"
# print(type(var)) # "3"

# var = int(var)
# print(type(var)) # 3

# var = float(var)
# print(type(var)) # 3.0

# print("What is your name?\n")
# my_name = input()

# if my_name:
#     print(f"Hello {my_name}, how are you?")
# else:
#     print("You did not give me your name!")

# bool = False

# if bool != True:
#     print("False")
# else:
#     print("True")

# def add_up():
#     num1 = input("Number One: ")
#     num2 = input("Number Two: ")

#     try:
#         print(f"{num1} + {num2} is {(int(num1) + int(num2))}!")
#     except:
#         print("ERROR: Numerical Values Only!")
#         add_up()
# add_up()


# scope = "global"
# print(f"the current scope is {scope}")

# def function():
#     scope = "local"
#     print(f"the current scope is {scope}")
# function()

# print(f"the current scope is {scope}")

def char_create():
    global char_name
    char_name = input("Please enter your name.\n")
    print(f"Welcome, {char_name}")
char_create()

def char_death():
    print(f"Unfortunately, {char_name} has died...")
char_death()
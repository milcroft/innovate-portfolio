# Activity one

def isEven(str):
    str_length = len(str)
    if str_length % 2 == 0:
        print(
            f'[{str}] has a string length of [{str_length}] and is an EVEN number.')
    else:
        print(
            f'[{str}] has a string length of [{str_length}] and  is an ODD number.')


isEven("Welcome to Code Nation")


# Activity two
# version 1

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
            "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


def select_list_item_value_by_index_number(list):
    try:
        number = input(f"select number between 1 and {len(list)} \n")
        number = int(number)
        if number >= 1 and number <= len(list):
            number = number - 1
            print(list[number])
        else:
            select_list_item_value_by_index_number(list)
    except:
        select_list_item_value_by_index_number(list)


select_list_item_value_by_index_number(alphabet)


# version 2

def value_by_index_number(list, number):
    try:
        number = int(number)
        if number >= 1 and number <= len(list):
            number = number - 1
            print(list[number])
        else:
            print(f"number is not between 1 and {len(list)}")
    except:
        print("non-numeric value found!")


value_by_index_number(alphabet, 3333)

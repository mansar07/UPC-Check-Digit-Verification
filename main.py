from code_check import *  # importing the functions from the code_check.py file into this current file

# Creating empty lists for every category
basic = []
positional = []
upc = []
none = []
base_nums = str  # Initializing the base_nums variable that stores the user input

while base_nums != str(0):  # Using a while True loop to keep looping and ask user for input
    base_nums = str(input("Please enter code (digits only) (enter 0 to quit): "))  # Asking user for input for the digits

    if (basic_code(base_nums) and positional_code(base_nums) and upc_code(base_nums)) is True:  # If all three codes are true then they will be appended to their lists
        basic.append(base_nums)
        positional.append(base_nums)
        upc.append(base_nums)
        print("-- code:", base_nums, "valid Basic code.")
        print("-- code:", base_nums, "valid Position code.")
        print("-- code:", base_nums, "valid UPC code.")

    elif (basic_code(base_nums) and positional_code(base_nums)) is True:  # If basic and positional code are true then they will be appended to their lists
        basic.append(base_nums)
        positional.append(base_nums)
        print("-- code:", base_nums, "valid Basic code.")
        print("-- code:", base_nums, "valid Position code.")

    elif (positional_code(base_nums) and upc_code(base_nums)) is True:  # If positional and upc code are true then they will be appended to their lists
        positional.append(base_nums)
        upc.append(base_nums)
        print("--code:", base_nums, "valid Position code.")
        print("--code:", base_nums, "valid UPC code.")

    elif (basic_code(base_nums) and upc_code(base_nums)) is True:  # If basic code and upc code are true then they will be appended to their lists
        basic.append(base_nums)
        upc.append(base_nums)
        print("--code:", base_nums, "valid Basic code.")
        print("--code:", base_nums, "valid UPC code.")

    elif basic_code(base_nums) is True:  # If basic code is true then it will be appended to its list
        basic.append(base_nums)
        print("--code:", base_nums, "valid Basic code.")

    elif positional_code(base_nums) is True:  # If positional code is true then it will be appended to its list
        positional.append(base_nums)
        print("--code:", base_nums, "valid Position code.")

    elif upc_code(base_nums) is True:  # If upc code is true then it will be appended to its list
        upc.append(base_nums)
        print("--code:", base_nums, "valid UPC code.")

    else:
        none.append(base_nums)  # If none of the statements are true then the code will be stored into the none list
        print("--code:", base_nums, "not Basic, Position or UPC code.")

    if base_nums == str(0):  # If the user enters 0 the loop will break and print the following
        print()  # Printing the final output which shows the summary of the codes
        print("Summary")
        none.remove(none[-1])  # Removes the 0 that is added onto the none list towards the end

        if not basic:  # If none of the elements are true for basic then it prints None
            basic.append("None")
        print("Basic:", ", ".join(basic))

        if not positional:  # If none of the elements are true for positional then it prints None
            positional.append("None")
        print("Position:", ", ".join(positional))

        if not upc:  # If none of the elements are true for upc then it prints None
            upc.append("None")
        print("UPC:", ", ".join(upc))

        if not none:  # If none of the elements are true for none then it prints None
            none.append("None")
        print("None:", ", ".join(none))

        exit(0)  # Breaks the loop

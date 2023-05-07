
def basic_code(base_nums):
    end_digit = int(base_nums[-1])  # Accessing the last digit of the numbers and storing it in this variable
    remaining_digits = str(base_nums)[:-1]  # Creating a new list of numbers which does not include the last number from the original list
    total = 0  # initializing the total variable

    if base_nums == str(0):
        return False

    else:

        for i in remaining_digits:  # Using a for loop to loop through the new list without the last element

            if i.isdigit():  # If the string is a integer then it will go through the if statement
                total = total + int(i)  # all the values in the string input are being added together

        if total % 10 == end_digit:  # if the result modulus 10 is the same as the last digit modulus 10 then it will return true, else it would return false
            return True

        else:
            return False

# print(basic_code("123456789"))


def positional_code(base_nums):
    end_digit = int(base_nums[-1])  # Accessing the last digit of the numbers and storing it in this variable
    remaining_digits = list(map(int, base_nums[:-1].split()))  # Using map to create the input of strings into a list of integers
    total = 0  # initializing the total variable
    result = 0  # initializing the result variable

    if base_nums == str(0):
        return False

    else:

        for i in remaining_digits:

            for j in remaining_digits:  # Iterating through remaining digits -1
                # print("i =", int(i) + 1, "j =", j)
                total += int(i) * int(j)  # Multiplying the digit with its index position
                # print("total =", total)
                result = total % 10  # Computing the result by doing total modulus 10

        if result == end_digit:  # If result is equal to the last digit than return true, and false otherwise
            return True

        else:
            return False

# print(positional_code("123456789"))


def upc_code(base_nums):
    end_digit = int(base_nums[-1])  # Accessing the last digit of the numbers and storing it in this variable
    remaining_digits = str(base_nums)[:-1]  # Creating a new list of numbers which does not include the last number from the original list
    total = 0  # initializing the total variable
    index = 0  # Creating an index variable to check for odd and even
    result = 0  # initializing the result variable
    length_of_base_nums = len(base_nums)  # Length of the base_nums input parameter

    if base_nums == str(0):
        return False

    else:

        for i in remaining_digits:  # Using a for loop to iterate through the remaining digits

            if (index + 1) % 2 != 0:  # If odd then multiply by 3
                total += int(i) * 3

                if index < length_of_base_nums:  # If index is less than the length of base_nums then increment index
                    index += 1

            elif (index + 1) % 2 == 0:  # If even then multiply by 1
                total += int(i) * 1

                if index < length_of_base_nums:  # If index is less than the length of base_nums then increment index
                    index += 1

        result = total % 10  # Compute the result by doing total modulus 10

        if 1 <= result <= 9:
            result = 10 - result

        if result == int(base_nums) % 10:  # If result is equal to the base_nums modulus 10 then return True, otherwise return False
            return True

        else:
            return False

# print(upc_code("123456789"))

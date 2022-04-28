# Write a Python function called max_num()to find the maximum of three numbers.

def max_num(num1, num2, num3):
    if num1 > num2:
        if num1 == num3:
            print("Numbers One and Three are equal, and greater than Number Two.")
        elif num1 > num3:
            print("Number One is maximum!")
        elif num1 < num3:
            print("Number Three is maximum!")
    elif num2>num1:
        if num2 == num3:
            print("Numbers Two and Three are equal, and greater than Number One.")
        elif num2 > num3:
            print("Number Two is maximum!")
        elif num2 < num3:
            print("Number Three is maximum!")
    elif num1 == num2:
        if num1 == num3:
            print("All numbers are equal.")
        elif num1 > num3:
            print("Numbers One and Two are equal, and greater than Number 3.")
        elif num1 < num3:
            print("Numbers One and Two are equal, and less than Number 3.")
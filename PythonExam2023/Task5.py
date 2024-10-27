# Task 5

negativeNumbers = []  # List for negative numbers
positiveNumbers = []  # List for positive numbers
zeroes = []  # List for zeroes

while True:  # While loop, with boolean condition, to stop only when userinput is blank
    userinput = input("Enter an integer (blank to quit): ")
    if userinput == "":  # If user enters blank, loop stops
        break  # Break the while loop, and print the numbers from the three lists
    try:  # Try this block of code, if loop is false
        userinput = int(userinput)  # Converting the string into an integer
        if userinput < 0:
            negativeNumbers.append(userinput)  # If input is 0, add number to zeroes
        elif userinput > 0:
            positiveNumbers.append(userinput)  # If number is positive, add number to positiveNumbers
        elif userinput == 0:
            zeroes.append(userinput)  # If number is negative, add number to
    except ValueError:  # ValueError, if user prints anything other than an integer
        print("Enter a valid number, or blank to quit")

print("The numbers were:")
#  Using the star expression, all the lists are printed without brackets []
print(*positiveNumbers + zeroes + negativeNumbers)
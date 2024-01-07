def string_splitter(s):
    # Ensure string length is greater than 16
    if len(s) < 16:
        return "The length of the string must be at least 16."
    
    # Create empty strings to hold numbers and letters separately
    numbers = []
    letters = []

    # Separate the characters and numbers into separate strings
    for char in s:
        if char.isdigit():
            numbers.append(char)
        elif char.isalpha():
            letters.append(char)

    # Check if the number is even for each number in the inputted/given string
    # If it is even, change its value to ASCII via ord() function
    for i in range(len(numbers)):
        if int(numbers[i]) % 2 == 0:
            numbers[i] = str(ord(numbers[i]))

    # Check if the letters separated are uppercase
    # If uppercase, change the value to ASCII via ord() function
    for i in range(len(letters)):
        if letters[i].isupper():
            letters[i] = str(ord(letters[i]))

    # Combine and return the amended numbers and letters list
    return ''.join(numbers + letters)

# Assignment given input and relevant output expected
s = "56aAww1984sktr235270aYmn145ss785fsq31D0" 
    # s = input("Enter a string to decode: ")
print(string_splitter(s)) 
    # Output: "554195652503550748152575653148a65wwsktra89mnssfsq68"
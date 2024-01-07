# Decryption function for Caesar cypher
def decrypt_caesar_cypher(encrypted_text, key):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            shifted = ord(char) - key
            if char.islower():
                if shifted < ord("a"):
                    shifted += 26
            elif char.isupper():
                if shifted < ord("A"):
                    shifted += 26
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char
    return decrypted_text


# Function to find key
def key():
    total = 0
    for i in range(5):
        for j in range(3):
            if i + j == 5:
                total += i + j
            else:
                total -= i - j

    counter = 0
    while counter < 5:
        if total < 13:
            total += 1
        elif total > 13:
            total -= 1
        else:
            counter += 2
    return total


# Print the decryption key result to the terminal
print(f"The decryption key is: {key()}")
print()  # Print an empty line for space

# Encrypted code provided in the assignment
encrypted_code = """
tybony inevnoyr
100
zl_qvpg = {'xrl1': 'inyhr1', 'xrl2': 'inyhr2', 'xr13': 'inyhr3'}
qrs cebprff_ahzoref():
tybony tybony_inevnoyr ybpny_inevnoyr = 5
ahzoref= [1, 2, 3, 4, 5]
juvyr ybpny_inevnoyr > >:
vs ybpny inevnoyr % 2 == 0: ahzoref.erzbir(ybpny_inevnoyr)
ybpny inevnoyr -= 1
erghea ahzoref
zl_frg (1, 2, 3, 4, 5, 5, 4, 3, 2, 1} erfhyg- cebprff_ahzoref(ahzoref-z1_frg)
qrs zbqvsl_qvpg():
ybpny inevnoyr
10
zl_qvpg['xr14'] = ybpny_inevnoyr
zbqvs1_qvpg(5)
qrs hcqngr_tybony():
tybony tybony_inevnoyr
tybony_inevnoyr += 10
sbe v va enatr(5):
cevag(v)
v +- 1
vs zl_frg vf abg Abar naq zl_qvpg['xr14'] == 10: cevag("Pbaqvgvba zrg!")
vs 5 abg va z1_qvpg:
cevag("5 abg sbhaq va gur qvpgvbanel!")
cevag(tybony_inevnoyr)
cevag(zl_qvpg)
cevag(zl_frg)
"""

# Use the key of 13 to decrypt the entire block of code
key_used_for_decryption = 13
decrypted_code = decrypt_caesar_cypher(encrypted_code, key_used_for_decryption)

# Print the decrypted code
print("Decrypted code:")
print(decrypted_code)
print()  # Print an empty line for space

# Global variable initialisation
global_variable = 100

# Dictionary initialisation
my_dict = {"key1": "value1", "key2": "value2", "key3": "value3"}


def process_numbers():
    local_variable = 5
    numbers = [1, 2, 3, 4, 5]
    while local_variable > 0:
        if local_variable % 2 == 0:
            if local_variable in numbers:
                numbers.remove(local_variable)
        local_variable -= 1
    return numbers


def modify_dict():
    local_variable = 10
    my_dict["key4"] = local_variable


def update_global():
    global global_variable
    global_variable += 10

if __name__ == "__main__":
    # Print heading for the corrected decrypted code
    print("Corrected decrypted code:")
    print()  # Print an empty line for space

    # Set initialisation
    my_set = {1, 2, 3, 4, 5}

    # Processing numbers and updating the dictionary
    result = process_numbers()
    modify_dict()

    # Updating the global variable
    update_global()

    # Loop for demonstration
    for i in range(5):
        print(i)

    # Conditional checks
    if my_set is not None and my_dict.get("key4") == 10:
        print("Condition met!")

    if 5 not in my_dict:
        print("5 not found in the dictionary!")

    # Printing results
    print(global_variable)
    print(my_dict)
    print(my_set)

    # End of script
    print("Script execution completed.")

#Decode Famous Quote
#Parameters
text =  "VZ FRYSVFU VZCNGVRAG NAQ N YVGGYR VAFRPHER V ZNXR ZVFGNXRF V NZ BHG BS PBAGEBY \n NAQ NG GVZRF UNEQ GB UNAQYR OHG VS LBH PNAG UNAQYR ZR NG ZL JBEFG GURA LBH FHER NF \nURYY QBAG QRFREIR ZR NG ZL ORFG ZNEVYLA ZBAEBR"
key = 13
decoded_text = ""
#Iterate through encrypted text
for char in text:
    #If not a space modify ascii value by key
    if (ord(char) != 32):
        oldchar = char
        newchar = ord(oldchar) - key
        #If character gets lowered below capital alphabet(<A), circle back to end(Z)
        if newchar < 65:
            newchar += 26
        #Append Decrypted Character
        decoded_text += chr(newchar)
    #If character is space include it in the decryption
    else:
        print(ord(char))
        decoded_text += char
print(decoded_text)
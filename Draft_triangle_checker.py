#Integrity testing a triangle
#enter the lenght of the corresponding side below
a = input('Enter the first side of the triangle (a)') 
b = input('Enter the second side of the triangle (b)')
c = input('Enter the third side of the triangle (c)')

if int(a) + int(b) > int(c) and int(b) + int(c) > int(a) and int(b) + int(c) > int(a) and int(c) + int(a) > int(b) and int(a) !=0 and int(b) !=0 and int(c) !=0:
    print('congratulations thats a triangle')
else:
    print('unfortunately thats not a triangle')
reset = input('would you like to try another set of inputs? Yes/No')

#if reset == Yes
    #code for looping back to top


#if True:(a+b>c) and (b+c>a) and (c+a>b)
    #print(YES, those side lenghts create a triangle)

#if False:
    #print(NO, those side lengths dont create a triangle)

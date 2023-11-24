from turtle import *
import turtle
import math

#Start Menu with User Options for which program they want to execute
def start():
    options = ["1","2","3"]
    userInput = ""
    showOptions = ["1","2"]
    continueProgram = ""
    print("\nHIT137 Assignment 01\nSELECT A PROGRAM\n")
    while True:
        
        #Re-occouring an input untill a valid input is entered
        while userInput not in options:
            userInput = input("1) Triangle Checker\n2) Square Builder\n3) Exit\n\nProgram Number: ")

        #Defining Option 1 - Triangle Checker
        if userInput == "1":
            values = triLengths()
            values = [float(i) for i in values]
            triCheck(values)
            restartProgram()
            return
            
        #Defining Option 2 - Square Builder
        if userInput == "2":
            print("\nRUNNING SQUARE MAKER\n")
            squareTest = True
            while squareTest == True:
                try:
                    size = int(input("Please input your desired Square Size: "))
                    if size <= 0:
                        raise ValueError()
                    else:
                        break
                except ValueError:
                    print("Please enter a whole number that is greater than 0")
                else:
                    print(size)
                    sqaureTest = False
            makeSquare(size)
            restartProgram()
            return

        #Defining Option 3 - Exit
        if userInput == "3":
            print("Exiting")
            return
        
#Define restart function to continue if the User wants
def restartProgram():
    showOptions = ["1","2"]
    toContinue = input("\nWould you like to restart?\n\n1) Yes\n2) No\n")
    while toContinue not in showOptions:
        toContinue = input("\nWould you like to restart?\n\n1) Yes\n2) No\n")
    if toContinue == "1":
            start()
    if toContinue == "2":
            return

#Defining the Triangle's 3 side lengths based on a User's Input
def triLengths():
    print("\nRUNNING TRIANGLE CHECKER\nPlease input 3 numbers as the side lengths for your triangle")
    val = [0,0,0]
    #To test if the inputted side values are numbers and greater than 0
    for i in range(len(val)):
        testing = True
        while testing == True:
            try:
                value = float(input("Length "+str(i+1)+": "))
                if value <= 0:
                    raise ValueError()
            except ValueError:
                print("Please enter a number that is greater than 0")
            else:
                val[i] = value
                testing = False    
    return sorted(val)

#Triangle Validator which cheks whether the Triangle is valid 
def triCheck(values):
    
    #As the values are already sorted, we now check the two lower values against the greatest value
    if((values[0] + values[1]) < values[2]):
        print("\nFailed testing:",values[0],"+", values[1], "is less than", values[2])
    else:
        #Calcualte the triangle's angles based on the inputted side lengths
        angle1= round(math.acos(((values[0]**2+values[2]**2)-values[1]**2)/(2*values[0]*values[2]))*180/math.pi,3)
        angle2= round(math.acos(((values[0]**2+values[1]**2)-values[2]**2)/(2*values[0]*values[1]))*180/math.pi,3) 
        angle3= round(math.acos(((values[1]**2+values[2]**2)-values[0]**2)/(2*values[1]*values[2]))*180/math.pi,3)
        angles = [angle1, angle2, angle3]
        #Define the type of Triangle based on their internal angles
        if 90 in angles:
            type="Right"
        elif max(angles) > 90:
            type="Obtuse"
        else:
            type="Acute"
        print("\nYes, these lengths can make a valid triangle\nThey create a "+type+" Triangle with sides lengths of "+str(values)+" and internal angles of "+str(angles))
        #Provide an option to view triangle drawn
        showOptions = ["1","2"]
        show = input("\nWould you like to see this triangle drawn?\n1) Yes\n2) No\n")
        while show not in showOptions:
            show = input("\nWould you like to see this triangle drawn?\n\n1) Yes\n2) No\n")
        if show == "1":
            draw(values,angles,type)

def draw(values,angles,type):
    #Define the function to draw the Triangle, setting the details, colour and font
    screen = Screen()
    width = values[2]*20+200
    height = values[1]*20+200
    screen.setup(width,height)
    screen.setworldcoordinates(0,0, width,height)
    try:
        t = Turtle()
    except:
        t = Turtle()
    t.up()
    t.goto((width/2)+(values[2]*20/2),height/6-(values[1]/3))
    t.down()
    t.color("#0089cd")
    t.fillcolor("#9acdff")
    t.begin_fill()
    t.width(2)

    #Draw the Triangle, multiplying the side lengths to scale into a visible size for the picture. 
    for x in range(3):
        t.write(str(angles[x])+"°",font=("Verdana",10,"normal"))
        t.left(180-angles[x])
        t.forward(values[x]/2*20)
        t.write(values[x],font=("Verdana",20,"normal"))
        t.forward(values[x]/2*20)
    t.hideturtle()
    t.end_fill()
    t.up()
    t.goto(width/2,height*0.9)
    t.write("Type of triangle is: "+type,align="center",font=("Verdana",15,"normal"))
    turtle.done()
    return            
    
#Square Builder function, taking user inputs for the boarders and interior.
def makeSquare(size):
    border = input("What would you like the border of the square to be built out of?\n")

    #Error check to ensure only one character is entered by the User
    while len(border) != 1:
        border = input("Please enter onle one character")
    inner = input("What would you like the inside of the square to be built out of?\n")
    while len(inner) != 1:
        inner = input("Please enter only one character")

    #Define Columns
    for i in range(size):
        #Define Rows
        for x in range(size):
            #Set any as a part of the board if their position is in first or last position of a column or a row
            if  i == 0 or i == (size-1) or x == 0 or x == (size-1):
                print(border, end =" ")
            #Set the remaining items as the middle of the square
            else:
                print(inner, end =" ")
        #Separating rows by ending the current row and starting a new line
        print()

start()
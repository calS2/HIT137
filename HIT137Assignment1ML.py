from turtle import *
import turtle
import math

#Input for 3 Triangles
def triLengths():
    print('RUNNING TRIANGLE CHECKER\nPlease input 3 different lengths')
    #invalid number message
    error = "Only accepts numbers above 0"
    val1 = input("Length 1: ")
    #Test if values are numbers and above 0
    while not val1.isnumeric() or float(val1) < 1:
        print(error)
        val1 = input("Length 1: ")
    val2 = input("Length 2: ")
    while not val2.isnumeric() or float(val2) < 1:
        print(error)
        val2 = input("Length 2: ")
    val3 = input("Length 3: ")
    while not val3.isnumeric() or float(val3) < 1:
        print(error)
        val3 = input("Length 3: ")
    return int(val1), int(val2), int(val3)

#Triangle Validator 
def triCheck(values):
    #Old method
    #A + B > C
    #A + C > B
    #B + C > A
    '''if (values[0] + values[1]) < values[2]:
        print("Failed testing:",values[0],"+", values[1], "is less than", values[2])
    elif (values[0] + values[2]) < values[1]:
        print('2')
        print("Failed testing:",values[0],"+", values[2], "is less than", values[1])
    elif (values[1] + values[2]) < values[0]:
        print('3')
        print("Failed testing:",values[1],"+", values[2], "is less than", values[0])
    else:
        print("Yes, these three lengths can for a triangle")
    '''
    #Sorted values means we only need to check the lowest against values
    if((values[0] + values[1]) < values[2]):
        print("Failed testing:",values[0],"+", values[1], "is less than", values[2])
    else:
        print("Yes, these three lengths can work for a triangle")
        #option to view triangle
        showoptions = ['1','2']
        show = input("Would you like to see this triangle drawn?\n1) Yes\n2) No\n")
        while show not in showoptions:
            show = input("Would you like to see this triangle drawn?\n1) Yes\n2) No\n")
        if show == "1":
            #calcualte angles
            angle1= round(math.acos(((values[0]**2+values[2]**2)-values[1]**2)/(2*values[0]*values[2]))*180/math.pi,3)
            angle2= round(math.acos(((values[0]**2+values[1]**2)-values[2]**2)/(2*values[0]*values[1]))*180/math.pi,3) 
            angle3= round(math.acos(((values[1]**2+values[2]**2)-values[0]**2)/(2*values[1]*values[2]))*180/math.pi,3)
            angles = [angle1, angle2, angle3]
            print(angles)
            if 90 in angles:
                type="Right"
            elif max(angles) > 90:
                type="Obtuse"
            else:
                type="Acute"
            #Turtle Parameters
            screen = Screen()
            width = values[2]*20+200
            height = values[1]*20+200
            screen.setup(width,height)
            screen.setworldcoordinates(0,0, width,height)
            t = Turtle()
            t.up()
            t.goto((width/2)+(values[2]*20/2),height/6-(values[1]/3))
            t.down()
            t.color('#0089cd')
            t.fillcolor('#9acdff')
            t.begin_fill()
            t.width(2)

            #draw Triangle, multiplying for scaling reason. 
            for x in range(3):
                t.write(str(angles[x])+"°",font=("Verdana",10,'normal'))
                t.left(180-angles[x])
                t.forward(values[x]/2*20)
                t.write(values[x],font=("Verdana",20,'normal'))
                t.forward(values[x]/2*20)
            t.hideturtle()
            t.end_fill()
            t.up()
            t.goto(width/2,height*0.9)
            t.write("Type of triangle is: "+type,align='center',font=("Verdana",15,'normal'))
            turtle.done()
            return
        
    
#Square Builder using Columns and Rows
def makeSquare(size):
    border = input("What would you like the square border to be built out of?\n")
    while len(border) != 1:
        border = input("Please only enter 1 character")
    inner = input("What would you like the square insides to be built out of?\n")
    while len(inner) != 1:
        inner = input("Please only enter 1 character")
    #Test if values are numbers and above 0
    while not size.isnumeric() or int(size) < 1:
        size = input("Enter a positive whole number\n")
    size = int(size)
    #Columns
    for i in range(size): 
        #Row
        for x in range(size):
            #test if in first or last column or row
            if  i == 0 or i == (size-1) or x == 0 or x == (size-1):
                print(border, end =" ")
            #anything else must be middle
            else:
                print(inner, end =" ")
        #separate next rowV B
        print()  

def start():
    options = ['1','2','3']
    userinput = ''
    print('HIT137 Assignment 01\nSELECT A PROGRAM\n')
    while True:
        #Reoccouring input till valid input
        while userinput not in options:
            userinput = input('1) Triangle Checker\n2) Square Builder\n3) Exit\n')

        #Option 1
        if userinput == '1':
            values = sorted(triLengths())
            print(values)
            values = [int(i) for i in values]
            triCheck(values)
            return
            
        #Option 2
        if userinput == '2':
            size = input('RUNNING SQUARE1 MAKER\nPlease input Square Size\n')
            makeSquare(size)
            return

        #Option 3
        if userinput == '3':
            print('Exiting')
            return
        
start()
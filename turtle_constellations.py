import turtle


print 'Welcome lets draw the Great Bear Constellation'
print 'Using a turtle'
print 'Please choose an option:'

print '1. Great Bear Cosntelattion seem from earth'
print '0. Exit'

opt = input()

if opt == 1:

    # Configuring the turtle

    window = turtle.Screen()

    turtle.setup(800, 800)

    t = turtle.Turtle()
    # Put label on the  top
    #t.tiltle("Great Bear constellation")
    # Selecting Turtle shape
    t.shape("turtle")
    # Selecting color of my turtle
    t.color("green")
    t.pen()

    ############################################################################################
    # This is a  draw of teh  Great Bear Cosntelattion seem from earth

    t.dot()

    t.left(5)
    t.forward(100)
    t.dot()

    t.right(45)
    t.forward(100)
    t.dot()

    t.right(7)
    t.forward(50)
    t.dot()

    t.right(30)
    t.forward(50)
    t.dot()

    t.left(82)
    t.forward(100)
    t.dot()

    t.left(70)
    t.forward(50)
    t.dot()

    # Thats it
    ############################################################################################

    turtle.exitonclick()

elif opt == 0:
    print('Bye bitch!')

else:
    print('Error check it out!')

import turtle
#this assigns colors to the design
#example: col=('red','blue','green','cyan','purple')
col=('red','blue','yellow','green')
#creating canvas
t=turtle.Turtle()
#here we are defining a screen and a background color with printing speed.
screen=turtle.Screen()
screen.bgcolor('black')
t.speed(50)

#this range gives number of lines for the design to be printed
#here i am printing 100 lines.
for i in range (100):
    #{i%2 mentions the " number of lines i.e.,"i"}' % '{number of colors mentioned above in the 'col=('colors','colors',...)}".
    #here i am taking 4 colors so i use 4 below.
    t.color(col[i%4])
    #this line states the space between each line of the patter printed.
    t.forward(i*5)
    #this line states the movement of the pattern i.e., from left-right or from right-left.
    # here the value 240 prints a triangle so, replace (240) with the below values to print different patterns
    t.right(240)
    t.width(2)
    # in t.right(240) u can replace the below values
    # (180) to print a straight line like an interface of loading theme.
    # (160)to print a star of 8 sides.
    # (150)to print a star of 12 sides.
    # (144) to print a star
    # (120)to prit an inverted triangle.
    # (90) or to print a square.
    # (72)to print pentagon
    # (60)to print hexagon
    # (45)to print octagon
    # give your values to print some other designs.



from turtle import *

speed('fastest')
pensize(2)
bgcolor('black')
pencolor('yellow')
# colors=['red','yellow','blue','green','orange','purple']
colors=['white','white','red','blue','blue','red']
side = 6
for i in range(side):
    fd(200)
    for i in range(side):
        fd(100)
        lt(360/side)
        begin_fill()
        fillcolor(colors[i%6])
        for i in range(side):
            fd(50)
            lt(360/side)
        end_fill()    
    lt(360/side) 
fd(200)   

hideturtle()    
mainloop()
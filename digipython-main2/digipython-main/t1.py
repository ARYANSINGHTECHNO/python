from turtle import *

speed('slowest')
pencolor('red')

# range(stop)

for i in range(6,40, 5):
    fd(120)
    lt(60)
    dot(10, 'green')
    write(i, font=('Calibri', 20, 'bold'))

    #reverse
    goto(100,100)
    for i in range(10,0,-1):
        fd(60)
        lt(60)
        dot(20, 'red')
        write(i, front=('calibri',20,'bold'))



mainloop()
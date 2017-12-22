from turtle import *
def star(size):
    for i in 1,2,3,4,5:
        forward(size)
        right(180 - 180/5)

reset()
star(100)
color('green')
begin_fill()
star(50)
end_fill()
while (1):
    input()


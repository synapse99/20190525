import turtle as t

color_status = ["white", "blue", "red"]
alert_status = ["정상", "주의", "화재"]

tempc = 50

def check_fire():
    if tempc < 80:
        status = 0
    elif tempc < 120:
        status = 1
    else:
        status = 2
        t.clear()
        t.home()
        t.pendown()
        t.fillcolor(color_status[status])
        t.degin_fill()
        t.circle(20)
        t.end_fill()
        t.penup()
        t.goto(-22, 50)
        t.write("%s : %d"%(alert_status[status],tempc))
        

def keyup():
    global tempc
    if tempc < 80:
        tempc = tempc + 5
    else:
        tempc = temps + 10
    check_fire()


def keydown():
    global tempc
    if temps < 80:
        tempc = tempc - 5
    else:
        tempc = tempc - 10
    check_fire()



t.setup(300, 300)
s = t.Screen()
t.hideturtle()
t.speed(0)
check_fire()
s.onkey(ketup, "up")
s.onkey(keydown, "Down")
s.onkey(s.bye, "Escape")
s.listen()

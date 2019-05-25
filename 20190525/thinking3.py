import turtle as t
s7seg_img = ["7s0.gif","7s1.gif","7s2.gif","7s3.gif","7s4.gif",
             "7s5.gif","7s6.gif","7s7.gif","7s8.gif","7s9.gif","7s10.gif"]

def disp_num(k):
         t.shape(s7seg_img[k])
         t.stamp()

def key_0():
         disp_num(0)
def key_1():
         disp_num(1)
def key_2():
         disp_num(2)
def key_3():
         disp_num(3)
def key_4():
         disp_num(4)
def key_5():
         disp_num(5)
def key_6():
         disp_num(6)
def key_7():
         disp_num(7)
def key_8():
         disp_num(8)
def key_9():
         disp_num(9)
def key_10():
         disp_num(10)

t.setup(400,400)
s = t.Screen()
t.hideturtle()
t.speed(0)

for i in range(11):
         s.addshape(s7seg_img[i])

disp_num(10)


s.onkeypress(key_0,"0")
s.onkeypress(key_1,"1")
s.onkeypress(key_2,"2")
s.onkeypress(key_3,"3")
s.onkeypress(key_4,"4")
s.onkeypress(key_5,"5")
s.onkeypress(key_6,"6")
s.onkeypress(key_7,"7")
s.onkeypress(key_8,"8")
s.onkeypress(key_9,"9")
#s.onkeypress(key_10,"r")

s.onkeyrelease(key_10,"0")
s.onkeyrelease(key_10,"1")
s.onkeyrelease(key_10,"2")
s.onkeyrelease(key_10,"3")
s.onkeyrelease(key_10,"4")
s.onkeyrelease(key_10,"5")
s.onkeyrelease(key_10,"6")
s.onkeyrelease(key_10,"7")
s.onkeyrelease(key_10,"8")
s.onkeyrelease(key_10,"9")
s.listen()

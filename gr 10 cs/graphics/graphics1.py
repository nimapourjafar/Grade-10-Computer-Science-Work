from graphics import *
#ex 1
win = GraphWin("Ex1",200,200)
rect = Rectangle(Point(60,130), Point(100,90))
rect.setOutline('green')
rect.draw(win)
line1 = Line(Point(60,130),Point(100,90))
line1.setFill('green')
line1.draw(win)
line2 = Line(Point(60,90),Point(100,130))
line2.setFill("green")
line2.draw(win)
# win.mainloop()

#ex 2
win2 = GraphWin("ex2",250,250)
line1 = Line(Point(160,230),Point(160,190))
line1.setFill('green')
line1.draw(win2)
line2 = Line(Point(160,230),Point(180,190))
line2.setFill('green')
line2.draw(win2)
line3 = Line(Point(160,230),Point(200,190))
line3.setFill('green')
line3.draw(win2)
line4 = Line(Point(160,230),Point(210,210))
line4.setFill('green')
line4.draw(win2)
line5 = Line(Point(160,230),Point(220,230))
line5.setFill('green')
line5.draw(win2)
# win2.mainloop()
#ex 3
win3 = GraphWin('ex3',400,400)
rect1 = Rectangle(Point(260,330),Point(300,290))
rect1.setOutline('green')
rect1.draw(win3)
rect2 = Rectangle(Point(260,330),Point(290,300))
rect2.setOutline('green')
rect2.draw(win3)
rect3 = Rectangle(Point(260,330),Point(280,310))
rect3.setOutline('green')
rect3.draw(win3)
rect4 = Rectangle(Point(260,330),Point(270,320))
rect4.setOutline('green')
rect4.draw(win3)
win3.mainloop()
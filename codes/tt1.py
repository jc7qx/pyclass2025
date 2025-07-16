#導入 turtle 套件
import turtle
#建立畫布
win = turtle.Screen()
#建立小烏龜
tt = turtle.Turtle()
#清除畫布
win.clear()
#重置繪圖狀態
#turtle go

tt.reset
tt.forward(100)
tt.left(45)
tt.forward(100)
tt.left(90)
tt.forward(100)
tt.pencolor("red")
tt.left(70)
tt.forward(100)
tt.right(70)
tt.pencolor("blue")
tt.forward(100)
tt.right(60)
tt.pencolor("green")
tt.forward(100)
tt.left(120)
tt.forward(200)
tt.right(75)
tt.pencolor("purple")
tt.forward(100)
tt.pencolor("black")
tt.home()

win.exitonclick()
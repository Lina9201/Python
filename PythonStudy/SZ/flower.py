# 海龟绘图
import turtle

def draw_diamond(turt):
    for i in range(1, 3):
        turt.forward(100)
        turt.right(45)
        turt.forward(100)
        turt.right(135)


# 创建画布
def draw_art():
    # 获得一个窗口句柄
    window = turtle.Screen()
    # 将背景设置为蓝色
    window.bgcolor("blue")

    # 创建实例
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("red")
    brad.speed("slow")

    for i in range(1, 37):
        draw_diamond(brad)
        brad.right(10)
    brad.right(90)
    brad.forward(300)
    # 当点击下窗口的时候会自动关闭
    window.exitonclick()

draw_art()

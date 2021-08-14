import turtle as T
import random as R
import matplotlib.pyplot as plt


T.speed(0)
T.hideturtle()
colors = ['SteelBlue', 'DodgerBlue', 'DeepSkyBlue', 'MediumBlue', 'CornflowerBlue',
          'DarkBlue', 'RoyalBlue', 'CadetBlue', 'blue', 'LightSeaGreen', 'SkyBlue4', 'NavyBlue']
snowflakes = []
color = "light blue"
counter = []
tests = 3000
number_of_snowflakes = 150

T.Screen().setup(1300, 700)
T.Screen().bgcolor("light blue")

def draw_circle(x, y, r):
    T.penup()
    T.color(color)
    T.fillcolor(color)
    T.goto(x,y)
    T.pendown()
    T.begin_fill()
    T.circle(r)
    T.end_fill()

def drawing_1(x_c, y_c, size):
    size -= size % 4
    T.pencolor(colors[R.randrange(len(colors))])
    T.penup()
    T.goto(x_c, y_c)
    T.pendown()
    T.dot()
    T.speed(0)
    for i in range(8):
        for i in range(3):
            T.forward(size // 4)
            T.right(45)
            T.forward(size // 4)
            T.backward(size // 4)
            T.left(90)
            T.forward(size // 4)
            T.backward(size // 4)
            T.right(45)
        T.forward(size // 4)
        T.backward(size)
        T.left(45)
    snowflakes.append((x_c, y_c, size))
    print(len(counter) + 1, cnt)
    counter.append(cnt)

def drawing_2(x_c, y_c, size):
    size -= size % 3
    T.pencolor(colors[R.randrange(len(colors))])
    T.penup()
    T.goto(x_c, y_c)
    T.pendown()
    T.dot()
    T.speed(0)
    T.dot(size//8)
    for i in range(8):
        T.forward(size // 3)
        T.left(45)
        T.forward(size // 8)
        T.backward(size // 8)
        T.right(90)
        T.forward(size // 8)
        T.backward(size // 8)
        T.left(45)
        T.forward(size // 3)
        T.left(45)
        T.forward(size // 3)
        T.backward(size // 3)
        T.right(90)
        T.forward(size // 3)
        T.backward(size // 3)
        T.left(45)
        T.forward(size // 3)
        T.dot(size // 8)
        T.backward(size)
        T.left(45)
    snowflakes.append((x_c, y_c, size))
    print(len(counter) + 1, cnt)
    counter.append(cnt)

def drawing_3(x_c, y_c, size):
    size -= size % 3
    T.pencolor(colors[R.randrange(len(colors))])
    T.penup()
    T.goto(x_c, y_c)
    T.pendown()
    T.dot()
    T.speed(0)
    T.dot(size // 8)
    for i in range(8):
        T.forward(size // 3)
        T.left(45)
        T.forward(size // 8)
        T.backward(size // 8)
        T.right(90)
        T.forward(size // 8)
        T.backward(size // 8)
        T.left(45)
        T.forward(size // 3)
        T.left(45)
        T.forward(size // 3)
        T.backward(size // 3)
        T.right(90)
        T.forward(size // 3)
        T.backward(size // 3)
        T.left(45)
        T.forward(size // 3)
        T.dot(size // 8)
        T.backward(size)
        T.left(45)
    size -= size % 4
    T.pencolor(colors[R.randrange(len(colors))])
    T.penup()
    T.goto(x_c, y_c)
    T.pendown()
    T.dot()
    T.speed(0)
    for i in range(8):
        for i in range(3):
            T.forward(size // 4)
            T.right(45)
            T.forward(size // 4)
            T.backward(size // 4)
            T.left(90)
            T.forward(size // 4)
            T.backward(size // 4)
            T.right(45)
        T.forward(size // 4)
        T.backward(size)
        T.left(45)
    snowflakes.append((x_c, y_c, size))
    print(len(counter) + 1, cnt)
    counter.append(cnt)

def check(x_c, y_c, r):
    if x_c > abs(r - 650) or y_c > abs(r - 350):
        return False
    for i in range(len(snowflakes)): #(x, y, r)
        if (x_c - snowflakes[i][0]) ** 2 + (y_c - snowflakes[i][1]) ** 2 <  (snowflakes[i][2] + r) ** 2 :
            return False
    return True


for i in range(number_of_snowflakes):
    T.width(R.randrange(1, 3))
    x_c = R.uniform(-650, 650)
    y_c = R.uniform(-350, 350)
    r = R.randrange(T.width() * 10 + 20, T.width() * 20 + 40)
    #r = R.randrange(4, T.width() * 20 + 40)
    cnt = 0
    if check(x_c, y_c, r):
        j = R.randint(0, 2)
        if j == 1:
            drawing_1(x_c, y_c, r)
        elif not j:
            drawing_2(x_c, y_c, r)
        else:
            drawing_3(x_c, y_c, r)
    cnt = 0
    while not check(x_c, y_c, r) and cnt < tests:
        x_c = R.uniform(-650, 650)
        y_c = R.uniform(-350, 350)
        r = R.randrange(T.width() * 10 + 10, T.width() * 20 + 40)
        #r = R.randrange(4, T.width() * 20 + 40)
        cnt += 1
    if cnt >= tests:
        counter.append(cnt)
        R.shuffle(snowflakes)
        x, y, r = snowflakes[0]
        draw_circle(x, y - r, r + r//8)
        del snowflakes[0]
    else:
        j = R.randint(0, 2)
        if j == 1:
            drawing_1(x_c, y_c, r)
        elif not j:
            drawing_2(x_c, y_c, r)
        else:
            drawing_3(x_c, y_c, r)
        cnt = 0

plt.title("Dependence of the number of attempts on the number of required generations")
plt.plot(range(len(counter)), counter)
plt.show()
T.done()

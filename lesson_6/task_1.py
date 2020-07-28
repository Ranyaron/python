import time
import turtle


class TrafficLight:
    __color = ['red', 'yellow', 'green']

    def __visualization(self, x=0, y=0, color='#808080', radius=50):
        t = turtle
        t.ht()
        t.speed(0)
        t.pensize(3)
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.begin_fill()
        t.fillcolor(color)
        t.circle(radius)
        t.end_fill()

    def running(self):
        self.__visualization(0, 85)
        self.__visualization(0, -25)
        self.__visualization(0, -135)
        red = TrafficLight.__color[0]
        yellow = TrafficLight.__color[1]
        green = TrafficLight.__color[2]
        while True:
            if red != 'red':
                print('Out of order!')
                break
            self.__visualization(0, 85, red)
            time.sleep(7)
            self.__visualization(0, 85)

            if yellow != 'yellow':
                print('Out of order!')
                break
            self.__visualization(0, -25, yellow)
            time.sleep(2)
            self.__visualization(0, -25)

            if green != 'green':
                print('Out of order!')
                break
            self.__visualization(0, -135, green)
            time.sleep(7)
            self.__visualization(0, -135)

            if yellow != 'yellow':
                print('Out of order!')
                break
            self.__visualization(0, -25, yellow)
            time.sleep(0.4)
            self.__visualization(0, -25)
            time.sleep(0.4)
            self.__visualization(0, -25, yellow)
            time.sleep(0.4)
            self.__visualization(0, -25)
            time.sleep(0.4)
            self.__visualization(0, -25, yellow)
            time.sleep(0.4)
            self.__visualization(0, -25)

            # print(f'\033[31m{TrafficLight.__color[0]}')
            # time.sleep(7)
            # print(f'\033[33m{TrafficLight.__color[1]}')
            # time.sleep(2)
            # print(f'\033[32m{TrafficLight.__color[2]}')
            # time.sleep(7)
            # print(f'\033[33m{TrafficLight.__color[1]}')
            # time.sleep(2)


traffic_light = TrafficLight()
traffic_light.running()

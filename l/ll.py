import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
ball, = plt.plot([], [], 'o', color='r', label='Ball')
line, = plt.plot([], [], '-')


#Задающиеся параметры точку
F = 100
m = 20
g = 9.81
l = 1

#Угол максимального отклонения
d = F/m/g
k = math.asin(d)
LR = k*(180/np.pi)
print(LR)


#Точки максимального отклонения из положения равновесия
L = 3*np.pi/2 - ((np.pi/2)/90)*LR
R = 3*np.pi/2 + ((np.pi/2)/90)*LR
#Массивы значений x для точек максимального отклонения справа и слева
s = np.arange(R, L, -0.05)
v = np.arange(L, R, 0.05)
T = []


#Создание массива значений x
def EE(s, v):
    for i in range(len(s)-1, 0, -1):
        h = s[i]
        T.append(h)
    for i in range(len(v)-1, 0, -1):
        j = v[i]
        T.append(j)
    return T
EE(s, v)


#Период колебаний
Tc = 2*np.pi*(0.5**(l/g))
itr = (Tc/len(T))*1000


#Координаты движения точки
def ball_move(x):
    x=x
    y=np.sin(x)
    return x, y


l = 1

#Интервал
Tc = 2*np.pi*(0.5**(l/g))
itr = (Tc/len(T))*1000
print(itr)


#Координаты линии
def line_move(t):
    alpha = np.arange(0, np.pi/2, 0.1)
    R = 0.8
    x = R*np.cos(alpha)
    y = R*np.cos(alpha)

    X = y*np.sin(t+np.pi/4)+x*np.cos(t+np.pi/4)+3*np.pi/2
    Y = x*np.sin(t+np.pi/4)-y*np.cos(t+np.pi/4)
    return X, Y

#Пределы
ax.set_xlim(2.5,np.pi*2+0.5)
ax.set_ylim(-2, 1)


#Анимация
def animater(i):
    line.set_data(line_move(t=i))
    ball.set_data(ball_move(x=i))
    	
ani = FuncAnimation(fig, animater, frames=T, interval=itr)
 
ani.save('i.gif')

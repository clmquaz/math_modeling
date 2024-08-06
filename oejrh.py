
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

frame = 5000
seconds_in_day = 24 * 60 * 60
days = 687
t = np.linspace(0, days * seconds_in_day, frame)

G = 6.67 * 10 ** (-11)
N:int = 0

"""
                                        Обястнение list[n * a + b]
n - номер элемента листа из которого мы хотим получить данные
a - переод list 
Переод - это количесво вставляемых подрят данных одного объекта моделирования в определённый лист
b - какие данные элемента мы хотим получить
"""


def get_dv_xdt(variable_balls: tuple, num: int):
    """
    :param variable_balls - все объекты моделирования
    :param num - номер объекта на который дейсвуют другие тела
    :return out: взаимодействие variable_balls элементов на num-ый элемент по x
    """

    out = 0.0

    for i in range(N):
        if i != num:
            # Вычисляем гравитационное взаимодействие variable_balls элементов на num-ый элемент
            out += (-G * not_variable_balls[i + 0] *
                    (variable_balls[num * 6 + 0] - variable_balls[i * 6 + 0]) /
                    ((variable_balls[num * 6 + 0] - variable_balls[i * 6 + 0]) ** 2 + (
                            variable_balls[num * 6 + 2] - variable_balls[i * 6 + 2]) ** 2 + (
                                    variable_balls[num * 6 + 4] - variable_balls[i * 6 + 4]) ** 2) ** 1.5)

    return out


def get_dv_ydt(variable_balls: tuple, num: int):
    """
    :param variable_balls: все объекты моделирования
    :param num: номер объекта на который дейсвуют другие тела
    :return out: взаимодействие variable_balls элементов на num-ый элемент по y
    """

    out = 0.0

    for i in range(N):
        if i != num:
            # Вычисляем гравитационное взаимодействие variable_balls элементов на num-ый элемент
            out += (-G * not_variable_balls[i + 0] *
                    (variable_balls[num * 6 + 2] - variable_balls[i * 6 + 2]) /
                    ((variable_balls[num * 6 + 0] - variable_balls[i * 6 + 0]) ** 2 + (
                            variable_balls[num * 6 + 2] - variable_balls[i * 6 + 2]) ** 2 + (
                                    variable_balls[num * 6 + 4] - variable_balls[i * 6 + 4]) ** 2) ** 1.5)


    return out


def get_dv_zdt(variable_balls: tuple, num: int):
    """
    :param variable_balls: все объекты моделирования
    :param num: номер объекта на который дейсвуют другие тела
    :return out: взаимодействие variable_balls элементов на num-ый элемент по y
    """

    out = 0.0

    for i in range(N):
        if i != num:
            # Вычисляем гравитационное взаимодействие variable_balls элементов на num-ый элемент
            out += (-G * not_variable_balls[i + 0] *
                    (variable_balls[num * 6 + 4] - variable_balls[i * 6 + 4]) /
                    ((variable_balls[num * 6 + 0] - variable_balls[i * 6 + 0]) ** 2 + (
                            variable_balls[num * 6 + 2] - variable_balls[i * 6 + 2]) ** 2 + (
                                    variable_balls[num * 6 + 4] - variable_balls[i * 6 + 4]) ** 2) ** 1.5)


    return out


def move_func(variable, t):
    """
    :param variable: все изменияемые данные объектов моделирования
    :param t: linspace переода времяни
    :return: outs: решение диференциального уравнения
    """

    # Лист возвращяемых данных
    # Переод = 4
    # Элементы объекта: 0 = dxdt, 1 = dv_xdt, 2 = dydt, 3 = dv_ydt
    outs = []

    # Для каждего моделируемого объекта вычислем возвращяемые даннные
    for j in range(N):
        # Вычисляем dxdt
        outs.append(variable[j * 6 + 1])
        # Вычисляем dv_xdt
        outs.append(get_dv_xdt(variable, j))
        # Вычисляем dydt
        outs.append(variable[j * 6 + 3])
        # Вычисляем dv_ydt
        outs.append(get_dv_ydt(variable, j))
        # Вычисляем dydt
        outs.append(variable[j * 6 + 5])
        # Вычисляем dv_ydt
        outs.append(get_dv_zdt(variable, j))
        
    return outs


# Лист не изменяемых данных моделируемых объектов
# Период = 2
# Данные одного моделируемого объекта: 0 = масса, 1 = зарят
not_variable_balls = []

# Лист изменяемых данных моделируемых объектов
# Период = 4
# Данные одного моделируемого объекта: 0 = x, 1 = вектор x, 2 = y, 3 = вектор y
variable = []


def ball(mas: float, x: float, v_x: float, y: float, v_y: float, z: float, v_z: float):
    """
    Распределяет данные моделируемых объктов по листам
    :param mas: масса
    :param x: координата x
    :param v_x: вектор по x
    :param y: координата y
    :param v_y: вектор по y
    """
    not_variable_balls.append(mas)
    variable.append(x)
    variable.append(v_x)
    variable.append(y)
    variable.append(v_y)
    variable.append(z)
    variable.append(v_z)


# Добавляем объекты моделирования

i_m = 1.84*np.pi/180
i_mer = 7.01*np.pi/180

x_m = 1.381*149 * 10 ** 9
x_mer = 0.3075*149 * 10 ** 9

v_m = 26500
v_mer = 58978


# i_p = 7.01*np.pi/180

# x_m = 5*10**9
# x_p = 149 * 10 ** 9

# v_m = 25759.1
# v_p = 30978

# print(v_p*np.cos(i_p), x_p*np.sin(i_p), v_p*np.sin(i_p))
# Звезда
ball(2 * 10 ** 30, 0, 0, 0, 0, 0, 0)

# ball(2 * 10 ** 30, x_m, 0, 0, v_m, 0, 0)
# ball(2 * 10 ** 30, -x_m, 0, 0, -v_m, 0, 0)
# ball(6 * 10 ** 24, x_p, 0, 0,  v_p*np.cos(i_p), x_p*np.sin(i_p), v_p*np.sin(i_p))
# print(v_p*np.cos(i_p))
# print(x_p*np.sin(i_p))
# print(v_p*np.sin(i_p))

ae = 149 * 10 ** 9
k = 3.6**-1 

ball(6.39 * 10 ** 23, 0.10725*ae, 0, 0, 363255*k, 0.01317*ae, 44602*k)
ball(6 * 10 ** 24, 0.08514*ae, 0, 0, 341319*k, 0.03614*ae, 144881*k)
ball(6 * 10 ** 24, 0.20323*ae, 0, 0, 239804*k, 0.0053*ae, 6280*k)
ball(6 * 10 ** 24, 0.52113*ae, 0, 0, 158069*k, 0.05165*ae, 15666*k)
ball(3.29 * 10 ** 23, 0.072083*ae, 0, 0, 520087*k, 0.005964*ae, 43033*k)



# Вычисляем сколько всего мы моделируем объектов
N = int(len(not_variable_balls))

# Моделируем
sol = odeint(move_func, variable, t)


def solve_func(n: int):
    """
    :param i: время в которое мы берём координаты
    :param n: номер моделируемого объекта для которого мы получаем координаты
    :param key: ключь. Если key="point", то получам координаты для моделирования точьки
        в ином случае получае координаты для моделирования пути моделирукмого объекта
    :return x, y: n-го моделируемого элемента в i-е время
    """
    
    x = sol[:, n * 6 + 0]
    y = sol[:, n * 6 + 2]
    z = sol[:, n * 6 + 4]
    return x, y, z




x1 = solve_func(1)[0]
y1 = solve_func(1)[1]
z1 = solve_func(1)[2]

x3 = solve_func(3)[0]
y3 = solve_func(3)[1]
z3 = solve_func(3)[2]

x2 = solve_func(2)[0]
y2 = solve_func(2)[1]
z2 = solve_func(2)[2]

x4 = solve_func(4)[0]
y4 = solve_func(4)[1]
z4 = solve_func(4)[2]

x5 = solve_func(5)[0]
y5 = solve_func(5)[1]
z5 = solve_func(5)[2]

x_s = solve_func(0)[0]
y_s = solve_func(0)[1]
z_s = solve_func(0)[2]

# Вращение вокруг оси z (аргумент перицентра) 

w_m = 286.46*np.pi/180
w_mer = 29.12*np.pi/180

# x_e = x_e*np.cos(w_m) - y_e*np.sin(w_m) 
# y_e = x_e*np.sin(w_m) + y_e*np.cos(w_m) 
# z_e = z_e 

w_1 = 7*np.pi/180
w_2 = 23*np.pi/180
w_3 = 1.5*np.pi/180
w_4 = 5.66*np.pi/180
w_5 = 4.73*np.pi/180

x_1 = x1*np.cos(w_1) - y1*np.sin(w_1) 
y_1 = x1*np.sin(w_1) + y1*np.cos(w_1) 
z_1 = z1 
x_2 = x2*np.cos(w_2) - y2*np.sin(w_2) 
y_2 = x2*np.sin(w_2) + y2*np.cos(w_2) 
z_2 = z2
x_3 = x3*np.cos(w_3) - y3*np.sin(w_3) 
y_3 = x3*np.sin(w_3) + y3*np.cos(w_3) 
z_3 = z3 
x_4 = x4*np.cos(w_4) - y4*np.sin(w_4) 
y_4 = x4*np.sin(w_4) + y4*np.cos(w_4) 
z_4 = z4 
x_5 = x5*np.cos(w_5) - y5*np.sin(w_5) 
y_5 = x5*np.sin(w_5) + y5*np.cos(w_5) 
z_5 = z5 


# print(f'max_x = {max(x_m)/(149*10**9)}')
# print(f'min_x = {min(x_m)/(149*10**9)}')
# print(f'max_y = {max(y_m)/(149*10**9)}')
# print(f'min_y = {min(y_m)/(149*10**9)}')
# print(f'max_z = {max(z_m)/(149*10**9)}')
# print(f'min_z = {min(z_m)/(149*10**9)}')

# fig = plt.figure(figsize=(30,30))
# ax = fig.add_subplot(111, projection='3d')
# ax.plot(x_m, y_m, z_m, color='red')
# ax.plot(x_e, y_e, z_e, color='blue')
# ax.plot(x_s, y_s, z_s, color='orange', marker = '*', ms = 50)
# ax.plot(x_mer, y_mer, z_mer, color='green')
# ax.view_init(0, 90, 0)
# ax.set_xlabel("x", fontsize= 20)
# ax.set_ylabel("y", fontsize= 20)
# ax.set_zlabel("z", fontsize= 20)
# ax.axis('equal')
# plt.show()


# fig = plt.figure(figsize=(30,30))
# ax = fig.add_subplot(111, projection='3d')
# ax.plot(x_m, y_m, z_m, color='red')
# ax.plot(x_e, y_e, z_e, color='blue')
# ax.plot(x_s, y_s, z_s, color='orange', marker = '*', ms = 50)
# ax.plot(x_mer, y_mer, z_mer, color='green')
# ax.view_init(90, 0, 0)
# ax.set_xlabel("x", fontsize= 20)
# ax.set_ylabel("y", fontsize= 20)
# ax.set_zlabel("z", fontsize= 20)
# ax.axis('equal')
# plt.show()

fig = plt.figure(figsize=(30,30))
ax = fig.add_subplot(111, projection='3d')
ax.plot(x_1, y_1, z_1, color='red')
ax.plot(x_2, y_2, z_2, color='blue')
ax.plot(x_3, y_3, z_3, color='green')
ax.plot(x_4, y_4, z_4, color='purple')
ax.plot(x_5, y_5, z_5, color='black')
ax.plot(x_s, y_s, z_s, color='orange')
ax.view_init(0, 0, 0)
ax.set_xlabel("x", fontsize= 20)
ax.set_ylabel("y", fontsize= 20)
ax.set_zlabel("z", fontsize= 20)
# ax.axis('equal')
plt.savefig('p')

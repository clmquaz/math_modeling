class Ball:

    #создание статистических полей класса
    color = 'red'
    radius = 5

ball = Ball()

#вызов статистических полей класса

print(ball.color)
print(ball.radius)

#изменение статических полей экземпляра
ball.color = 'white'
print(ball.color)

#изменение статических полей класса
Ball.color = 'white'
new_ball = Ball()
print(Ball.color)
print(new_ball.color)
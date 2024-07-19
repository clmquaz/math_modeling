class Ball:
    def __init__ (self):
        '''инициализатор '''
        print('I was called')

ball = Ball()


class Ball:
    def __init__ (self, mass):
        self.mass = mass
        self.image = 'hexadone'

ball = Ball(0.5)
print(ball.image)
print(ball.mass)

ball.image = 'lines'
print(ball.image)
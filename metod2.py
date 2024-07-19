class Ball:
    def __init__ (self, mass):
        self.mass = mass
        self.image = 'hexadone'
        self.x = 0
        self.y = 0

    #методы, реализующие поведение экземпляра
    #self - подразумеваемый экземпляр
    def drop(self):
        print('I was dropped')
        self.x = 2
    def kick(self):
        print('I was kicked')
        self.x += 1
    def fail(self):
        self.mass = self.mass - 0.1

ball = Ball(0.5)
ball.drop()
ball.kick()
ball.fail()

print(ball.x)
print(ball.mass)


ball2 = Ball(1)
ball2.kick()
ball2.kick()
ball2.kick()
print(ball2.x)

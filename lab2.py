class Pyramid:
    def __init__(self, max_h):
        self.max_h = max_h
        self.bricks_count = 0
    def add_bricks(self, bricks):
        self.bricks_count += bricks
        r = 0
        for i in range(self.max_h, 0, -1):
            r+=i
        if self.bricks_count > r:
            self.bricks_count = 'error'
        else:
            pass
    def get_height(self):
        r = 0
        s = 0
        if self.bricks_count == 'error':
            print('error') 
        else:
            for i in range(self.max_h, 0, -1):
                r += i
                if self.bricks_count< r-i:
                    pass
                else:
                    s += 1
            print(s)
    def is_done(self):
        r = 0
        if self.bricks_count == 'error':
            print('error')
        else:
            for i in range(self.max_h, 0, -1):
                r+=i
            print(self.bricks_count/r)

s = Pyramid(5)
s.add_bricks(13)
s.get_height()
s.is_done()

class Builder:
    def __init__ (self, bricks):
        self.bricks = bricks
        self.my_pyramid = Pyramid(5)
    def buy_bricks(self, bricks):
        self.bricks += bricks
        if self.bricks <= 15:
            pass
        else:
            self.bricks -= bricks
            print('error')

    def build_pyramid(self, bricks):
        if bricks>=1 and bricks<=5:
            self.my_pyramid.add_bricks(bricks)
            self.bricks -= bricks
        else:
            print('error')
    def work_day():
        d = 1
        
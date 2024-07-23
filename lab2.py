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
            pass
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
            pass
        else:
            for i in range(self.max_h, 0, -1):
                r+=i
            print(f'{self.bricks_count/r*100}% is done')

#s = Pyramid(5)
#s.add_bricks(15)
#s.is_done()

class Builder:
    def __init__ (self, bricks):
        self.bricks = bricks
        self.my_pyramid = Pyramid(5)
        self.day = 0
    def buy_bricks(self, bricks):
        self.bricks += bricks
        if self.bricks <= 15 and bricks>= 0:
            pass
        else:
            self.bricks -= bricks
    def build_pyramid(self, bricks):
        if bricks>=1 and bricks<=5:
            self.my_pyramid.add_bricks(bricks)
            self.bricks -= bricks
        else:
            pass
    def work(self):
        d = 0
        r = 0
        n = 15-self.bricks
        self.buy_bricks(n)
        for i in range(self.my_pyramid.max_h, 0, -1):
            r+=i
        while r-self.my_pyramid.bricks_count>=5:
            self.build_pyramid(5)
            self.buy_bricks(5)
            d+=1
        c = r-self.my_pyramid.bricks_count
        if c>0:
            self.build_pyramid(c)
            d+=1
        else:
            pass
        print(f'day {d}')
    def work_day(self):
        r=0
        for i in range(self.my_pyramid.max_h, 0, -1):
            r+=i
        if self.my_pyramid.bricks_count <r:
            self.day +=1
            print(f'day {self.day}')
            n = 15-self.bricks
            self.buy_bricks(n)
            print(f'bought {n} bricks')
            if r-self.my_pyramid.bricks_count>=5:
                self.build_pyramid(5)
                print(f'add 5')
            else:
                self.build_pyramid(r-self.my_pyramid.bricks_count)
                print(f'add{r-self.my_pyramid.bricks_count}')
            print(self.my_pyramid.is_done())
            print(f'{self.bricks} bricks left', end = '\n\n')
        else:
            exit()
    

b = Builder(13)

while True:
    b.work_day()
class Planet:
    @staticmethod
    def is_big_planet(d):
        if d > 10000:
            return True
        else:
            return False
        
#print(Planet.is_big_planet(100))

class Sum:
    @staticmethod
    def sum_1(a, b):
        print(a+b)
    def sum_2(self, a, b):
        print(a+b)
    def sum_3(self, a, b):
        return Sum.sum_1(a, b)

Sum.sum_1(5, 10)

sum_num = Sum()
sum_num.sum_2(10, 15)
sum_num.sum_1(20, 25)
sum_num.sum_3(30, 35)

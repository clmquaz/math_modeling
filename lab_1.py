class Businessman:
    def_name = "Businessman"
    def_age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._money = 0
        self._business = [] 

    def info(self):
        print(self.name, self.age, self._money, self._business )

    @classmethod
    def def_info(cls):
        print(cls.def_name, cls.def_age)

    def _make_deal(self, obj):
        self._money-= obj._price
        self._business.append(obj)

    def earn_money(self, money):
        self._money += money

    def buy_business(self, obj, discount):
        obj.final_price(discount)
        if self._money >= obj._price:
            self._make_deal(obj)
        else:
            print("warning")


class Business:
    def __init__(self, area, price):
        self._area = area
        self._price = price 
    
    def final_price(self, discount):
        self._price = self._price - self._price*discount
        return self._price


class RestarauntBusiness(Business):
    def __init__(self, area):
        self._area = area
        self._price = 50*10**6


Businessman.def_info()
boss = Businessman('Vladimir', 10)
boss.info()
goal = RestarauntBusiness('dream')
boss.buy_business(goal, 0)
boss.earn_money(50*10**6)
boss.buy_business(goal, 0)
boss.info()
#print(boss._business[0]._price)
class Business:
    def __init__(self, area, price):
        self._area = area
        self._price = price 
    
    def final_price(self, discount):
        self._price = self._price - self._price*discount



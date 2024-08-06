class Puppy:
    states = ['sick', 'recover','health']
    def __init__(self, index):
        self.index = index 
        self.n = 0
        self.state = Puppy.states[self.n]

        
    def  get_treatment(self):
        if self.state != Puppy.states[2]:
            self.n+=1
            self.state = Puppy.states[self.n]
        else:
            pass


    def is_healthy(self):
        if self.state != Puppy.states[2]:
            pass
        else:
            print('health')
    
#s = Puppy(2)
#s.get_treatment()
#s.get_treatment()
#s.is_healthy()


class Dog:
    def __init__(self, n):
        self.puppies = [] 
        for i in range(0, n):
            x = Puppy(i)
            self.puppies.append(x)


    def heal_all(self):
        for i in range(0, len(self.puppies)):
            self.puppies[i].get_treatment()


    def all_are_healthy(self):
        a=0
        for i in range(0, len(self.puppies)):
            if self.puppies[i].state == 'health':
                a+=1
            else:
                pass
        if a == len(self.puppies):
            return True
        else:
            pass


    def  give_away_all(self):
        self.puppies.clear()
    
d = Dog(2)
#d.heal_all()


class Vet:
    def  __init__(self, name, dog):
        self.name = name 
        self.plant = dog


    def work_all(self):
        self.plant.heal_all()


    def work_one(self, n):
        self.plant.puppies[n-1].get_treatment()


    def care(self):
        if self.plant.all_are_healthy()==True:
            self.plant.give_away_all()
        else:
            print('warning')


    def knowledge_base(self):
        for i in range(0, len(self.plant.puppies)):
            print(self.plant.puppies[i].state)

if __name__ == '__main__':
    v = Vet('q', d)
    v.work_all()
    v.care()
    v.knowledge_base()
    v.work_one(2)
    v.knowledge_base()
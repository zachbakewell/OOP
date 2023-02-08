import random

class Insect:
    def __init__(self):
        self.legs = 4
        self.wings = 2
        self.len_flight = 0
        

    def len_flight(self):
        self.len_flight = random.randint(1,11)

    def type(self):
        if random.randint(0,1) == 0:
            self.type = 'Mosquito'
        else:
            self.type = 'House Fly'


    def get_len_flight(self):
        return self.len_flight

    
            

import random

class Human:
    def __init__(self, name="Human",
                 job = None, home=None, car = None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
class Auto:
    def __init__(self, brand_list):
        self.brand=random.choice( list(brand_list) )
        self.fuel = brand_list[self.brand]["fuel"]
        self.horsep = brand_list[self.brand]["horsep"]
        self.consumption = brand_list[self.brand]["consumption"]
brands_of_car = {
    "BMW":{"fuel": 100, "horsep": 140, "consumption": 6},
    "Ferrari":{"fuel": 100, "horsep": 170, "consumption": 10},
    "Porshe":{"fuel": 100, "horsep": 160, "consumption": 12},
    "Volkswagen":{"fuel": 100, "horsep": 60, "consumption": 7},
    "Lada":{"fuel": 100, "horsep": 40, "consumption": 10}
}



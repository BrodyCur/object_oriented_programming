class Cat:
    """ This is a class defining a cat """ 

    def __init__(self, name, preferred_food, meal_time):
        self.name = name
        self.preferred_food = preferred_food
        self.meal_time = meal_time

    def __str__(self):
        return f"{self.name} eats their {self.preferred_food} at {self.meal_time}"

    def eats_at(self):
        if self.meal_time == 24:
            self.meal_time -= 12
            return f"{self.meal_time} AM"
        elif self.meal_time > 24 or self.meal_time == 0:
            return "Invalid Number"
        elif self.meal_time >= 12:
            self.meal_time -= 12
            return f"{self.meal_time} PM"
        elif self.meal_time < 12:
            return f"{self.meal_time} AM"
        else:
            pass


    def meow(self):
        return f"My name is {self.name} and I eat {self.preferred_food} at {self.eats_at()}"
            

cat1 = Cat('Tibby', 'Chicken Pate', 24)
cat2 = Cat('Frank', 'Dog Kibble', 13)

print(cat1.meow())
print(cat2.meow())

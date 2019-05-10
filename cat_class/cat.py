class Cat:
    """ This is a class defining a cat """ 

    def __init__(self, name, preferred_food, meal_time):
        self.name = name
        self.preferred_food = preferred_food
        self.meal_time = meal_time

    def __str__(self):
        return f"{self.name} eats their {self.preferred_food} at {self.meal_time}"


tibby = Cat('Tibby', 'Chicken Pate', 9)
frank = Cat('Frank', 'Dog Kibble', 20)

print(tibby)
print(frank)
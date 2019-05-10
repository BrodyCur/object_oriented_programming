class Player:
    """ This is a class defining a player character in a game """

    def __init__(self):
        self.gold_coins = 0
        self.health_points = 10
        self.lives = 5

    def __str__(self):
        return f"Stats\nHealth: {self.health_points}\nLives: {self.lives}\nGold: {self.gold_coins}"

    def level_up(self):
        self.lives += 1
    
    def collect_treasure(self):
        self.gold_coins += 1
        if self.gold_coins % 10 == 0:
            self.level_up()
    
    def do_battle(self, damage):
        self.health_points -= damage
        if self.health_points < 1:
            self.lives -=1
            self.health_points = 10
        if self.lives == 0:
            self.restart()
    
    def restart(self):
        self.gold_coins = 0
        self.health_points = 10
        self.lives = 5
        

hero = Player()

hero.level_up()
hero.collect_treasure()
hero.collect_treasure()
hero.collect_treasure()
hero.collect_treasure()
hero.collect_treasure()
hero.collect_treasure()
hero.collect_treasure()
hero.collect_treasure()
hero.collect_treasure()
hero.collect_treasure()

hero.do_battle(10)
hero.do_battle(10)
hero.do_battle(10)
hero.do_battle(10)
hero.do_battle(10)
hero.do_battle(10)
hero.do_battle(10)

print(hero)
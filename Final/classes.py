class room:
    def __init__(self, enemy, loot):
        self.enemy = enemy
        self.loot = loot
class enemy:
    def __init__(self, health, type, item, name, attack, armor = 0, level = 1,):
        self.health = health
        self.type = type
        self.item = item
        self.level = level
        self.name = name
        self.attack = attack
        self.armor = armor
    def yell(self):
        self.armor = self.armor + 1
        return (self.armor)
class player:
    def __init__(self, health, type, item, name, attack, inv, armor = 0, level = 1):
        self.health = health
        self.type = type
        self.item = item
        self.level = level
        self.name = name
        self.attack = attack
        self.armor = armor
        self.inv = inv
if __name__ == "__main__":
    placeholder = enemy(50,"type","item","placeholder")
    print(placeholder.health)
    print(placeholder.type)
    print(placeholder.item)
    print(placeholder.level)
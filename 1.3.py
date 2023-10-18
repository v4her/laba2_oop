class Weapon:
    ammo = None
    damage = None
    durability = None
    distance = None

    def attack(self):
        pass
    def reload(self):
        pass
    def repair(self):
        pass
    pass

ak47 = Weapon()
ak47.ammo = 30
ak47.damage = 35
ak47.durability = 100
ak47.distance = 1000

def info(self):
    print('ammo =', self.ammo)
    print('damage =', self.damage)
    print( 'durability =', self.durability)
    print('distance =', self.distance)

info(ak47)
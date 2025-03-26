from Novice import Novice

class Swordsman(Novice):
    def __init__(self, username):
        super().__init__(username)
        self.setStr(5)
        self.setVit(10)
        self.setHp(self.getHp() + self.getVit())

    def slashAttack(self, character):
        new_damage = self.getDamage() + self.getStr()
        character.reduceHp(new_damage)
        print(f"{self.getUsername()} performed Slash Attack! - {new_damage} damage")

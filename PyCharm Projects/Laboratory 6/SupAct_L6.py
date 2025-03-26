import random

class Character:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.wins = 0

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def is_alive(self):
        return self.hp > 0

class Player(Character):
    def __init__(self, name, role="Novice"):
        roles = {
            "Novice": (100, 10),
            "Swordsman": (120, 15),
            "Archer": (100, 20),
            "Magician": (90, 25)
        }
        hp, attack = roles[role]
        super().__init__(name, hp, attack)
        self.role = role

class Monster(Character):
    def __init__(self):
        super().__init__("Monster", 100, 12)

class Game:
    def __init__(self):
        self.players = []

    def select_mode(self):
        print("Select mode:")
        print("1. Single Player")
        print("2. Player vs Player")
        choice = input("Enter choice (1 or 2): ")
        if choice == "1":
            self.single_player_mode()
        elif choice == "2":
            self.pvp_mode()
        else:
            print("Invalid choice. Try again.")
            self.select_mode()

    def single_player_mode(self):
        name = input("Enter your name: ")
        player = Player(name)
        self.players.append(player)
        self.play_match(player, Monster())
        if player.wins >= 2:
            print("Congratulations! You can now choose a new role.")
            self.change_role(player)

    def pvp_mode(self):
        name1 = input("Enter Player 1 name: ")
        role1 = input("Choose role (Novice, Swordsman, Archer, Magician): ")
        player1 = Player(name1, role1)

        name2 = input("Enter Player 2 name: ")
        role2 = input("Choose role (Novice, Swordsman, Archer, Magician): ")
        player2 = Player(name2, role2)

        self.players.extend([player1, player2])
        self.play_match(player1, player2)

    def change_role(self, player):
        role = input("Choose new role (Swordsman, Archer, Magician): ")
        if role in ["Swordsman", "Archer", "Magician"]:
            player.__init__(player.name, role)
        else:
            print("Invalid role. Keeping current role.")

    def play_match(self, player1, player2):
        print(f"Match Start: {player1.name} vs {player2.name}")
        players = [player1, player2]
        random.shuffle(players)

        while player1.is_alive() and player2.is_alive():
            attacker, defender = players[0], players[1]
            damage = attacker.attack
            print(f"{attacker.name} attacks {defender.name} for {damage} damage!")
            defender.take_damage(damage)
            print(f"{defender.name} HP: {defender.hp}\n")
            if not defender.is_alive():
                print(f"{attacker.name} wins!")
                attacker.wins += 1
                break
            players.reverse()

if __name__ == "__main__":
    game = Game()
    game.select_mode()

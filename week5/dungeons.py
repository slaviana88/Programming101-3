import random
from WeaponAndSpell import Weapon, Spell
from HeroAndEnemy import Hero, Enemy


class Dungeon:

    def __init__(self, filename):
        lines = open(filename).read().split("\n")
        lines = [line for line in lines if line.strip() != 0]
        self.dungeon = [[ch for ch in line] for line in lines]
        self.map = None
        self.hero = Hero("Bron", "Dragonslayer", 100, 100, 2)

    def print_map(self):
        for x in self.dungeon:
            ss = ''.join(x)
            print(ss)

    def spawn(self):

        found = False
        for i in range(0, len(self.dungeon)):
            for j in range(0, len(self.dungeon[i])):
                if self.dungeon[i][j] == 'S':
                    self.dungeon[i][j] = 'H'
                    found = True
                    break
                    if found:
                        break
            return found

    def get_position(self):
        for i in range(len(self.dungeon)):
            for j in range(len(self.dungeon[i])):
                if self.dungeon[i][j] == "H":
                    return (i, j)

    def pick_treasure(self):
        treasures = ["heal_potion", "mana_potion", "weapon", "spell"]
        loot = random.choice(treasures)
        if loot == "heal_potion":
            heal = random.choice(self.treasure[loot])
            self.hero.take_healing(heal)
            print("Found health potion. Hero health is {}.".format(
                self.hero.get_health()))
        elif loot == "mana_potion":
            mana = random.choice(self.treasure[loot])
            self.hero.take_mana(mana)
            print("Found mana potion. Hero mana is {}.".format(
                self.hero.get_mana()))
        elif loot == "weapon":
            weapon = random.choice(self.treasure[loot])
            self.hero.equip(weapon)
            print("Found a weapon - {}.".format(weapon.name))
        elif loot == "spell":
            spell = random.choice(self.treasure[loot])
            self.hero.learn(spell)
            print("Learned a new spell: {}.".format(spell.name))

    def next_position(self, i, j):
        if self.dungeon[i][j] == "#":
            return False
        elif self.dungeon[i][j] == ".":
            self.dungeon[i][j] = "H"
            return True
        elif self.dungeon[i][j] == "G":
            print("Game over!")
            return True
        elif self.dungeon[i][j] == "E":

            return True
        elif map[i][j] == "T":
            self.pick_treasure()
            self.dungeon[i][j] = "H"
            return True

    def check_out_of_range(self, i, j):
        if i < 0 or i > len(self.dungeon) - 1:
            return False
        if j < 0 or j > len(self.dungeon[j]):
            return False
        return True

    def move_hero(self, direction):
        position = self.get_position()
        i = position[0]
        j = position[1]
        if direction == "right":
            if self.check_out_of_range(i, j+1):
                if not self.next_position(i, j+1):
                    return False
                self.dungeon[i][j] = "."
            else:
                return False
        if direction == "left":
            if self.check_out_of_range(i, j-1):
                if not self.next_position(i, j-1):
                    return False
                self.dungeon[i][j] = "."
            else:
                return False
        if direction == "up":
            if self.check_out_of_range(i-1, j):
                if not self.next_position(i-1, j):
                    return False
                self.dungeon[i][j] = "."
            else:
                return False
        if direction == "down":
            if self.check_out_of_range(i+1, j):
                if not self.next_position(i+1, j):
                    return False
                self.dungeon[i][j] = "."
            else:
                return False
        self.hero.take_mana(self.hero.mana_regeneration_rate)
        return True

    def hero_attack(self, by=""):
        


class Fight:

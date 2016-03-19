from HeroAndEnemy import Enemy
from WeaponAndSpell import Spell, Weapon
import random


class Dungeon:
    OBSTACLE = "#"
    SPAWNING_POINT = "S"
    ENEMY = "E"
    EXIT = "G"
    TREASURE = "T"
    WALKABLE_PATH = "."
    HERO = "H"
    DIRECTIONS = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1)
    }

    @staticmethod
    def create_from_file(path):
        dungeon = []
        with open(path, "r") as f:
            contents = f.read().split("\n")
            dungeon = [list(line) for line in contents if line.strip() != ""]

        return Dungeon(dungeon)

    @staticmethod
    def create_from_string(string):
        dungeon = [list(line) for line in string.split()]

        return Dungeon(dungeon)

    def __init__(self, dungeon_matrix):
        self.__map = dungeon_matrix
        self.__spawning_points = self.__find_spawning_points()
        self.__hero = None
        self.__hero_position = None
        self.__enemy = None
        self.__enemy_position = None
        self.treasure = {
                   "heal_potion": [25, 50, 75, 100],
                   "mana_potion": [25, 50, 75, 100],
                   "weapon": [Weapon("Axe", damage=20),
                              Weapon("Sword", damage=25),
                              Weapon("Mace", damage=30)],
                   "spell": [Spell("Frostbolt", 20, 30, cast_range=3),
                             Spell("Fireball", 25, 40, cast_range=2),
                             Spell("Arcanebolt", 30, 50, cast_range=2)],
                   }

    def get_spawning_points(self):
        return self.__spawning_points

    def __find_spawning_points(self):
        spawning_points = []

        for row_index in range(0, len(self.__map)):
            for tile_index in range(0, len(self.__map[row_index])):
                tile = self.__map[row_index][tile_index]

                if tile == Dungeon.SPAWNING_POINT:
                    spawning_points.append((row_index, tile_index))

        return spawning_points

    def print_map(self):
        res = ""
        for line in self.__map:

            for ch in line:
                res += ch

            if ch == "G":
                return res

            else:
                res += '\n'


    def __place_on_map(self, point, entity):
        self.__map[point[0]][point[1]] = entity

    def spawn(self, hero):
        if len(self.__spawning_points) == 0:
            raise Exception("Cannot spawn hero.")

        self.__hero = hero
        self.__hero_position = self.__spawning_points.pop(0)

        self.__place_on_map(self.__hero_position, Dungeon.HERO)

    def __can_make_move(self, point):
        x, y = point
        if x < 0 or x >= len(self.__map):
            return False

        if y < 0 or y >= len(self.__map[0]):
            return False

        if self.__map[x][y] == Dungeon.OBSTACLE:
            return False

        return True

    def __str__(self):
        return "\n".join(["".join(line) for line in self.__map])

    def __trigger_action_on_move(self, position):
        x, y = position
        entity = self.__map[x][y]
        if entity == Dungeon.TREASURE:
            return False

        if entity == Dungeon.ENEMY:
            return True

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

    def move(self, direction):
        if direction not in Dungeon.DIRECTIONS:
            raise Exception("{} is not a valid direction".format(direction))

        dx, dy = Dungeon.DIRECTIONS[direction]
        hero_x, hero_y = self.__hero_position

        new_position = (hero_x + dx, hero_y + dy)

        if self.__can_make_move(new_position):

            self.__place_on_map((hero_x, hero_y), Dungeon.WALKABLE_PATH)
            is_dead = self.__trigger_action_on_move(new_position)

            if is_dead:
                self.spawn(self.__hero)
                return

            self.__hero_position = new_position
            self.__place_on_map(new_position, Dungeon.HERO)

    def search_enemy_in_range_attack(self, cast_range):
        hero_x, hero_y = self.__hero_position

        for direction in Dungeon.DIRECTIONS:
            dx, dy = Dungeon.DIRECTIONS[direction]

            for r in range(1, cast_range+1):
                dx, dy = dx*r, dy*r

                point = (hero_x+dx, hero_y+dy)
                if self.__can_make_move(point):
                    entity = self.__map[hero_x + dx][hero_y + dy]

                    if entity == Dungeon.ENEMY:
                        self.__enemy = Enemy(health=100, mana=100, damage=20)
                        self.__enemy_position = entity
                        return True

        return False

    def __create_message_nothing_cast(self, cast_range):
        return "Nothing in casting range {}".format(cast_range)

    def __create_message_start_fight(self):
        return "A fight is started between our {} and {}".format(self.__hero, self.__enemy)

    def hero_attack(self, by=""):
        if by == "spell" and self.__hero.has_spell():
            cast_range = self.__hero.spell.get_cast_range()
            if self.search_enemy_in_range_attack(cast_range):
                print(self.__create_message_start_fight())
            else:
                print(self.__create_message_nothing_cast(cast_range))
        else:
            pass

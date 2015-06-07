import unittest
from dungeons import Hero
from dungeons import Dungeon


class DungeonsAndPythonsTests(unittest.TestCase):
    def setUp(self):
        self.hero = Hero("Bron", "Dragon", 100, 100, 2)
        self.dungeon = Dungeon("map2.txt")
        self.weapon = Weapon(name="The Axe of Destiny", damage=20)
        self.spell = Spell(name="Fireball", damage=30, mana_cost=50, cast_range=2)
        self.mana_potion = self.hero.mana
        self.health_potion = self.hero.health

    def test_known_as(self):
        self.assertEqual(self.hero.known_as(), "Bron the Dragon")

    def test_is_alive(self):
        self.assertTrue(self.hero.is_alive())

    def test_spawn_hero(self):
        self.dungeon.spawn()

    def test_get_position(self):
        self.dungeon.spawn()
        self.assertEqual(self.dungeon.get_position(), (0, 0))

    def test_move_right(self):
        self.dungeon.spawn()
        self.dungeon.move_hero("right")
        # self.dungeon.print_map()
        self.assertFalse(self.dungeon.move_hero("right"))

    def test_move_up(self):
        self.dungeon.spawn()
        self.dungeon.move_hero("up")
        self.assertFalse(self.dungeon.move_hero("up"))

    def test_move_left(self):
        self.dungeon.spawn()
        self.dungeon.move_hero("left")
        self.assertFalse(self.dungeon.move_hero("left"))

    def test_move_down(self):
        self.dungeon.spawn()
        self.dungeon.move_hero("down")
        self.assertFalse(self.dungeon.move_hero("down"))


if __name__ == '__main__':
    unittest.main()

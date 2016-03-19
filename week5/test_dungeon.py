import unittest
from HeroAndEnemy import Hero
from WeaponAndSpell import Spell, Weapon
from dungeon import Dungeon


class TestDungeon(unittest.TestCase):
    def setUp(self):
        map_dungeon = """S.##.....T
#T##..###.
#.###E###E
#.E...###.
###T#####G"""
        self.dungeon = Dungeon.create_from_string(map_dungeon)
        self.hero = Hero("Bron", "Dragon", 100, 100, 2)

    def test_get_spawning_points(self):
        self.assertEqual(self.dungeon.get_spawning_points(), [(0, 0)])

    def test_spawn(self):
        self.dungeon.spawn(self.hero)
        expected = """H.##.....T
#T##..###.
#.###E###E
#.E...###.
###T#####G"""
        self.assertEqual(self.dungeon.print_map(), expected)

    def test_move_out_of_map(self):
        self.dungeon.spawn(self.hero)
        self.assertFalse(self.dungeon.move("up"))

    def test_move_on_walkable_path(self):
        self.dungeon.spawn(self.hero)
        self.dungeon.move("right")
        expected = """.H##.....T
#T##..###.
#.###E###E
#.E...###.
###T#####G"""
        self.assertEqual(self.dungeon.print_map(), expected)

    def test_move_on_treasure(self):
        self.dungeon.spawn(self.hero)
        self.dungeon.move("right")
        self.assertFalse(self.dungeon.move("down"))

    def test_move_on_obstacle(self):
        self.dungeon.spawn(self.hero)
        self.dungeon.move("right")
        self.assertFalse(self.dungeon.move("right"))

    def test_move_on_enemy(self):
        map2 = """S.##.....T
#E##..###.
#.###E###E
#.E...###.
###T#####G"""
        dungeon2 = Dungeon.create_from_string(map2)
        dungeon2.spawn(self.hero)
        dungeon2.move("right")

        with self.assertRaises(Exception):
            dungeon2.move("down")

    def test_search_enemy_in_range_attack(self):
        self.dungeon.spawn(self.hero)
        self.dungeon.move("right")
        self.dungeon.move("down")
        self.dungeon.move("down")
        self.dungeon.move("down")

        self.assertTrue(self.dungeon.search_enemy_in_range_attack(2))

    def test_search_when_enemy_not_in_range_attack(self):
        self.dungeon.spawn(self.hero)
        self.assertFalse(self.dungeon.search_enemy_in_range_attack(2))

if __name__ == '__main__':
    unittest.main()

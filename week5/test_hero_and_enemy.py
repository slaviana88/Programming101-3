import unittest
from HeroAndEnemy import Hero
from WeaponAndSpell import Spell, Weapon


class TestHero(unittest.TestCase):
    def setUp(self):
        self.hero = Hero(name="Bron", title="DragonSlayer", health=100,
                         mana=100, mana_regeneration_rate=2)
        self.spell = Spell(name="Fireball", damage=30, mana_cost=50,
                           cast_range=2)
        self.weapon = Weapon(name="The Axe of Destiny", damage=20)

    def test_known_as(self):
        self.assertEqual(self.hero.known_as(), "Bron the DragonSlayer")

    def test_is_alive(self):
        self.assertTrue(self.hero.is_alive())

    def test_can_cast(self):
        self.hero.learn(self.spell)
        self.assertTrue(self.hero.can_cast())

    def test_learn_spell(self):
        self.hero.learn(self.spell)
        self.assertTrue(self.hero.has_spell())

    def test_equip_weapon(self):
        self.hero.equip(self.weapon)
        self.assertTrue(self.hero.has_weapon())

    def test_take_damage_when_hero_has_enough_health(self):
        self.hero.take_damage(50)
        self.assertEqual(self.hero.get_health(), 50)

    def test_take_damage_when_hero_has_not_enough_health(self):
        self.hero.take_damage(200)
        self.assertEqual(self.hero.get_health(), 0)

    def test_take_mana_when_hero_has_max_mana(self):
        self.hero.take_mana(50)
        self.assertEqual(self.hero.get_mana(), 100)

    def test_take_mana(self):
        self.hero.learn(self.spell)
        self.hero.attack(by="magic")
        self.hero.take_mana(30)

        self.assertEqual(self.hero.get_mana(), 80)

    def test_is_alive_when_hero_is_dead(self):
        hero2 = Hero(name="Bron", title="DragonSlayer", health=0,
                     mana=100, mana_regeneration_rate=2)

        self.assertFalse(hero2.is_alive())

    def test_take_healing_when_hero_is_dead(self):
        hero2 = Hero(name="Bron", title="DragonSlayer", health=0,
                     mana=100, mana_regeneration_rate=2)

        self.assertFalse(hero2.take_healing(2))

    def test_take_healing(self):
        self.hero.learn(self.spell)
        self.hero.attack(by="magic")

        self.assertTrue(self.hero.take_healing(40))

    def test_attack_weapon(self):
        self.hero.equip(self.weapon)

        self.assertEqual(self.hero.attack(by="weapon"), 20)

    def test_attack_spell(self):
        self.hero.learn(self.spell)

        self.assertEqual(self.hero.attack(by="magic"), 30)

    def test_attack_without_weapon(self):
        self.assertEqual(self.hero.attack(by="weapon"), 0)

if __name__ == '__main__':
    unittest.main()

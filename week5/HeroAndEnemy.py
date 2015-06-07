from WeaponAndSpell import Weapon, Spell


class Hero:
    def __init__(self, name, title, health, mana, mana_regeneration_rate):
        self.name = name
        self.title = title
        self.health = health
        self.mana = mana
        self.__max_health = health
        self.__max_mana = mana
        self.mana_regeneration_rate = mana_regeneration_rate
        self.weapon = None
        self.spell = None

    def __str__(self):
        return "Hero(hp:{})".format(self.health)

    def __hash__(self):
        return hash(self.__str__())

    def __repr__(self):
        return self.__str__()

    def known_as(self):
        return "{} the {}".format(self.name, self.title)

    def is_alive(self):
        return self.health > 0

    def get_health(self):
        return self.health

    def get_mana(self):
        return self.mana

    def can_cast(self):
        if self.mana == 0:
            return False
        if self.spell is not None:
            if self.mana >= self.spell.get_mana_cost():
                return True
        return False

    def equip(self, weapon):
        self.weapon = weapon

    def learn(self, spell):
        self.spell = spell

    def take_mana(self, mana):
        if self.mana + mana > self.__max_mana:
            self.mana = self.__max_mana
        else:
            self.mana += mana

    def take_damage(self, damage):
        if self.health - damage < 0:
            self.health = 0
        else:
            self.health -= damage

    def take_healing(self, health):
        if not self.is_alive():
            return False
        if self.health + health > self.__max_health:
            self.health = self.__max_health
        else:
            self.health += health

    def attack(self, by=""):
        if by == "weapon":
            if self.weapon is not None:
                return self.weapon.get_damage()
        elif by == "magic":
            if self.spell is not None:
                if self.can_cast():
                    self.mana -= self.spell.get_mana_cost()
                    return self.spell.get_damage()
                raise Exception("Not enough mana.")
        return self.damage


class Enemy:
    def __init__(self, health, mana, damage):
        self.health = health
        self.__man_health = health
        self.mana = mana
        self.__max_mana = mana
        self.damage = damage

    def __str__(self):
        return "Enemy({}health - {} mana)".format(self.__health, self.__mana)

    def __hash__(self):
        return hash(self.__str__())

    def __repr__(self):
        return self.__str__()

    def is_alive(self):
        return self.health > 0

    def get_health(self):
        return self.health

    def get_mana(self):
        return self.mana

    def can_cast(self):
        if self.mana == 0:
            return False
        if self.damage is not None:
            if self.mana >= self.spell.get_mana_cost():
                return True
        return False

    def take_mana(self, mana):
        if self.mana + mana > self.__max_mana:
            self.mana = self.__max_mana
        else:
            self.mana += mana

    def take_damage(self, damage):
        if self.health - damage < 0:
            self.health = 0
        else:
            self.health -= damage

    def take_healing(self, health):
        if not self.is_alive():
            return False
        if self.health + health > self.__max_health:
            self.health = self.__max_health
        else:
            self.health += health

    def attack(self, by=""):
        if by == "weapon":
            if self.weapon is not None:
                return self.weapon.get_damage()
        elif by == "magic":
            if self.spell is not None:
                if self.can_cast():
                    self.mana -= self.spell.get_mana_cost()
                    return self.spell.get_damage()
                raise Exception("Not enough mana.")
        return self.damage

    def attack(self):
        if not self.damage:
            raise Exception("Not enough damage")
        if self.damage > 0:

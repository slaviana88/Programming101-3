class Weapon:
    def __init__(self, name, damage):
        if not isinstance(name, str):
            raise TypeError("Name must be string")

        if not isinstance(damage, int):
            raise TypeError("Damage must be integer")

        self.name = name
        self.__damage = damage

    def __repr__(self):
        return "{} - {} damage".format(self.name, self.__damage)

    def get_damage(self):
        return self.__damage


class Spell:
    def __init__(self, name, damage, mana_cost, cast_range):
        if not isinstance(name, str):
            raise TypeError("Name must be string")

        if not isinstance(damage, int):
            raise TypeError("Damage must be integer")

        if not isinstance(mana_cost, int):
            raise TypeError("mana_cost must be integer")

        if not isinstance(cast_range, int):
            raise TypeError("Cast_range must be integer")

        self.name = name
        self.__damage = damage
        self.__mana_cost = mana_cost
        self.__cast_range = cast_range

    def __repr__(self):
        return "{} - {} damage {} mana_cost".format(self.name, self.__damage, self.__mana_cost)

    def get_damage(self):
        return self.__damage

    def get_mana_cost(self):
        return self.__mana_cost

    def get_cast_range(self):
        return self.__cast_range

class Panda2():

    def __init__(self, name, email, gender):

        if not isinstance(name, str):
            raise TypeError
        if not (gender == "male" or gender == "female"):
            raise TypeError("Nekorektni danni")
#        if not is_valid

        self.__name = name
        self.__email = email
        self.__gender = gender

    def name(self):
        return self.__name

    def email(self):
        return self.__email

    def gender(self):
        return self.__gender

    def isMale(self):
        return self.__gender == "male"

    def isFemale(self):
        return self.__gender == "female"

    def __str__(self):
        return "Panda: {} {} {}".format(self.__name, self.__email, self.__gender)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return str(self) == str(other)

    def __hash__(self):
        return hash(self.__str__())

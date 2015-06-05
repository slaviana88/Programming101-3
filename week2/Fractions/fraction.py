class Fraction:

    def __init__(self, num, den):
        self.num = num
        self.den = den

    def __str__(self):
        return "{} / {}".format(self.num, self.den)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.num/self.den == other.num/other.den

    def reduce(self, num, den):
        for i in range(num, 0, -1):
            if den % i == 0 and num % i == 0:
                num /= i
                den /= i
        return int(num), int(den)

    def __add__(self, other):
        below = self.den * other.den
        above = self.num * (below / self.den) + other.num * (below / other.den)
        above = int(above)
        return Fraction(self.reduce(above, below)[0],
                        self.reduce(above, below)[1])

    def __sub__(self, other):
        below = self.den * other.den
        above = self.num * (below / self.den) - other.num * (below / other.den)
        above = int(above)
        if above == 0:
            return 0
        return Fraction(self.reduce(above, below)[0],
                        self.reduce(above, below)[1])

    def __mul__(self, other):
        above = self.num * other.num
        below = self.den * other.den
        return Fraction(self.reduce(above, below)[0],
                        self.reduce(above, below)[1])

    def __truediv__(self, other):
        above = self.num * other.den
        below = self.den * other.num
        return Fraction(self.reduce(above, below)[0],
                        self.reduce(above, below)[1])


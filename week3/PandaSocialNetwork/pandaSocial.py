import json
from Panda import Panda2

class PandaSocialNetwork():
    def __init__(self):
        self.network = {}

    def pandas(self):
        return self.__pandas

    def has_panda(self, panda):
        return panda in self.network

    def are_friends(self, panda1, panda2):
        return panda1 in self.network[panda2] and panda2 in self.network[panda1]

    def add_panda(self, panda):
        if self.has_panda(panda):
            raise Exception('Panda already there')
        self.network[panda] = []

    def make_friend(self, panda1, panda2):
        if not self.has_panda(panda1):
            self.add_panda(panda1)

        if not self.has_panda(panda2):
            self.add_panda(panda2)

        if self.are_friends(panda1, panda2):
            raise Exception("Panda are already friends")

        self.network[panda1].append(panda2)
        self.network[panda2].append(panda1)

    def friends_of(self, panda):
        if panda not in self.network:
            raise Exception('pandata ne e tam')
        return self.network[panda]

    def connection_level(self, panda1, panda2):
        if self.friends_of(panda2) == []:
            return False
        if (panda1 or panda2) not in self.network:
            return False

        if self.are_friends(panda1, panda2):
            return 1

        queue = []
        path = [panda1]
        queue.append(path)
        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node == panda2:
                return len(path)-1
            for adjacent in self.network[node]:
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)
        return -1

    def panda_connections(self, panda):
        connections = {}
        q = []
        visited = set()

        q.append((0, panda))
        visited.add(panda)

        while len(q) != 0:
            panda_data = q.pop(0)
            current_level = panda_data[0]
            current_node = panda_data[1]

            connections[current_node] = current_level

            for neighboor in self.network[current_node]:
                if neighboor not in visited:
                    visited.add(neighboor)
                    q.append((current_level+1, neighboor))

        return connections

    def connection_level2(self, panda1, panda2):
        panda_table = self.panda_connections(panda1)

        if panda2 not in panda_table:
            return -1

        return panda_table[panda2]

    def genders_in_network(self, level, gender, panda):
        panda_table = self.panda_connections(panda)
        counter = 0

        for panda in panda_table:
            p_level = panda_table[panda]
            if p_level != 0 and p_level <= level and panda.gender() == gender:
                counter += 1
        return counter

    def __repr__(self):
        for_save = {}

        for panda in self.network:
            friends = [repr(panda_friend) for panda_friend in self.network[panda]]
            for_save[repr(panda)] = friends

        return for_save

    def save(self, filename):
        with open(filename, "w") as f:
            f.write(json.dumps(self.__repr__(), indent=True))

    def load(filename):
        with open(filename, "r") as f:
            contents = f.read()
            json_network = json.loads(contents)

            network = PandaSocialNetwork()

            for panda in json_network:
                for friends in json_network[panda]:

                    p1 = eval(panda)
                    p2 = eval(friends)
                    if not network.are_friends(p1, p1):
                        network.make_friend(p1, p2)
            return network

    def are_connected(self, panda1, panda2):
        if self.connection_level(panda1, panda2) > 0:
            return True
        return False

    def how_many_gender_in_network(level, panda, gender):
        pass


network = PandaSocialNetwork()
ivo = Panda2("Ivo", "ivo@pandamail.com", "male")
rado = Panda2("Rado", "rado@pandamail.com", "male")
tony = Panda2("Tony", "tony@pandamail.com", "female")
buby = Panda2("bobi", "bobi@mail.bg", "female")

for panda in [ivo, rado, tony,buby]:
    network.add_panda(panda)
print(network.__dict__)

network.make_friend(ivo, rado)
network.make_friend(rado, tony)

#print(network.connection_level(ivo, tony) == 2)
print(network.connection_level(ivo,buby))

#print(network.are_connected(ivo, rado))
print(network.are_connected(ivo, buby))

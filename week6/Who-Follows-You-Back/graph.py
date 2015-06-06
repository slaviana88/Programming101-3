import requests


class DirectedGraph:
    def __init__(self):
        self.info = {}

    def get_info(self):
        return self.info

    def has_node(self, node):
        return node in self.info

    def add_node(self, node):
        if self.has_node(node):
            raise Exception('Node already there')
        self.info[node] = []

    def add_edge(self, node1, node2):
        if not self.has_node(node1):
            self.add_node(node1)

        if not self.has_node(node2):
            self.add_node(node2)

        self.info[node1].append(node2)

    def get_neighbors_for(self, node):
        return self.info[node]

    def path_between(self, node1, node2):
        queue = []
        queue.append([node1])
        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node == node2:
                return True
            for adjacent in self.info[node]:
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)
        return False


class GithubSocialNetwork:

    IDS = "?client_id=31c51d6d3dafb7e24219&client_secret=b2aff3ccf1310933baa08f1882bfc3fed46afcca"
    ADDRESS = "https://api.github.com/users/"

    def __init__(self, username, level):
        if level > 3:
            return ValueError
        self.username = username
        self.level = level
        self.graph = DirectedGraph()

    def get_info2(self, user):
        info = {
               "followers": [user["login"] for user in requests.get(
                self.ADDRESS + user + "/followers" + self.IDS).json()],
               "following": [user["login"] for user in requests.get(
                self.ADDRESS + user + "/following" + self.IDS).json()],
               }
        return info

    def build_network(self, start, level):
        q = []
        visited = set()
        visited.add(start)
        q.append((0, start))
        while len(q) != 0:
            current_level = q.pop(0)
            current_node = q.pop(0)
            if current_level + 1 > level:
                break
            for follower in self.get_info()["followers"]:
                self.graph.add_edge(follower, current_node)
                q.append((current_level + 1, follower))
            for following in self.get_info()["following"]:
                self.graph.add_edge(following, current_node)
                q.append((current_level + 1, following))

    def do_you_follow(self, user):
        return user in self.get_info2(self.username)["following"]

    def do_you_follow_indirectly(self, user):
        for followed in self.get_info2(self.username)["following"]:
            if user in self.get_info2(followed)["following"]:
                return True
        return False

    def does_he_she_follow_user(self, user):
        return user in self.get_info()["followers"]

    def does_he_she_follows_indirectly(self, user):
        for follow in self.get_info()["followers"]:
            return user in self.get_info()[follow]

    def who_follows_you_back(self):
        followers = [follower for follower in self.get_info2(self.username)["followers"]]
        following = [follow for follow in self.get_info2(self.username)["following"]]
        result1 = [user for user in followers if user in following]
        result2 = [user for user in followers for followed in following if user in self.get_info2(followed)["following"]]
        return list(set(result1 + result2))

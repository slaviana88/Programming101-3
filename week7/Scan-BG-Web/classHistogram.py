class Histogram:

    def __init__(self):
        self.servers = {}

    def add(self, server):
        if server not in self.servers:
            self.servers[server] = 0
        if server in self.servers.keys:
            self.servers[server] += 1
        return self.servers

    def count(self, server):
        if server not in self.servers:
            return None
        return self.servers[server]

    def get_dict(self):
        return self.servers

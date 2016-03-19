import unittest
from graph import DirectedGraph, GithubSocialNetwork


class GraphTests(unittest.TestCase):
    def setUp(self):
        self.graph = DirectedGraph()

    def test_add_node(self):
        self.graph.add_node("Rado")
        self.assertTrue(self.graph.has_node("Rado"))

    def test_add_edge(self):
        self.graph.add_edge("Rado", "Ivo")
        self.assertEqual(self.graph.info, {"Rado": ["Ivo"], "Ivo": []})

    def test_get_neighbors_for(self):
        self.graph.add_edge("Rado", "Gosho")
        self.assertEqual(self.graph.get_neighbors_for("Rado"), ["Gosho"])

    def test_path_between(self):
        self.graph.add_edge("Rado", "Gosho")
        self.graph.add_edge("Rado", "Ani")
        self.graph.add_edge("Gosho", "Ivo")
        self.assertTrue(self.graph.path_between("Rado", "Ani"))
        self.assertFalse(self.graph.path_between("Ani", "Ivo"))
        self.assertTrue(self.graph.path_between("Rado", "Ivo"))


class NetworkTests(unittest.TestCase):
    def setUp(self):
        self.network = GithubSocialNetwork("slaviana88", 2)
        self.username = "slaviana88"

    def test_get_info(self):
        expected = {'followers': ['peter359', '6desislava6', 'PavlinGergov', 'miglen', \
        'Rositsazz', 'kbadova', 'ruzhaa', 'zorie', 'stanislavBozhanov', 'boyski33'], \
        'following': ['RadoRado', 'IvayloT', 'frisibeli', '6desislava6', 'Rositsazz', 'PavlinGergov']}

        self.assertEqual(self.network.get_info(self.username), expected)

    def test_do_you_follow(self):
        user = 'frisibeli'
        self.assertTrue(self.network.do_you_follow(user))

    def test_do_you_follow_indirectly(self):
        user = 'Ivaylo-Bachvarov'
        self.assertTrue(self.network)

if __name__ == '__main__':
    unittest.main()

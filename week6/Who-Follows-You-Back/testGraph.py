import unittest
from graph import DirectedGraph, GithubSocialNetwork

class graphTests(unittest.TestCase):
    def setUp(self):
        self.graph = DirectedGraph()
        self.network = GithubSocialNetwork("slaviana88", 2)
        self.username = "slaviana88"

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


if __name__ == '__main__':
    unittest.main()

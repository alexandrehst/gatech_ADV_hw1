import unittest
from submission import TMDBAPIUtils, Graph

class Test_Q1(unittest.TestCase):

    def test_get_movie_cast_ok(self):
        tmdb_api_utils = TMDBAPIUtils('68c675b4eb94bd6b2124432798e79f67')

        movie_cast = tmdb_api_utils.get_movie_cast('550', None, None)

        self.assertTrue(movie_cast )

    def test_get_movie_cast_nok(self):
        tmdb_api_utils = TMDBAPIUtils('68c675b4eb94bd6b2124432798e79f67')

        movie_cast = tmdb_api_utils.get_movie_cast('412', None, None)

        self.assertFalse(movie_cast )

    def test_get_movie_cast_exclude(self):
        tmdb_api_utils = TMDBAPIUtils('68c675b4eb94bd6b2124432798e79f67')

        movie_cast = tmdb_api_utils.get_movie_cast('550', None, [287])
        
        item_check = None
        for item in movie_cast:
            if item['id'] == 287:
                item_check = item

        self.assertIsNone(item_check)

    def test_get_movie_cast_limit(self):
        tmdb_api_utils = TMDBAPIUtils('68c675b4eb94bd6b2124432798e79f67')

        movie_cast = tmdb_api_utils.get_movie_cast('550', 5, None)
        
        item_check = []
        for item in movie_cast:
            if item['order'] not in range(5):
                item_check.append(item)

        self.assertEqual(len(item_check),0)
        
    def test_get_person_movie_cast(self):
        tmdb_api_utils = TMDBAPIUtils('68c675b4eb94bd6b2124432798e79f67')

        movie_cast = tmdb_api_utils.get_movie_credits_for_person( '287', None)

        self.assertIsNotNone( movie_cast)

    def test_get_person_movie_cast_threshold(self):
        tmdb_api_utils = TMDBAPIUtils('68c675b4eb94bd6b2124432798e79f67')

        movie_cast = tmdb_api_utils.get_movie_credits_for_person( '287', 8.5)

        self.assertEqual( len(movie_cast), 1)

class Test_graph(unittest.TestCase):
    def test_add_node(self):
        graph = Graph()
        graph.add_node(id='2975', name='Laurence Fishburne')

        self.assertEqual( len(graph.nodes), 1)

    def test_add_node_duplicated(self):
        graph = Graph()
        graph.add_node(id='2975', name='Laurence Fishburne')
        graph.add_node(id='2975', name='Laurence Fishburne')

        self.assertEqual( len(graph.nodes), 1)
    
    def test_add_edges(self):
        graph = Graph()
        graph.add_edge('2975', '443')

        check = ('2975', '443')

        self.assertEqual( graph.edges[0], check)

    def test_add_edges_duplicated(self):
        graph = Graph()

        graph.add_edge('2975', '443')
        graph.add_edge('2975', '443')

        check = [('2975', '443')]

        self.assertListEqual( graph.edges, check)        

    def test_max_nodes(self):
        graph = Graph()

        graph.add_edge('1', '2')
        graph.add_edge('1', '3')
        graph.add_edge('2', '3')
        graph.add_edge('4', '1')
        graph.add_edge('4', '6')
        graph.add_edge('5', '4')

        max_nodes = graph.max_degree_nodes()
        check = {'1':3, '4':3}

        self.assertDictEqual( max_nodes, check) 
    def test_leaf_nodes(self):
        graph = Graph()

        graph.add_edge('1', '2')
        graph.add_edge('2', '3')
        graph.add_edge('1', '4')

        leaf_nodes = graph.count_leaf_nodes()

        self.assertEqual( leaf_nodes, 2)         
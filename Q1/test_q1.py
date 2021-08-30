import unittest
from submission import TMDBAPIUtils

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

    

import unittest
from rental import Rental
from movie import Movie
from pricing import NEW_RELEASE, REGULAR, CHILDREN


class RentalTest(unittest.TestCase):

    def setUp(self):
        self.new_movie = Movie("Dune: Part Two", 2023, ["Action", "Sci-Fi"])
        self.regular_movie = Movie("Air", 2023, ["Drama"])
        self.childrens_movie = Movie("Frozen", 2013, ["Animation", "Family"])

    def test_movie_attributes(self):
        """Trivial test to catch refactoring errors or change in API of Movie"""
        m = Movie("Air", 2023, ["Drama"])
        self.assertEqual("Air", m.title)
        self.assertEqual(2023, m.year)
        self.assertIn("Drama", m.genre)

    # @unittest.skip("add this test when you refactor rental price")
    def test_rental_price(self):
        """Test rental price calculation for different movie types"""
        # New release pricing
        rental1 = Rental(self.new_movie, 1, NEW_RELEASE)
        self.assertEqual(rental1.get_price(), 3.0)

        rental1 = Rental(self.new_movie, 5, NEW_RELEASE)
        self.assertEqual(rental1.get_price(), 15.0)

        rental2 = Rental(self.regular_movie, 2, REGULAR)
        self.assertEqual(rental2.get_price(), 2.0)

        rental2 = Rental(self.regular_movie, 3, REGULAR)
        self.assertEqual(rental2.get_price(), 3.5)

        rental3 = Rental(self.childrens_movie, 3, CHILDREN)
        self.assertEqual(rental3.get_price(), 1.5)

        rental3 = Rental(self.childrens_movie, 4, CHILDREN)
        self.assertEqual(rental3.get_price(), 3.0)

    # @unittest.skip("add this test of rental points when you add it to Rental")
    def test_rental_points(self):
        """Test rental points calculation for different movie types"""
        rental1 = Rental(self.new_movie, 3, NEW_RELEASE)
        self.assertEqual(rental1.rental_points(), 3)

        rental2 = Rental(self.regular_movie, 5, REGULAR)
        self.assertEqual(rental2.rental_points(), 1)

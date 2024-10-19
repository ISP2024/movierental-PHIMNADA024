import unittest
from rental import Rental
from movie import Movie


class RentalTest(unittest.TestCase):

    def setUp(self):
        self.new_movie = Movie("Dune: Part Two", 2024, ["Action", "Sci-Fi"])
        self.regular_movie = Movie("Air", 2023, ["Drama"])
        self.childrens_movie = Movie("Frozen", 2013, ["Animation", "Family", "Children"])

    def test_movie_attributes(self):
        """Trivial test to catch refactoring errors or change in API of Movie"""
        m = Movie("Air", 2023, ["Drama"])
        self.assertEqual("Air", m.title)
        self.assertEqual(2023, m.year)
        self.assertIn("Drama", m.genre)

    def test_rental_price(self):
        """Test rental price calculation for different movie types"""
        # New release pricing (automatic price code determination)
        rental1 = Rental(self.new_movie, 1)
        self.assertEqual(rental1.get_price(), 3.0)

        rental1 = Rental(self.new_movie, 5)
        self.assertEqual(rental1.get_price(), 15.0)

        # Regular movie pricing
        rental2 = Rental(self.regular_movie, 2)
        self.assertEqual(rental2.get_price(), 2.0)

        rental2 = Rental(self.regular_movie, 3)
        self.assertEqual(rental2.get_price(), 3.5)

        # Children's movie pricing
        rental3 = Rental(self.childrens_movie, 3)
        self.assertEqual(rental3.get_price(), 1.5)

        rental3 = Rental(self.childrens_movie, 4)
        self.assertEqual(rental3.get_price(), 3.0)

    def test_rental_points(self):
        """Test rental points calculation for different movie types"""
        rental1 = Rental(self.new_movie, 3)
        self.assertEqual(rental1.rental_points(), 3)

        rental2 = Rental(self.regular_movie, 5)
        self.assertEqual(rental2.rental_points(), 1)

        rental3 = Rental(self.childrens_movie, 4) 
        self.assertEqual(rental3.rental_points(), 1)

import unittest
from datetime import datetime
from rental import Rental
from movie import Movie
from pricing import NEW_RELEASE, REGULAR, CHILDREN


class PricingTest(unittest.TestCase):
    """Tests for Rental.price_code_for_movie"""

    def test_new_release(self):
        """Test that a movie released this year is a new release."""
        current_year = datetime.now().year
        movie = Movie("Fast & Furious", current_year, ["Action"])
        self.assertEqual(Rental.price_code_for_movie(movie), NEW_RELEASE)

    def test_children_genre(self):
        """Test that a movie with 'Children' genre returns CHILDREN price."""
        movie = Movie("Frozen", 2013, ["Children", "Animation"])
        self.assertEqual(Rental.price_code_for_movie(movie), CHILDREN)

    def test_childrens_genre_variant(self):
        """Test that a movie with 'Childrens' genre (variant spelling) returns CHILDREN price."""
        movie = Movie("The Lion King", 1994, ["Childrens", "Adventure"])
        self.assertEqual(Rental.price_code_for_movie(movie), CHILDREN)

    def test_regular_movie(self):
        """Test that a movie with neither 'Children' genre nor current year is regular price."""
        movie = Movie("Inception", 2010, ["Sci-Fi", "Thriller"])
        self.assertEqual(Rental.price_code_for_movie(movie), REGULAR)

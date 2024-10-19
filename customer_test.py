import re
import unittest
from customer import Customer
from rental import Rental
from movie import Movie


class CustomerTest(unittest.TestCase):
    """Tests of the Customer class"""

    def setUp(self):
        """Test fixture contains:
        c = a customer
        movies = list of some movies
        """
        self.c = Customer("Movie Mogul")
        self.new_movie = Movie("Mulan", 2024, ["Action"])
        self.regular_movie = Movie("CitizenFour", 2014, ["Documentary"])
        self.childrens_movie = Movie("Frozen", 2013, ["Children"])

    @unittest.skip("No convenient way to test")
    def test_billing():
        # no convenient way to test billing since it's buried in the statement() method.
        pass

    def test_statement(self):
        """Test the statement generation for a customer"""
        stmt = self.c.statement()
        # get total charges from statement using a regex
        pattern = r".*Total [Cc]harges\s+(\d+\.\d\d).*"
        matches = re.match(pattern, stmt, flags=re.DOTALL)
        self.assertIsNotNone(matches)
        self.assertEqual("0.00", matches[1])

        # Add a new release movie rental
        self.c.add_rental(Rental(self.new_movie, 4))  # days
        stmt = self.c.statement()
        matches = re.match(pattern, stmt.replace('\n', ''), flags=re.DOTALL)
        self.assertIsNotNone(matches)
        self.assertEqual("12.00", matches[1])

    def test_total_charge(self):
        """Test the total charge calculation"""
        self.c.add_rental(Rental(self.new_movie, 3))
        self.c.add_rental(Rental(self.regular_movie, 2))
        self.c.add_rental(Rental(self.childrens_movie, 4))
        self.assertEqual(self.c.get_total_charge(), 14)

    def test_total_rental_points(self):
        """Test the total frequent renter points calculation"""
        self.c.add_rental(Rental(self.new_movie, 10))
        self.c.add_rental(Rental(self.regular_movie, 5))
        self.c.add_rental(Rental(self.childrens_movie, 12))
        self.assertEqual(self.c.get_total_rental_points(), 12)

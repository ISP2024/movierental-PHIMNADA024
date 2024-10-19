# Demonstrate the movie rental code.
# Create a customer with some movies and print a statement.

from rental import Rental
from customer import Customer
from movie_catalog import MovieCatalog


def make_movies():
    """Some sample movies."""
    movies = [
        MovieCatalog().get_movie("Fair Play"),
        MovieCatalog().get_movie("Oppenheimer"),
        MovieCatalog().get_movie("Deadpool"),
        MovieCatalog().get_movie("Bitconned"),
        MovieCatalog().get_movie("Particle Fever")
    ]
    return movies


if __name__ == '__main__':
    # Create a customer with some rentals
    customer = Customer("Edward Snowden")
    days = 1
    for movie in make_movies():
        customer.add_rental(Rental(movie, days))
        days = (days + 2) % 5 + 1
    print(customer.statement())

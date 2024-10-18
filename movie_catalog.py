import csv
from typing import Optional
from movie import Movie


class MovieCatalog:
    _instance = None
    _movies = []

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(MovieCatalog, cls).__new__(cls)
            cls._instance.load_movies('movies.csv')
        return cls._instance

    def load_movies(self, filename: str):
        """Reads the movie data from a CSV file and creates Movie objects."""
        try:
            with open(filename, 'r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file, delimiter=',')
                next(reader)
                for row in reader:
                    try:
                        title, year, genres = row[1], int(row[2]), row[3].split('|')
                        self._movies.append(Movie(title=title, year=year, genre=genres))
                    except (IndexError, ValueError):
                        continue
        except FileNotFoundError:
            print(f"Error: The file '{filename}' was not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def get_movie(self, title: str, year: Optional[int] = None) -> Optional[Movie]:
        """Returns a movie with the matching title and optional year."""
        for movie in self._movies:
            if movie.title.lower() == title.lower() and (year is None or movie.year == year):
                return movie
        return None

## Movie Rental Refactoring

A classic refactoring problem from Chapter 1 of
_Refactoring: Improving the Design of Existing Code_ by Martin Fowler.  

This repository contains Python code translated from the Java version.

The runnable `main.py` creates a customer and prints a statement.


## Instructions

See [Movie Rental Refactoring, Part 1](https://cpske.github.io/ISP/assignment/movierental/movierental-part1) for description of the code and what to do.

Before and after each refactoring you should **run the unit tests**.

## Resources

See [Resources](https://cpske.github.io/ISP/assignment/movierental/movierental-part1#resources) in the assignment description.

## Rationale

**2.1 what refactoring signs (code smells) suggest this refactoring?**

**Answer** Feature Envy because Rental relies on movie's price_code to calculate prices and points. 
This indicates Rental envies functionality that should belong to it. 
Moving price_code to Rental reduces unnecessary dependency and improves clarity.

**2.2 what design principle suggests this refactoring? Why?**

**Answer** Single Responsibility Principle (SRP) because the Movie class should only manage movie details, not pricing.
Moving price_code and related methods to Rental ensures each class handles its own responsibility, improving cohesion and adhering to SRP.

**5.2 Describe where you implement this method and the reasons for your choice.**

**Answer** I chose to implement the price_code_for_movie method in the Rental class by using these 2 design principles.

**High Cohesion and Information Expert:** Rental class is used for managing the movie rentals, it knows about the movie's release year and genre. It also has the day rented. These information can be used to calculate the rental price, rental points, and also can get price code for each movie.

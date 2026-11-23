"""Reusable helper functions for the Week 4 hands-on lab."""


def add_numbers(first, second):
    """Return the sum of two numbers."""
    return first + second


def is_pass(score, pass_mark=50):
    """Return True when score meets or exceeds the pass mark."""
    return score >= pass_mark


def greet(name, greeting="Hello"):
    """Return a greeting for the supplied name."""
    return f"{greeting}, {name}!"

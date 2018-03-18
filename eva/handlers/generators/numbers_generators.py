from random import choice


def random_password():
    """Randomly generates a six-digit password."""
    return choice(range(100000, 999999))

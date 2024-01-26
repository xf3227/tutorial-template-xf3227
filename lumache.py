"""
Lumache - Python library for cooks and food lovers.
"""

__version__ = "0.1.0"


class InvalidKindError(Exception):
    """Raised if the kind is invalid."""
    pass


def get_random_ingredients(kind=None):
    """
    Return a list of random ingredients as strings.

    :param kind: Optional "kind" of ingredients.
    :type kind: list[str] or None
    :raise lumache.InvalidKindError: If the kind is invalid.
    :return: The ingredients list.
    :rtype: list[str]
    """
    return ["shells", "gorgonzola", "parsley"]

class TestClass:
    """
    Test class.
    """
    def __init__(self, p1):
        """ __init__
        
        :param p1: __p1__
        :type p1: list[str] or None
        """
        pass

    def method_1(self, p1):
        """ method_1
        
        :param p1: __p1__
        :type p1: list[str] or None
        :rtype: list
        """
        pass

class Cube(object):
    # This cube needs help
    # Define a constructor which takes one integer, or handles no args
    def __init__(self, side=0):
        # Ensure the side length is non-negative
        self.__side = abs(side)

    def get_side(self):
        """Return the side of the Cube"""
        return self.__side

    def set_side(self, new_side):
        """Set the value of the Cube's side."""
        self.__side = abs(new_side)

class Block:
    def __init__(self, block):
        self.width = block[0]
        self.length = block[1]
        self.height = block[2]

    def get_width(self):
        return self.width

    def get_length(self):
        return self.length

    def get_height(self):
        return self.height

    def get_volume(self):
        return self.width * self.height * self.length

    def get_surface_area(self):
        return (2 * self.length * self.width) + (2 * self.height * self.length) + (2 * self.width * self.height)

    from operator import mul

    # class Block(object):
    #     def __init__(self, dimensions):
    #         self.dimensions = dimensions
    #
    #     def get_width(self):
    #         return self.dimensions[0]
    #
    #     def get_length(self):
    #         return self.dimensions[1]
    #
    #     def get_height(self):
    #         return self.dimensions[2]
    #
    #     def get_volume(self):
    #         return reduce(mul, self.dimensions)
    #
    #     def get_surface_area(self):
    #         w, l, h = self.dimensions
    #         return 2 * (w * l + l * h + w * h)
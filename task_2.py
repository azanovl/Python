class Road:

    def __init__(self, length, width, layers=5):
        self._length = length
        self._width = width
        self.layers = layers
        mass = self._length * self._width * self.layers
        print(f"При длине: {length} м.,  ширине: {width} м. и количестве слоев: {layers} "
              f"\nнеобходимо {mass} кг. асфальта. ")

Road(20, 30, 56)

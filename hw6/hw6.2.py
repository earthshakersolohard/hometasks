class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def culc_weight(self, thickness, sq_weight):
        print(self._length)
        print(self._width)
        print(thickness)
        print(sq_weight)

        return self._length * self._width * sq_weight * thickness

r = Road(85, 5)
print(f'{(r.culc_weight(8, 40))/1000} тонн асфальта необходимо для строительства дороги')
class Point3D:
    __slots__ = ('_x', '_y', '_z')

    def __init__(self, x, y, z):
        super().__setattr__("_x", x)
        super().__setattr__("_y", y)
        super().__setattr__("_z", z)

    def __setattr__(self, key, value):
        raise AttributeError("Özellik Değiştirilemez.")

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def z(self):
        return self._z

point = Point3D(1, 1, 1)
print(point.__slots__)
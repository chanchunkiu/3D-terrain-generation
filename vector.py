import math

class Vector3:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, v):
        return Vector3(self.x + v.x, self.y + v.y, self.z + v.z)

    def __sub__(self, v):
        return Vector3(self.x - v.x, self.y - v.y, self.z - v.z)

    def __mul__(self, k):
        return Vector3(self.x * k, self.y * k, self.z * k)

    def __truediv__(self, k):
        return Vector3(self.x / k, self.y / k, self.z / k)

    def __eq__(self, v):
        return self.x == v.x and self.y == v.y and self.z == v.z

    def __ne__(self, v):
        return self.x != v.x or self.y != v.y or self.z != v.z

    def __neg__(self):
        return Vector3(-self.x, -self.y, -self.z)

    def __getitem__(self, i):
        if i == 0:
            return self.x
        elif i == 1:
            return self.y
        return self.z

    def __setitem__(self, i, value):
        if i == 0:
            self.x = value
        elif i == 1:
            self.y = value
        else:
            self.z = value

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def __gt__(self, v):
        return self.x > v.x and self.y > v.y and self.z > v.z

    def __lt__(self, v):
        return self.x < v.x and self.y < v.y and self.z < v.z

    def __ge__(self, v):
        return self.x >= v.x and self.y >= v.y and self.z >= v.z

    def __le__(self, v):
        return self.x <= v.x and self.y <= v.y and self.z <= v.z

    def max(self):
        return max(self.x, self.y, self.z)

    def min(self):
        return min(self.x, self.y, self.z)

    def max_index(self):
        if self.x >= self.y:
            if self.x >= self.z:
                return 0
            else:
                return 2
        else:
            if self.y >= self.z:
                return 1
            else:
                return 2

    @staticmethod
    def min(a, b):
        return Vector3(min(a.x, b.x), min(a.y, b.y), min(a.z, b.z))

    @staticmethod
    def max(a, b):
        return Vector3(max(a.x, b.x), max(a.y, b.y), max(a.z, b.z))


def cross(u, v):
    return Vector3((u.y * v.z) - (u.z * v.y), (u.z * v.x) - (u.x * v.z), (u.x * v.y) - (u.y * v.x))


def dot(u, v):
    return u.x * v.x + u.y * v.y + u.z * v.z


def magnitude(u):
    return math.sqrt(u.x * u.x + u.y * u.y + u.z * u.z)


def squared_magnitude(u):
    return u.x * u.x + u.y * u.y + u.z * u.z


def normalize(v):
    kk = 1.0 / magnitude(v)
    return v * kk


class Vector2:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.x * other.x, self.y * other.y)
        else:
            return Vector2(self.x * other, self.y * other)

    def __truediv__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.x / other.x, self.y / other.y)
        else:
            return Vector2(self.x / other, self.y / other)

    def __neg__(self):
        return Vector2(-self.x, -self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __getitem__(self, i):
        if i == 0:
            return self.x
        return self.y

    def __setitem__(self, i, value):
        if i == 0:
            self.x = value
        else:
            self.y = value

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __lt__(self, other):
        return self.x < other.x and self.y < other.y

    def __ge__(self, other):
        return self.x >= other.x and self.y >= other.y

    def __le__(self, other):
        return self.x <= other.x and self.y <= other.y

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

    def __imul__(self, other):
        self.x *= other
        self.y *= other
        return self

    def __idiv__(self, other):
        self.x /= other
        self.y /= other
        return self

    def to_vector3(self, yy):
        return Vector3(self.x, yy, self.y)


    def max(self):
        return max(self.x, self.y)

    def min(self):
        return min(self.x, self.y)


def dot(u, v):
    return u.x * v.x + u.y * v.y


def magnitude(u):
    return math.sqrt(u.x * u.x + u.y * u.y)


def squared_magnitude(u):
    return u.x * u.x + u.y * u.y

def normalize(v):
    kk = 1.0 / magnitude(v)
    return v * kk
import math
from vector import Vector2, Vector3


class Box3D:
        def __init__(self, A, B=None):
            if B is None:
                C, R = A
                RR = Vector3(R)
                self.a = C - RR
                self.b = C + RR
            else:
                self.a = A
                self.b = B

        def contains(self, p):
            return p > self.a and p < self.b

        def extended(self, r):
            return Box3D(self.a - r, self.b + r)

        def distance(self, p):
            r = 0.0
            for i in range(3):
                if p[i] < self.a[i]:
                    s = p[i] - self.a[i]
                    r += s * s
                elif p[i] > self.b[i]:
                    s = p[i] - self.b[i]
                    r += s * s
            return r

        def vertex(self, i):
            if i == 0:
                return self.a
            return self.b

        def __getitem__(self, i):
            if i == 0:
                return self.a
            return self.b

        def set_parallelepipedic(self, size, xyz):
            d = self.b - self.a
            x, y, z = int(d[0] / size), int(d[1] / size), int(d[2] / size)

            if x == 0:
                x += 1
            if y == 0:
                y += 1
            if z == 0:
                z += 1

            c = (self.a + self.b) * 0.5
            e = Vector3(float(x), float(y), float(z)) * size / 2.0
            self.a = c - e
            self.b = c + e

            xyz[0], xyz[1], xyz[2] = x, y, z

        def set_parallelepipedic_n(self, n, xyz):
            d = self.b - self.a
            e = max(d.x, d.y, d.z)
            size = e / n
            self.set_parallelepipedic(size,xyz)

class Box2D:
    def __init__(self, A=None, B=None):
        if A is None and B is None:
            self.a = Vector2(0)
            self.b = Vector2(0)
        elif B is None:
            C, R = A
            RR = Vector2(R)
            self.a = C - RR
            self.b = C + RR
        else:
            self.a = A
            self.b = B

    def contains(self, p):
        return p > self.a and p < self.b

    def intersect(self, box):
        return not (self.a[0] >= box.b[0] or self.a[1] >= box.b[1] or self.b[0] <= box.a[0] or self.b[1] <= box.a[1])

    def distance(self, p):
        r = 0.0
        for i in range(2):
            if p[i] < self.a[i]:
                s = p[i] - self.a[i]
                r += s * s
            elif p[i] > self.b[i]:
                s = p[i] - self.b[i]
                r += s * s
        return r

    def vertex(self, i):
        if i == 0:
            return self.a
        return self.b

    def to_box(self, y_min, y_max):
        return Box3D(Vector3(self.a.x, y_min, self.a.y), Vector3(self.b.x, y_max, self.b.y))



    def __getitem__(self, i):
        if i == 0:
            return self.a
        return self.b

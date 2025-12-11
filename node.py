from box import Box3D
from vector import Vector3


class Node:
    def __init__(self):
        self.box = Box3D(Vector3(0), 1.0)
    
    def __init__(self, box):
        self.box = box
    
    def __del__(self):
        pass
    
    def Intensity(self):
        pass
    
    def Gradient(self, vector):
        Epsilon=1e-4
        if not self.GetBox().Contains(vector):
            return Vector3(0.0)
        x = self.Intensity(Vector3(vector[0] + Epsilon, vector[1], vector[2])) - self.Intensity(Vector3(vector[0] - Epsilon, vector[1], vector[2]))
        y = self.Intensity(Vector3(vector[0], vector[1] + Epsilon, vector[2])) - self.Intensity(Vector3(vector[0], vector[1] - Epsilon, vector[2]))
        z = self.Intensity(Vector3(vector[0], vector[1], vector[2] + Epsilon)) - self.Intensity(Vector3(vector[0], vector[1], vector[2] - Epsilon))
        return Vector3(x, y, z) / (2.0 * Epsilon)
    
    def GetBox(self):
        return self.box

class BinaryOp(Node):
    def __init__(self, a, b):
        self.e = [a, b]
        self.box = Box3D(self.e[0].GetBox(), self.e[1].GetBox())
    
    def __del__(self):
        del self.e[0]
        del self.e[1]

class BlendOp(BinaryOp):
    def __init__(self, a, b):
        super().__init__(a, b)
    
    def Intensity(self, vector):
        if not self.box.Contains(vector):
            return 0.0
        return self.e[0].Intensity(vector) + self.e[1].Intensity(vector)
    
    def Gradient(self, vector):
        if not self.box.Contains(vector):
            return Vector3(0.0)
        return self.e[0].Gradient(vector) + self.e[1].Gradient(vector)




from node import Node,BlendOp
class Tree:
    t = 7.5

    def __init__(self, n):
        self.root = n

    def Intensity(self, p):
        return self.root.Intensity(p) - self.t

    def Gradient(self, p):
        return self.root.Gradient(p)

    def Blend(self, n):
        self.root = BlendOp(self.root, n)

    def GetBox(self):
        return self.root.GetBox()

    @staticmethod
    def T():
        return Tree.t
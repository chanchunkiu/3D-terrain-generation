from node import Node
from box import Box3D
from vector import Vector3, Vector2
from perlinnosie import PerlinNoise
from maths_function import clamp, step, lerp, cubic_smooth_compact, cubic_sigmoid, cubic_smooth, cubic_smooth_step
from tree import Tree

class TerrainLeaf(Node):
    def __init__(self, b, X, r):
        super().__init__(b.extended(Vector3(0.0, r, 0.0)))
        self.x = X
        self.r = r
        self.localbox =b.extended(Vector3(-0.5 * r))

    def Intensity(self, p):
        if not self.box.contains(p):
            return 0.0
        z = self.Height(Vector2(p.x,p.z))
        dt = z - p[1]
        e = cubic_sigmoid(dt, self.r, Tree.T()) + Tree.T()
        f = 2.0 * Tree.T() * cubic_smooth_compact(self.localbox.distance(p), self.r * self.r * 0.25)
        return min(e, f)


class CliffLeaf(TerrainLeaf):
    def __init__(self, B, minMax, X, r, scales, amplitudes):
        super().__init__(B, X, r)  # Pass X and r to the TerrainLeaf constructor
        self.c = (Vector2(B.vertex(0).x, B.vertex(0).z) + Vector2(B.vertex(1).x, B.vertex(1).z)) / 2.0
        self.minMaxElevation = minMax
        self.scales = scales
        self.amplitudes = amplitudes
        
    def Height(self, p):
        q = p - self.c
        zc = self.minMaxElevation[0]
        for scale, amplitude in zip(self.scales, self.amplitudes):
            zc += amplitude * PerlinNoise.get_value(Vector3(q.x / scale, 0.0, q.y / scale))
        zc += self.minMaxElevation[1] * (0.5 + 0.5 * PerlinNoise.get_value(Vector3(q.x / 1050.0, 0.0, q.y / 1050.0)))
        zs = self.minMaxElevation[0] + 10.0
        qq_x = q.x + 135.0 * PerlinNoise.get_value(Vector3(q.x / 150.0, 0.24/150, q.y / 150.0)) + 75.0 * PerlinNoise.get_value(Vector3(q.x / 70.0, 0.24/70, q.y / 70.0))
        qq_y = q.y + 135.0 * PerlinNoise.get_value(Vector3(q.x / 150.0, 0.24/150, q.y / 150.0)) + 75.0 * PerlinNoise.get_value(Vector3(q.x / 70.0, 0.24/70, q.y / 70.0))
        qq = Vector2(qq_x, qq_y)
        u = cubic_smooth_step(qq[0], -35.0, 25.0)
        z = lerp(zs, zc, u)
        z += self.minMaxElevation[0] * step(-qq[0], -500.0, 500.0) + 2.0 * PerlinNoise.get_value(Vector2(q.x / 50.0, q.y / 50.0)) + 1.0 * PerlinNoise.get_value(Vector2(q.x / 25.0, q.y / 25.0))
        return clamp(z, self.minMaxElevation[0], self.minMaxElevation[1])

import bpy
import os
import sys
import numpy as np
from bpy.props import FloatProperty, FloatVectorProperty
from bpy.types import Panel, Operator
import math

# add project
current_dir = os.path.dirname(bpy.data.filepath)
if current_dir not in sys.path:
    sys.path.append(current_dir)

#add site packages to sys.path
user_site_packages = "/Users/your_username/Library/Python/3.10/lib/python/site-packages"
if user_site_packages not in sys.path:
    sys.path.append(user_site_packages)

from vector import Vector2, Vector3  
from box import Box2D
from terrain import CliffLeaf
from tree import Tree
from skimage import measure


def register_properties():
    bpy.types.Scene.minAlt = FloatProperty(name="Min Altitude", default=0, min=0, max=7000, step=10)
    bpy.types.Scene.maxAlt = FloatProperty(name="Max Altitude", default=200, min=0, max=700, step=10)
    bpy.types.Scene.testing_X = FloatProperty(name="Vertical Scale", default=50.0, min=0, max=100, step=1)
    bpy.types.Scene.testing_r = FloatProperty(name="Radius of Smoothing", default=10.0, min=0, max=50, step=1)
    bpy.types.Scene.scale = FloatProperty(name="Perlin noise scale", default=5000.0, min=0, max=10000, step=100)
    bpy.types.Scene.scale_2 = 3000.0  #default, not adjust in ui
    bpy.types.Scene.scale_3 = 1500.0  #default, not adjust in ui
    bpy.types.Scene.amplitude_1 = FloatProperty(name="Amplitude 1", default=15.0, min=0, max=500, step=10)
    bpy.types.Scene.amplitude_2 = FloatProperty(name="Amplitude 2", default=7.0, min=0, max=500, step=10)
    bpy.types.Scene.amplitude_3 = FloatProperty(name="Amplitude 3", default=20.0, min=0, max=500, step=10)
    print("Properties registered.")

def unregister_properties():
    del bpy.types.Scene.minAlt
    del bpy.types.Scene.maxAlt
    del bpy.types.Scene.testing_X
    del bpy.types.Scene.testing_r
    del bpy.types.Scene.scale
    del bpy.types.Scene.amplitude_1
    del bpy.types.Scene.amplitude_2
    del bpy.types.Scene.amplitude_3
    print("Properties unregistered.")

# panel class
class CliffLeafPanel(Panel):
    bl_label = "Cliff Leaf Parameters"
    bl_idname = "VIEW3D_PT_cliff_leaf"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Custom Terrain'

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        layout.label(text="Custom Panel Test")
        layout.prop(scene, "minAlt", slider=True)
        layout.prop(scene, "maxAlt", slider=True)
        layout.prop(scene, "testing_X", slider=True)
        layout.prop(scene, "testing_r", slider=True)
        layout.prop(scene, "scale", slider=True)
        layout.label(text="Perlin Noise Amplitudes")
        layout.prop(scene, "amplitude_1", slider=True)
        layout.prop(scene, "amplitude_2", slider=True)
        layout.prop(scene, "amplitude_3", slider=True)

        # generate button
        layout.operator("object.generate_terrain", text="Generate Terrain")

sizeX = 700
sizeY = 700

#function to generate terrain
def generate_terrain():
    print("Starting terrain generation...")
    bpy.ops.object.select_all(action='DESELECT')
    bpy.ops.object.select_by_type(type='MESH')
    bpy.ops.object.delete()
    scene = bpy.context.scene
    try:
        minAlt = scene.minAlt
        maxAlt = scene.maxAlt
        testing_X = scene.testing_X
        testing_r = scene.testing_r
        scales = scene.scales
        amplitudes = (scene.amplitude_1, scene.amplitude_2, scene.amplitude_3)
        print(f"Properties accessed successfully:\n minAlt: {minAlt}\n maxAlt: {maxAlt}\n testing_X: {testing_X}\n testing_r: {testing_r}\n scales: {scales}\n amplitudes: {amplitudes}")
    except AttributeError as e:
        print(f"Error accessing properties: {e}")
        return

  
    bbox = Box2D(Vector2(-sizeY / 2.0, -sizeX / 2.0), Vector2(sizeY / 2.0, sizeX / 2.0))
    cliff = CliffLeaf(bbox.to_box(minAlt, maxAlt), Vector2(minAlt, maxAlt), testing_X, testing_r, scales, amplitudes)
    terrainTree = Tree(cliff)

    #scalar field
    grid_size = 50 #resolution
    x = np.linspace(bbox.a.x, bbox.b.x, grid_size)
    y = np.linspace(minAlt, maxAlt, grid_size)
    z = np.linspace(bbox.a.y, bbox.b.y, grid_size)

    X, Y, Z = np.meshgrid(x, y, z, indexing='ij')
    scalar_field = np.zeros(X.shape)

    for i in range(grid_size):
        for j in range(grid_size):
            for k in range(grid_size):
                scalar_field[i, j, k] = terrainTree.Intensity(Vector3(X[i, j, k], Y[i, j, k], Z[i, j, k]))

    print("Scalar field generated.")

    #generate mesh by marching cubes
    verts, faces, _, _ = measure.marching_cubes(scalar_field, level=0, spacing=(x[1] - x[0], y[1] - y[0], z[1] - z[0]))
    print("Mesh vertices and faces generated.")
    #center mesh
    verts -= np.mean(verts, axis=0)
    print("Mesh centered.")
    #create new mesh
    mesh = bpy.data.meshes.new(name="TerrainMesh")
    mesh.from_pydata(verts.tolist(), [], faces.tolist())
    mesh.update()

    #create object from mesh
    obj = bpy.data.objects.new("TerrainMeshObject", mesh)

    #link object to scene
    scene = bpy.context.scene
    scene.collection.objects.link(obj)

    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)

    obj = bpy.context.scene.objects['TerrainMeshObject']
    obj.rotation_euler = (math.radians(90), 0, math.radians(180))
    #scale the terrain
    obj.scale = (1,1,1)

    print("Terrain generation completed.")

class GenerateTerrainOperator(Operator):
    bl_idname = "object.generate_terrain"
    bl_label = "Generate Terrain"

    def execute(self, context):
        generate_terrain()
        return {'FINISHED'}

def register():
    print("Registering")
    bpy.utils.register_class(CliffLeafPanel)
    register_properties()
    bpy.utils.register_class(GenerateTerrainOperator)
    print("Panel and properties registered successfully.")
    generate_terrain()  

def unregister():
    print("Unregistering")
    bpy.utils.unregister_class(CliffLeafPanel)
    unregister_properties()
    bpy.utils.unregister_class(GenerateTerrainOperator)
    print("Panel and properties unregistered successfully.")

if __name__ == "__main__":
    register()
    print("Successfully executed.")
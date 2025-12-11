# 3D-terrain-generation
Simplify the terrain development process by implementing an interface to control parameters for artists

<img width="1125" height="634" alt="image" src="https://github.com/user-attachments/assets/24abb0bf-f7f4-4194-8b14-4bd16fb62a6c" />

##Why is terrain important?

●Used in 3D environment

● Used for animation, simulation, video game


##Aim of project

● Terrain generation includes development and understanding of
complex algorithms

● Simplify the terrain development process by implementing an
interface to control parameters

● Easier approach for artists and designers

#Techniques used

Constructive approach
● Combination of similar shapes to create a complex terrain
feature
● Approach -> smoothly joining two planes that are carved into
each other

Data interpolation
● Mathematical technique
● To estimate unknown values that lie between ranges of known
data points
● It can interpolate between different height values to a smooth
terrain

Noise function
Perlin noise value is determined by the amplitude and frequency
● Amplitude affects the height
● Frequency affects the details -> high frequency ->small wavelegth
● Combine multiple layers results a complex and detail looking
terrain

<img width="2018" height="435" alt="image" src="https://github.com/user-attachments/assets/3db62ebd-3219-4587-b5a2-2c8d513f0f3e" />


Implicit surface
~Surface defined by f(x,y,z) = 0
~Includes all points satisfying the equation
~Point evaluated as inside, outside or on the surface
~Different features for terrain
~Terran height is determin by the function

Mesh generation
● Cube configuration : 15 ways an implicit surface intersect a
cube

Flow of system
1. User interacts with different parameters in the UI
2. The system process the parameters
3. Generate terrain with parameters
4. Easily identify and adjust parameters to change when not
satisfied

User interface
● Provide a user friendly experience for artists to adjust
the terrain according to their needs
They contol...
● Height of terrain
● Smoothness of terrain
● Details of terrain

<img width="581" height="945" alt="image" src="https://github.com/user-attachments/assets/e3c229f0-174e-4313-ae8a-f6d04705dafb" />


Rendering
Artist can render the result by adjusting shaderse, materials by themselves

<img width="1496" height="667" alt="image" src="https://github.com/user-attachments/assets/5ee16668-92bd-4a09-b6cc-f0c775e0cfe0" />


Result

change of attitude

<img width="1505" height="792" alt="image" src="https://github.com/user-attachments/assets/7979bc4b-d0a7-4437-a885-ce1f496654eb" />


<img width="1420" height="829" alt="image" src="https://github.com/user-attachments/assets/d186b7d0-b749-45c4-91f8-cee70af05076" />







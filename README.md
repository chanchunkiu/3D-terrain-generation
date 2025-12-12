# 3D-terrain-generation
A Python-based terrain generator that creates 3D landscapes with adjustable parameters and procedural noise functions.

<img width="1125" height="634" alt="image" src="https://github.com/user-attachments/assets/24abb0bf-f7f4-4194-8b14-4bd16fb62a6c" />

##Why is terrain important?

●Used in 3D environment

● Used for animation, simulation, and video games

## Features 
- Procedural 3D terrain generation

- Adjustable parameters (height, scale, smoothness, detail)

- Perlin-noise–based heightmap creation

- Automatic mesh construction

- Simple interface for artists/users

- Real-time visualisation of generated terrain by using 3D software Blender


## Flow of system

1. User interacts with different parameters in the UI
2. The system processes the parameters
3. Generate terrain with parameters
4. Easily identify and adjust parameters to change when not satisfied
5. Back to step 1


## Quick view

<img width="1505" height="792" alt="image" src="https://github.com/user-attachments/assets/7979bc4b-d0a7-4437-a885-ce1f496654eb" />


<img width="1420" height="829" alt="image" src="https://github.com/user-attachments/assets/d186b7d0-b749-45c4-91f8-cee70af05076" />

## Installation

git clone https://github.com/chanchunkiu/3D-terrain-generation.git

cd 3D-terrain-generation

### virtual environment
python -m venv venv
source venv/bin/activate     # Mac/Linux
venv\Scripts\activate        # Windows

### install libraries
pip install -r requirements.txt

### Run the project
Add main.py to the Blender script and run it

## Rendering
An artist can render the result by adjusting the shaders, materials by themselves

<img width="1496" height="667" alt="image" src="https://github.com/user-attachments/assets/5ee16668-92bd-4a09-b6cc-f0c775e0cfe0" />

## Project Overview

### This project demonstrates skills in:
- understand Perlin noise
- algorithms
- mesh construction
- interpolation
- ui design
- python development

It was created as my final project for university to explore how terrain tools can help artists rapidly experiment with landscapes.








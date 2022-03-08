from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import pickle

def buildStructure(x, y, z, structure):
    xStart = x
    zStart = z
    for row in structure:
        for column in row:
            for block in column:
                mc.setBlock(x, y, z, block)
                z += 1
            x += 1
            z = zStart
        y += 1
        x = xStart
        
#open and load the structure file
file = open("saveStructure.txt", "rb")
structure = pickle.load(file)

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z
buildStructure(x, y, z, structure)
file.close()
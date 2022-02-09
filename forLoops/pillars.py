from mcpi.minecraft import Minecraft
mc = Minecraft.create()

height = 6

def setPillar(x, y, z, height):
    """ Creates a pillar. Args set position and height of pillar """
    stairBlock = 156
    block = 155
    
    #Pillar top
    mc.setBlocks(x - 1, y + height, z - 1, x + 1, y + height, z + 1, block, 1)
    mc.setBlock(x - 1, y + height - 1, z, stairBlock, 12)
    mc.setBlock(x + 1, y + height - 1, z, stairBlock, 13)
    mc.setBlock(x, y + height - 1, z + 1, stairBlock, 15)
    mc.setBlock(x, y + height - 1, z - 1, stairBlock, 14)
    
    #Pillar  base
    mc.setBlocks(x - 1, y, z - 1, x + 1, y, z + 1, block, 1)
    mc.setBlock(x - 1, y + 1, z, stairBlock, 0)
    mc.setBlock(x + 1, y + 1, z, stairBlock, 1)
    mc.setBlock(x, y + 1, z + 1, stairBlock, 3)
    mc.setBlock(x, y + 1, z - 1, stairBlock, 2)
    
    #Pillar column
    mc.setBlocks(x, y, z, x, y + height, z, block, 2)
    
pos = mc.player.getTilePos()
a = 0
x, y, z =  pos.x + 2, pos.y, pos.z
for num in range(0, 10):
    a += 5
    setPillar(x + a, y, z, height)
    

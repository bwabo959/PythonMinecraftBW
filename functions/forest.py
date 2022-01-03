from mcpi.minecraft import Minecraft
mc = Minecraft.create()

tree = 0
def growTree(x,y,z): 
    mc.setBlock(x,y,z, 17)
    mc.setBlock(x,y+1,z, 17)
    mc.setBlock(x,y+2,z, 17)
    mc.setBlock(x,y+3,z, 17)
    mc.setBlock(x,y+4,z, 17)
    mc.setBlock(x,y+5,z, 18)
    mc.setBlock(x+1,y+4,z, 18)
    mc.setBlock(x,y+4,z, 18)
    mc.setBlock(x+1,y+4,z+1, 18)
    mc.setBlock(x,y+4,z+1, 18)
    mc.setBlock(x-1,y+4,z, 18)
    mc.setBlock(x-1,y+4,z-1, 18)
    mc.setBlock(x,y+4,z-1, 18)
    mc.setBlock(x+1,y+4,z-1, 18)
    mc.setBlock(x-1,y+4,z+1, 18)
    
    
        
        
    
pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

growTree(x+1,y,z)
growTree(x+3,y,z)
growTree(x+5,y,z)
growTree(x+7,y,z)
growTree(x+9,y,z)
growTree(x+11,y,z)
growTree(x+13,y,z)
growTree(x+15,y,z)
growTree(x+17,y,z)
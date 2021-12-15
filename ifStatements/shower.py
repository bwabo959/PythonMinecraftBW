from mcpi.minecraft import Minecraft
mc = Minecraft.create()

shwrX = 70.0
shwrY = 0.0
shwrZ = 70.0

width = 1
height = 5
length = 1

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

if shwrX <= x < shwrX + width and shwrY <= y < shwrY + height and shwrZ <= z < shwrZ + length:
    mc.setBlocks(shwrX, shwrY + height, shwrZ, shwrX + width, shwrY + height, shwrZ + length, 8)
else:
    mc.setBlocks(shwrX, shwrY + height, shwrZ, shwrX + width, shwrY + height, shwrZ + length, 0)

        

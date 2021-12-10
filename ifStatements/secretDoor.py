from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x = -0.7
y = 55.0
z = -104.4

gift = mc.getBlock(x, y, z)
if gift == 57:
    mc.setBlock(0.3, 54.0, -103.4, 0)
    mc.setBlock(0.3, 55.0, -103.4, 0)
elif gift == 0:
    mc.postToChat("Place an offering on the pedestal.")
else:
   pos = mc.player.getPos()
   x = pos.x
   y = pos.y
   z = pos.z
   mc.setBlock(x,y, z + 1, 11)
    
    

    
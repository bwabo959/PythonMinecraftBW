from mcpi.minecraft import Minecraft
mc = Minecraft.create()
buildX = -7.5
buildY = 0.0
buildZ = 73.9
width = 4
height = 5
length = 7
 
pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z
 
inside = buildX< x< buildX + width and buildY < y < buildY + height and buildZ< z< buildZ + length
mc.postToChat("The player is at home: " + str(inside))
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import time

pos = mc.player.getTilePos()
x, y, z = pos.x, pos.y, pos.z


yur = 0

for num in range(0, 49):
    yur += 1
    blockBelow = mc.getBlock(x, y - yur, z)
    if blockBelow == 56:
        mc.postToChat("There are diamonds here at: " +  str(y - yur))
        break
    else:
        mc.postToChat("No diamonds bum.")
        
        

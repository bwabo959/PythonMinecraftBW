from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import time

heights = [100, 0]
count = 0

while count < 10:
    pos = mc.player.getTilePos()
    x = pos.x
    y = pos.y
    z = pos.z
    
    if y < heights[0]:
        heights[0] = y
        
    elif y > heights[1]:
        heights[1] = y
        
    count += 1
    time.sleep(1)
    
mc.postToChat("Lowest: ", str(heights[0]))
mc.postToChat("Highest: ", str(heights[1]))
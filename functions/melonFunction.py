from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import time


def placeMelon():
    pos = mc.player.getPos()
    x = pos.x
    y = pos.y - 1
    z = pos.z
    mc.setBlock(x, y, z, 103)
    time.sleep(10)
    
placeMelon()
placeMelon()
placeMelon()
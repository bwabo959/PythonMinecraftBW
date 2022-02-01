from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import random


ids = [57, 21, 41, 42, 22, 73]

pos =  mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

block = random.choice(ids)

mc.setBlock(x + 1, y, z, block)
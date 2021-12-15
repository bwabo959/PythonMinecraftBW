import random
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

count = 0
while count < 5:
    time.sleep(10)
    x = random.randint(-127, 127)
    y = random.randint(0, 64)
    z = random.randint(-127, 127)
    mc.player.setTilePos(x,y,z)
    count += 1
    
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

x = 15.0
y = 10.0
z = 15.0

mc.player.setTilePos(x,y,z)

#wait ten seconds
time.sleep(10)

x = 20.0
y = 20.0
z = 20.0

mc.player.setTilePos(x,y,z)
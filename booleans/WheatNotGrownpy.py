from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x = 25
y = 0
z = 5
wheat = 59
block = mc.getBlock(x, y, z)

noWheat = block != wheat
    
mc.postToChat("You need to get some food: " + str(noWheat))
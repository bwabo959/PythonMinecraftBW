from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z

blockType = mc.getBlock(x, y - 1, z)
if blockType == 18 or blockType == 17:
    mc.postToChat("The player is in a tree: True" )
else:
    mc.postToChat("The player is in a tree: False" )
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
pos = mc.player.getTilePos()
x = pos.x
y = pos.y
y = y - 1
z = pos.z
blockType = 10
mc.setBlock(x ,y, z, blockType)
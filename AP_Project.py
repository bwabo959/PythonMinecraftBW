from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

items = []

def getBlocks(x,y,z):
    block2 = mc.getBlock(x,y,z)       
    if block2 == 3:
        items.append(57)
        mc.setBlock(x,y,z, 0)
    elif block2 == 103:
        items.append(42)
        mc.setBlock(x,y,z, 0)
    elif block2 == 46:
        items.append(41)
        mc.setBlock(x,y,z, 0)
    elif block2 == 35:
        items.append(56)
        mc.setBlock(x,y,z, 0)
    elif block2 == 5:
        items.append(15)
        mc.setBlock(x,y,z, 0)
    elif block2 == 22:
        items.append(14)
        mc.setBlock(x,y,z, 0)
    elif block2 == 87:
        items.append(58)
        mc.setBlock(x,y,z, 0)
    elif block2 == 12:
        items.append(61)
        mc.setBlock(x,y,z, 0)
    elif block2 == 1:
        items.append(47)
        mc.setBlock(x,y,z, 0)

x = 45
y = 17
z = -50
block = mc.getBlock(x,y,z)

block2 = mc.getBlock(51, 20, -46)

while block != 45:
    mc.postToChat("Place a brick block down")
    time.sleep(5)
    x = 45
    y = 17
    z = -50
    block = mc.getBlock(x,y,z)
    

if block == 45:
    mc.postToChat("what item would you like?")
    mc.postToChat("Diamond Block = Dirt")
    mc.postToChat("Iron Block = Melon")
    mc.postToChat("Gold Block = TnT")
    mc.postToChat("Diamond Ore = White Wool")
    mc.postToChat("Iron Ore = Oak Planks")
    mc.postToChat("Gold Ore = Lapiz Block")
    mc.postToChat("Crafting Table = Netherrack")
    mc.postToChat("Furnace = Sand")
    mc.postToChat("Bookshelf = Stone")


if block == 45:
    time.sleep(3)
    getBlocks(47,17,-50)
    mc.setBlock(51,16,-47, items[0])
    time.sleep(3)
    getBlocks(47,17,-50)
    mc.setBlock(51,17,-47, items[1])
    time.sleep(3)
    getBlocks(47,17,-50)
    mc.setBlock(51,18,-47, items[2])
    time.sleep(3)
    getBlocks(47,17,-50)
    mc.setBlock(51,19,-47, items[3])
    time.sleep(3)
    getBlocks(47,17,-50)
    mc.setBlock(51,20,-47, items[4])
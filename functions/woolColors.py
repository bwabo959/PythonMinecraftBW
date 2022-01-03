from mcpi.minecraft import Minecraft
mc = Minecraft.create()

def getWoolState(color):
    """ Takes a color as a string and returns the wool block state for that color """
    if color == "pink":
        blockState = 6
    elif color == "black":
        blockState = 15
    elif color == "white":
        blockState = 0
        
colorString = input("Enter a block color: ")
state = getWoolState(colorString)

pos = mc.player.getTilePos()
mc.setBlock(pos.x, pos.y, pos., 35, state) 

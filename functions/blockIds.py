from mcpi.minecraft import Minecraft
mc = Minecraft.create()

def melon():
    """ Returns the value of the melon block"""
    return 103

def water():
    """ Returns the value of the water block"""
    return 9

def wool():
    """ Returns the value of the wool block"""
    return 35

def lava():
    """ Returns the value of the lava block"""
    return 11

def TNT():
    """ Returns the value of the TNT block"""
    return 46

def flower():
    """ Returns the value of the flower block"""
    return 38

def diamond():
    """ Returns the value of the diamond block"""
    return 57

block = TNT()
pos = mc.player.getTilePos()
mc.setBlock(pos.x,pos.y,pos.z, block)
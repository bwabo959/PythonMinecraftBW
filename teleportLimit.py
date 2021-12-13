from mcpi.minecraft import Minecraft
mc = Minecraft.create()
valid = True
pos = mc.player.getTilePos()
Y = pos.y

x = int(input("Enter x: "))
y = int(input("Enter y: "))
z = int(input("Enter z: "))
height = mc.getHeight(x,z)

if not -127 < x < 127:
    valid = False
if not -63 < y < 63:
    valid = False
if not -127 < z < 127:
    valid = False
if height < Y:
    valid = False
    
if valid == True:
    mc.player.setPos(x,y,z)
else:
    mc.postToChat("Please enter a valid number")


from mcpi.minecraft import Minecraft
mc = Minecraft.create()
valid = True

pos = mc.player.getTilePos()
x1 = pos.x
y2 = pos.y
z3 = pos.z
height = mc.getHeight(x1,z3)

x = int(input("Enter x: "))
y = int(input("Enter y: "))
z = int(input("Enter z: "))

if not -127 < x < 127:
    valid = False
if not -63 < y < 63:
    valid = False
if not -127 < z < 127:
    valid = False
    
if height > y:
    valid = False
    
if valid:
    mc.player.setPos(x,y,z)
else:
    mc.postToChat("Please enter a valid location")
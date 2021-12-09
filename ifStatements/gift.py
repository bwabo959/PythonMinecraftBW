from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x = -9.3
y = 0.0
z = 99.5
gift = mc.getBlock(x, y, z)

if gift == 57:
    mc.postToChat("Thanks for the diamond.")
elif gift == 6:
    mc.postToChat("I guess tree sapplings are as good as diamonds...")
else:
    mc.postToChat("Bring a gift to the coordinates.")
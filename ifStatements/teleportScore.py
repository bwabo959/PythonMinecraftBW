from mcpi.minecraft import Minecraft
mc = Minecraft.create()

points = input("Enter your key word: ")
if points == "sea fortress":
    mc.player.setPos(32, 18, -38)
elif points == "tree house":
    mc.player.setPos(60, 20, 32)
elif points == "castle":
     mc.player.setPos(112, 10, 112)
elif points == "house":
    mc.player.setPos(0, 12, 20)
else:
    mc.postToChat("I don't know what to do with that information.")
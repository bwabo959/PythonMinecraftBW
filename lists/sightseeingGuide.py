from mcpi.minecraft import Minecraft
mc = Minecraft.create()

places = {'Brick Hut': (-50, 0, -14), 'Stone Hut': (-27, 2, -14)}

choice = ""
while choice != "exit":
    choice = input("Enter a location ('exit' to close): ")
    if choice in places:
        location = places[choice]
        x, y, z = location[0], location[1], location[2]
        mc.player.setTilePos(x,y,z)
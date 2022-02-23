from mcpi.minecraft import Minecraft
mc = Minecraft.create()

toDoList = open("/home/pi/PythonMinecraftBW/files/toDoFile.txt","r")

for line in toDoList:
    mc.postToChat(line)
    
    

toDoList.close()
    
    
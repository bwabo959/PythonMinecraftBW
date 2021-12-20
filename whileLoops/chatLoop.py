from mcpi.minecraft import Minecraft
mc= Minecraft.create()
username = input("Enter your name: ")

while True:
    message = input("Enter your message: ")
    if message == "exit":
        break
    else:
        mc.postToChat(username + message)
    
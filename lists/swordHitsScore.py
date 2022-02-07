from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import time

name = ""
scoreboard = {}

while True:
    name = input("What is your name? ")
    if name == "exit":
        break
    mc.postToChat("Go!")

    time.sleep(10)

    blockHits = mc.events.pollBlockHits()

    blockhitsLength = len(blockHits)
    mc.postToChat("Your score is " + str(blockhitsLength))

    scoreboard[name] = str(blockhitsLength)

    print(scoreboard)
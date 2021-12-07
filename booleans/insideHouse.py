from mcpi. minecraft import minecraft
mc = minecraft.create()
 buildX =
 buildY =
 buildZ =
 width = 10
 height = 5
 length = 6
 
 pos = mc.player.getTilePos()
 x = pos.x
 y = pos.y
 z = pos.z
 
 inside = buildX< x< buildX + width and 
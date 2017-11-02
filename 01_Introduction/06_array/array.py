import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft()

playerPos = mc.player.getPos()

a = [block.JUKEBOX, block.CHEST, block.PISTON]
x = 0
for b in a:
  mc.setBlock(
    playerPos.x + x,
    playerPos.y - 1,
    playerPos.z,
    b)
  x+=1

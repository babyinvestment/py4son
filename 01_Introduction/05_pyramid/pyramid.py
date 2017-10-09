import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft()
playerPos = mc.player.getPos()

height = 20
for y in range(0, height + 1):
  d = height - y
  for z in range(-d, d + 1):
    for x in range(-d, d + 1):
      mc.setBlock(
        playerPos.x + x,
        playerPos.y + y,
        playerPos.z + z,
        block.SANDSTONE)

import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft()
playerPos = mc.player.getPos()

for y in range(0, 10):
  for z in range(0, 10):
    for x in range(0, 10):
      mc.setBlock(
        playerPos.x + x,
        playerPos.y + y + 3,
        playerPos.z + z,
        block.BEACON)

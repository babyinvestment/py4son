import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft()
playerPos = mc.player.getPos()

r = 20
for y in range(-r, r + 1):
  for z in range(-r, r + 1):
    for x in range(-r, r + 1):
      if ((x**2 + z**2) <= r**2):
        mc.setBlock(
          playerPos.x + x,
          playerPos.y + y + r + 3,
          playerPos.z + z,
          block.BEACON)

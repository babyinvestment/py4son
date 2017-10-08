import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft()
playerPos = mc.player.getPos()

for z in range(0, 10):
    for x in range(0, 10):
      mc.setBlock(playerPos.x + x, playerPos.y -1, playerPos.z + z, block.GOLD_BLOCK)

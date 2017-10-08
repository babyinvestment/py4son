import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft()
playerPos = mc.player.getPos()

for z in range(0, 8):
    for x in range(0, 8):
      b = block.OBSIDIAN if (x + z) % 2 == 0 else block.QUARTZ_BLOCK
      mc.setBlock(playerPos.x + x, playerPos.y - 1, playerPos.z + z, b)

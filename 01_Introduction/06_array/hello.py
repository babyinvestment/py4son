import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft()

playerPos = mc.player.getPos()

a = [
    [1,0,1,0,1,1,1,0,1,0,0,0,1,0,0,0,1,1,1],
    [1,0,1,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,1],
    [1,1,1,0,1,1,1,0,1,0,0,0,1,0,0,0,1,0,1],
    [1,0,1,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,1],
    [1,0,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1]
]
t = {
    0: block.GRASS,
    1: block.BEACON
}

z = 0
for row in a:
    x = 0
    for v in row:
        mc.setBlock(playerPos.x + x, playerPos.y - 1, playerPos.z + z, t[v])
        x+=1
    z+=1

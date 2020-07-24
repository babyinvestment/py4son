---
category: py4son
title: ブロック配置 Part 3
date: 2017-09-29 20:30:00
tags:
image: pyramid.png
description: 息子が大好きなMinecraftを使ってプログラミングを教えるため、Raspberry Jam Modを使ってピラミッド状にブロックを配置してみました。
---

息子が大好きなMinecraftを使ってプログラミングを教える。  
第4回目は、前回（[ブロック配置 Part 2](./04_circle)）に続いて、ブロックを三次元に配置するプログラムを息子と一緒に考えることにしました。

キューブ、円柱、球をつくることができたので、今日はピラミッドをつくることにしました。実際のピラミッドは内部に通路がありますが、ここでは、内部もすべてブロックで埋めることにします。

ピラミッドは、底面が正方形で頂点に向かって段が上がるたびに正方形が小さくなっていく<ruby>四角錐<rt>しかくすい</rt>の形ですので、これをプログラミングで表現してみました。

#### プログラム [[pyramid.py](https://github.com/babyinvestment/py4son/blob/master/01_Introduction/05_pyramid/pyramid.py)]

```python
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
```
<br>

#### 実行結果

![pyramid.png](pyramid.png)
<br>

#### 余談

プログラムを実行すると、自分が現在いる場所にピラミッドが建造されますので、実行すると自分自身がピラミッドの中に埋まってしまいます。
その場合、以下のコマンドを使って好きな場所にジャンプするとよいかもしれません。

```shell
/py teleport X座標 Y座標 Z座標
```
<br>

teleport.pyの中身は以下になっています。`mc.player.setTilePos()`関数に、コマンドの引数として渡されたX, Y, Z座標を指定することにより、好きな場所に一瞬で移動できるようですね。
```python
from mine import *
from sys import argv
mc = Minecraft()
mc.player.setTilePos(int(argv[1]), int(argv[2]), int(argv[3]))
```
https://github.com/arpruss/raspberryjammod/blob/master/mcpipy/teleport.py
<br>

なお、MinecraftのcheatsモードをONとしておくと、`/tp`コマンドが使えますが、Raspberry Jam Modで指定する座標の値と`/tp`で指定する座標の値は違いますので気をつけてください。

## 感想

ピラミッドのほかにプログラムで簡単につくれそうな建造物がが思い浮かばなかったので、今日はここまでとします。息子にプログラミングを教えたいという思いが息子にちゃんと伝わっていて、プログラミングを学んでいるのか、ただMinecraftを使って遊んでいるだけなのか、何とも言えません。

息子一人でも同じように書けるのかというとまだ微妙な感じなのですが、少しずつ慣れていってほしいと願っています。

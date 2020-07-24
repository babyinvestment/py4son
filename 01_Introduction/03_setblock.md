---
category: py4son
title: ブロック配置 Part 1
date: 2017-09-23 19:30:32
tags:
image: fourth.png
description: 息子が大好きなMinecraftを使ってプログラミングを教えるため、Raspberry Jam Modを使ってブロックを平面状に配置してみました。
---

息子が大好きなMinecraftを使ってプログラミングを教える。  
第2回目に息子と実施したことについて記載します。

1. メッセージの表示
1. ブロックを一列にならべて配置する
1. ブロックを平面に敷き詰める
1. チェス盤をつくる

## 1. メッセージの表示

前回解説したサンプルプログラム`helloworld.py`を参考に、チャットウィンドウに好きなメッセージを表示するプログラムを作成しました。プログラミングに使用するエディタは何でもよいですが、うちの場合はJavaScriptを教えるときと同じく、[Visual Studio Code](https://code.visualstudio.com/)を使わせています。

mcpipyフォルダに、適当なファイル名をつけて作成しました。(例: first.py)

#### プログラム [[first.py](https://github.com/babyinvestment/py4son/blob/master/01_Introduction/03_setblock/first.py)]
```python
import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft()
mc.postToChat("That's one small step for a man.")
```
<br>

#### 実行結果

![first.py](first.png)
<br>


## 2. ブロックを一列にならべて配置する

サンプル`helloworld.py`はブロックを一つだけ配置するものですが、複数のブロックを配置したい場合、ループ文を使って場所をずらしながらmc.setBlock()を呼び出せばよさそうです。

Pythonではどのようにループ文を書くことができるのか息子に教えて、実際にプログラムを打ち込んでもらいました。

#### プログラム [[second.py](https://github.com/babyinvestment/py4son/blob/master/01_Introduction/03_setblock/second)]

```python
import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft()
playerPos = mc.player.getPos()

for x in range(0, 10):
  mc.setBlock(playerPos.x + x, playerPos.y - 1, playerPos.z, block.BEACON)
```

`for x in range(0, 10)`と書いた場合、xの値が0～9まで10回処理が繰り返されます。

繰り返される処理を書きはじめる位置は、Pythonではfor文よりもインデントを下げて(字下げして)書く必要があるので注意が必要です。
<br>

#### 実行結果

![second.py](second.png)
<br>


## 3. ブロックを平面に敷き詰める

先の例では、x方向にブロックを一列に並べました。線が引けたので、つぎは平面にブロックを敷き詰めてみましょう。
x方向に一列にブロックを並べる処理を、z方向に1つずつずらしながら繰り返すことによって、xとzの二次元方向にブロックを敷き詰めることができます。

#### プログラム [[third.py](https://github.com/babyinvestment/py4son/blob/master/01_Introduction/03_setblock/third.py)]

```python
import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft()
playerPos = mc.player.getPos()

for z in range(0, 10):
  for x in range(0, 10):
    mc.setBlock(playerPos.x + x, playerPos.y - 1, playerPos.z + z, block.GOLD_BLOCK)
```
<br>

for文の繰り返し処理の中にさらにfor文がある二重ループとなります。

#### 実行結果

![third.py](third.png)
<br>
10×10の金ブロック(Gold block)が生成されました。

#### 余談

実は、`mc.setBlocks()`という関数があります。この関数を使用すれば、引数で指定した開始座標から終了座標までを好きなブロックで敷き詰めることができますので、先ほどの重ループで面状にブロックを配置する処理は、以下のように書き換えることはできます。

```python
import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft()
playerPos = mc.player.getPos()

mc.setBlocks(
  playerPos.x,     playerPos.y - 1, playerPos.z,
  playerPos.x + 9, playerPos.y - 1, playerPos.z + 9,
  block.GOLD_BLOCK)
```

これは速くて便利な関数ではありますが、今回は息子に二重ループの考え方について教えることが目的でしたので、あえて二重ループを使う方法で説明しました。
<br>


## 4. チェス盤をつくる

正方形に敷き詰めることができましたので、せっかくですので少し工夫をしてみましょう。サンプルの中に`chess.py`というものがありますが、それはひとまず置いておいて、どのように交互にブロックを配置すればよいか、ということを息子に少し考えてもらうことにしました。

交互になるという特徴から、x座標とy座標を足した値が偶数か奇数か、つまり、2で割ったときのあまり（剰余）が0か1かで判断するということを子供が理解できれば（最下位ビットが0か1かと言ってしまいそうになりますが・・・）、あとはPythonで剰余計算やif文やelse文をどのように書くかの問題になります。

#### プログラム  [[fourth.py](https://github.com/babyinvestment/py4son/blob/master/01_Introduction/03_setblock/fourth.py)]

```python
import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft()
playerPos = mc.player.getPos()

for z in range(0, 8):
    for x in range(0, 8):
      if ((x + z) % 2 == 0):
        mc.setBlock(playerPos.x + x, playerPos.y - 1, playerPos.z + z, block.OBSIDIAN)
      else:
        mc.setBlock(playerPos.x + x, playerPos.y - 1, playerPos.z + z, block.QUARTZ_BLOCK)
```
<br>

`setBlock()`の部分は共通にして、配置するブロックの種類だけを変えるようにするには、以下の書き方でも良さそうです。

```python
import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft()
playerPos = mc.player.getPos()

for z in range(0, 8):
  for x in range(0, 8):
    b = block.OBSIDIAN if (x + z) % 2 == 0 else block.QUARTZ_BLOCK
    mc.setBlock(playerPos.x + x, playerPos.y - 1, playerPos.z + z, b)
```

#### 実行結果

![fourth.png](fourth.png)
<br>

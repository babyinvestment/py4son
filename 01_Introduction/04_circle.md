---
category: py4son
title: ブロック配置 Part 2
date: 2017-09-28 19:30:32
tags:
image: sphere.png
description: 息子が大好きなMinecraftを使ってプログラミングを教えるため、Raspberry Jam Modを使ってブロックを立方体や球状に配置してみました。
---

息子が大好きなMinecraftを使ってプログラミングを教える。  
第3回目に息子と実施したことを記載します。
1. キューブを描く
1. 円を描く
1. 円柱を描く
1. 球を描く

## 1. キューブを描く

これまで線や面を描く方法を息子に教えてきましたが、Minecraftの世界というのは2次元ではなく3次元です。
そこで今日は、三次元の中で最も基本的な形であるキューブ（立方体）をどうやって描けるかについて、息子に教えることにしました。

前回（[ブロック配置 Part 1](./03_setblock)）、x方向に並んだ線をz方向に繰り返し配置していくことで、面が描けることを教えましたので、この面をy方向に繰り返し描いて、x,y,zの長さを同じにすればキューブ（立方体）になることが理解できれば、プログラムのイメージが沸くかと思います。

#### プログラム [[cube.py](https://github.com/babyinvestment/py4son/blob/master/01_Introduction/04_circle/cube.py)]

```python
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
```
<br>

for文の中にfor文があってさらにその中にfor文がある。マトリョーシカみたいな三重ループですね。自分自身がブロックの中に埋もれてしまわないようy方向に+3程度加えておくことにしました。

#### 実行結果

![cube.png](cube.png)
<br>


## 2. 円を描く

再び2次元に戻って、平面上にブロックを敷き詰めることを考えてみましょう。
前回の記事（[ブロック配置 Part 1](https://www.babyinvestment.com/py4son/03_setblock)）では、平面状にブロックを敷き詰めてチェス盤をつくってみたので、今回は円状にどのように配置するか、息子に教えてみようと試みました。

円を描く方法はいくつか考えられますが、チェス盤を描いたときの考え方をもとに、三平方の定理（ピタゴラスの定理）を用いる方法で教えることにしました。

直角三角形の辺a, b, cがあるとき、a<sup>2</sup> + b<sup>2</sup> = c<sup>2</sup>の関係があることが理解できれば、平面上にブロックを配置していく際に、自分の位置から半径cの内側となるときだけに限定してsetBlock()を呼ぶことで、中を塗りつぶした円が描けることが分かれば、もうプログラムが書けたようなものです。

まだ学校で習っていないとは思いますが、別に習っていないから使ってはいけないというわけではないですし、習えば使えるようになるのか、使っていくうちに理解が追いつくのか、どちらでも良いと考えています。大切なのは、何かを実現したいときに、習ってないからできないとあきらめるのではなく色々と工夫してやり遂げていくことです。

#### プログラム [[circle.py](https://github.com/babyinvestment/py4son/blob/master/01_Introduction/04_circle/circle.py)]

```python
import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft()
playerPos = mc.player.getPos()

r = 20
for z in range(-r, r + 1):
  for x in range(-r, r + 1):
    if ((x**2 + z**2) <= r**2):
      mc.setBlock(
        playerPos.x + x,
        playerPos.y-1,
        playerPos.z + z,
        block.BEACON)
```
<br>

#### 実行結果

![circle.png](circle.png)
<br>

## 3. 円柱を描く

今日はまずキューブを描きました。そして、その次に平面に円を描きました。それでは、この円をキューブをつくったときのようにy方向に繰り返し配置していくことにより円柱ができるのではないか、ということを息子と話しました。

『できるだろう』という予想に対して、本当にできるかどうかプログラムを組んで試してみるという習慣をぜひ身につけてほしいと願っています。
<br>

#### プログラム [[cylinder.py](https://github.com/babyinvestment/py4son/blob/master/01_Introduction/04_circle/cylinder.py)]

```python
import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft()
playerPos = mc.player.getPos()

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
```
<br>

自分を中心にして円柱を描く際、xとzと同様にy方向も自分を中心としてしまうと円柱の中に閉じ込められてしまうため、yの表示位置にオフセットを加えます。yのfor文で指定しているrange()の値を変更する方法でもよいですが、x,y,zのループ範囲を-r～r+1と統一したかったので、setBlock時に、r + 3のオフセットを設定しました。(yの取りうる最小値のときにプレーヤーの頭上+3となるように値を決めました）

#### 実行結果

![cylinder.png](cylinder.png)
<br>

## 4. 球を描く

今日、息子に描かせたいと考えていたのは球でしたので、まずは平面に円を描いて、キューブのように縦方向に重ねて円柱を描くという順序で教えました。円柱が描けたので、次に球を描いてみることにしました。

球の表面は、中心からの距離がみな同じ長さにある点が集まったもの』であるということを説明し、円柱を描く処理の中で、ブロックを配置する場所が球の外側か内側かなのかを判定して、内側のときだけブロックを配置すれば球ができることを教えました。

球の外側か内側かを判定する方法ですが、中心からの距離rとx,y,zには以下の関係があります。

x<sup>2</sup> + y<sup>2</sup> + z<sup>2</sup> = r<sup>2</sup>

いつか学校で習うかと思いますので詳しくは説明しませんでしたが、先ほどの円柱のブロック配置条件を少し変えるだけで球を描くことができました。

- 円柱（変更前）
```python
      if ((x**2 + z**2) <= r**2):
```

- 球（変更後）
```python
      if ((x**2 + y**2 + z**2) <= r**2):
```
<br>

#### プログラム [[sphere.py](https://github.com/babyinvestment/py4son/blob/master/01_Introduction/04_circle/sphere.py)]

```python
import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft()
playerPos = mc.player.getPos()

r = 20
for y in range(-r, r + 1):
  for z in range(-r, r + 1):
    for x in range(-r, r + 1):
      if ((x**2 + y**2 + z**2) <= r**2):
        mc.setBlock(
          playerPos.x + x,
          playerPos.y + y + r + 3,
          playerPos.z + z,
          block.BEACON)
```

#### 実行結果

![sphere.png](sphere.png)
<br>

小学生の息子にどの程度、自分の教えていることをちゃんと理解できているのか正直な話疑問です。ですが、それでもとにかくこうして一緒に試みているのは、コンピュータを使い算数の知識を活かせば、いろんなことがとても簡単にできてしまう、そんな素晴らしい『魔法の世界』をもっと感じてほしいからです。

## 感想

色々な種類のブロックを一つずつ配置して街や村をつくっていた息子にとって、数行のプログラムで球が描けたり、サンプルプログラムにあるように画像ファイルを読み込んでブロックで再現するようなものは新鮮なようです。

ですが、その一方で自分が少しずつ感じてはじめているのは、息子にプログラムやアルゴリズムばかり教えて、今まで楽しんでいた『街づくり』をしなくなってしまったら、効率性と引き換えに大切な何かを失ってしまうような、何ともいえない惜しい気持ちです。

これからも『街づくり』を続けてたくさんの世界を想像してほしいですし、プログラムはあくまで便利なツールとして、必要に応じて使える程度で十分ではないかと思うようになりました。私のようにプログラムは組めるけどセンスや想像力がイマイチ、というようにはあまりなってほしくはないですね。

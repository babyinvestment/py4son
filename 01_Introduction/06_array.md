---
category: py4son
title: ブロック配置 Part 4
date: 2017-10-03 23:30:00
tags:
image: hello.png
description: 息子が大好きなMinecraftを使ってプログラミングを教えるため、Raspberry Jam Modを使って配列を教えました。
---

息子が大好きなMinecraftを使ってプログラミングを教える。  
第5回目は、配列を使って好きなブロックを配置することを考えます。[前回](./05_pyramid)まで、同じブロックを規則的に並べたり、パターン（計算）に基づいて配置するブロックを変えたりしましたが、自分の好きなようにブロックをまとめて置きたいものです。

Raspberry Jam Modを使う場合、setBlock()でブロックを配置できますので、配置したいブロック数の数だけ、setBlock()文を記述すれば好きなブロックを配置することはできます。しかし、配置したブロックが10個、20個、100個と増えた場合に、その数分setBlock()を書きたくないものです。

『もっと分かりやすくスマートに、シンプルにプログラムを書けないか』

これはプログラミングを学ぶ上でとても大切な姿勢です。  
繰り返すときに何が変わるのかという点に着目すると、配置する場所と、配置するブロックの種類は変わりますが、setBlock()文を呼び出すこと自体は変わりません。そこで、for文を使ったループを考えて、ループのたびに配置する場所を1つずつ増やしていくことにして、配置するブロックの種類はあらかじめ配列として定義しておき、その要素を順に参照して配置していくという方法を考えたいと思います。

今日は、以下の2つを息子と一緒に試してみたいと思います。

- 配列を使ってブロックを一列に並べる (1次元配列)
- 配列を使ってブロックを平面に並べる (2次元配列)


## 1. 配列を使ってブロックを一列に並べる (1次元配列)

### Pythonにおける配列（リスト）

配列を使うにあたって、Pythonでどのように記述するのかについて知っておく必要があります。これまで自分は、BASIC、x86アセンブラ、C/C++、Java、C#、bash、JavaScript・・・とコンピュータ言を学んできましたが、Pythonはまだビギナーでしたので、息子に教えながら慣れていこうと考えることにしました。

[公式サイト](https://www.python.org/)のドキュメントを読むと、Pythonでは配列をリストと呼ぶようです。息子に配列を説明するために、以下を書いて実行してみました。

```python
days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
for day in days:
  print(day)
```

```shell
Sun
Mon
Tue
Wed
Thu
Fri
Sat
```

#### プログラム [[array.py](https://github.com/babyinvestment/py4son/blob/master/01_Introduction/06_array/array.py)]

配列（リスト）の使い方が分かったので、置きたいブロックを配列（リスト）に定義して、順に配置していくことにしました。

```python
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
```

変数bには、配列（リスト）から取り出したブロックの種類が順に取り出されます。

#### 補足

上の例では、ループのたびに配置する場所を変更するために、変数xを用意して自分で数えましたが、ほかにいくつかの記述方法が考えられます。

##### (a) 配列要素番号を使う

```python
for i in range(len(a)):
  mc.setBlock(
    playerPos.x + i,
    playerPos.y - 1,
    playerPos.z,
    a[i])
```

変数`i`には、配列（リスト）の何番目かという値が入りますので、その数値をもとに、`a[i]`で要素を取り出します。

##### (b) enumerateを使う

```python
for i,b in enumerate(a):
  mc.setBlock(
    playerPos.x + i,
    playerPos.y - 1,
    playerPos.z,
    b)
```

`enumerate`を使うと、変数`i`には配列（リスト）要素番号、変数`b`には値が順に入ります。

#### 実行結果

![array.png](array.png)
<br>

## 2. 配列を使ってブロックを平面に並べる (2次元配列)

先ほどの例では横一列にブロックを並べただけでしたが、2次元の平面上に並べるにはどうしたらよいでしょうか。

配列（リスト）の中に配列（リスト）を入れるとよいでしょう。イメージとしては以下になります。

```python
a = [
  [block.BEACON, block.SANDBLOCK],
  [block.BEACON, block.SANDBLOCK],
  [block.BEACON, block.SANDBLOCK]
]
```

でも、1つ1つどのブロックを配置するか種類を記述するのは大変ですね。そこで、0だったら～,1だったら～という対応表を一つ用意して配置してみましょう。

#### プログラム [[hello.py](https://github.com/babyinvestment/py4son/blob/master/01_Introduction/06_array/hello.py)]

```python
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
```

#### 実行結果

![hello.png](hello.png)
<br>

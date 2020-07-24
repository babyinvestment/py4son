---
category: py4son
title: Raspberry Jam Mod
date: 2017-09-22 06:30:32
tags:
image: earth.png
description: 息子が大好きなMinecraftを使ってプログラミングを教えるため、Minecraft Java EditionにRaspberry Jam Modを導入してサンプルプログラムを実行してみました。
---

教育用のコンピュータとして発売されている[Raspberry Pi](https://www.raspberrypi.org/)向けに[Minecraft Pi Edition](https://minecraft.net/en-us/edition/pi/)というプログラミングができるMinecraftがありますが、WindowsやMac向けのJava Editionでも同じようにプログラミングできるよう機能追加するのが、Minecraft Jam Modです。

うちの場合は、すでにMinecraft Java Editionを持っていて息子が遊び慣れていることもありますので、Raspberry Jam Modを導入することにしました。

環境の準備は以下の流れで行いました。
1. Minecraft Forgeの導入
1. Raspberry Jam Modの導入
1. Phytonの導入
1. サンプルの実行

1～3については、色々なWebページで紹介されているので簡単に記載します。

## 1. Minecraft Forgeの導入

Raspberry Jam Modを動かすには、Minecraft Forgeが必要になります。  
以下のサイトからダウンロードできました。
- https://files.minecraftforge.net/

使用するPCに合わせて、Windows または Mac向けのMinecraftのバージョンに合ったモジュールをダウンロードしてください。

インストールした後、一度Minecraftを起動して初期設定が済んだ状態にしておく必要があるようです。

## 2. Raspberry Jam Modのインストール

Raspberry Jam Modは、以下のサイトからダウンロードできました。

- https://github.com/arpruss/raspberryjammod/releases

ダウンロードしたmods.zipの中から、環境に合ったバージョンのRaspberryJamMod.jarを、modsフォルダに格納しました。

標準的なminecraftのフォルダは以下になります。Minecraft Forgeのインストール先を変えている場合はそのディレクトリの下のmodsフォルダに格納するとよいでしょう。

- Windowsの場合
```shell
C:\Users\<ユーザ名>\AppData\Roaming\.minecraft
```

- Macの場合
```shell
/Users/<ユーザ名>/Library/Application Support/minecraft
```

また、Python-scripts.zipを解凍して作成されるmcpipyフォルダを、modsフォルダと同じ階層になるように格納しました。

## 3. Pythonの導入

Raspberry Jam Modを使ってプログラムを実行するには、Pythonが必要ですので、使用している環境にPythonが導入されていなければ、インストールが必要です。
- https://www.python.org/

Python 2.x系とPython 3.x系がありますが、Raspberry Jam Modはどちらでも動作するということですので、これから学ぶのであれば、Python 3.x系を使えばよいと思います。

### 補足

息子のMacで試してみたところ、OS XにはPython 2.x系があらかじめ入っているようで、Python 3をインストールしたにも関わらず、Python 2.x系で動作してしまっていました。

この場合、以下の設定ファイルを修正する等の方法により解決できる可能性があります。

```shell
/Users/<ユーザ名>/Library/Application Support/minecraft/config/raspberryjammod.cfg
```

- 修正箇所
```shell
S:"Python Interpreter"=python
```

- フルパスで指定した例
```shell
S:"Python Interpreter"=/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
```

## 4. サンプルの実行

python-scripts.zipを解凍してできたmcpipyフォルダには、数多くのサンプルのプログラムが格納されています。以下に公開されています。
- https://github.com/arpruss/raspberryjammod/tree/master/mcpipy

サンプルは以下のいずれかの方法で実行することができます。
- Minecraftのチャットウィンドウで `/py <Pythonファイル名から拡張子を除いたもの)` を入力
- OSのコマンドラインから `python <Pythonファイル名>` を実行

### helloworld.py

プログラミングを学ぶときに一番最初に実行するのが `Hello, world` と表示するプログラムであるように、まず、このサンプルを実行してみましょう。  
```shell
/py helloworld
```

#### 実行結果
![Helloworld.py](helloworld.png)

チャットウィンドウに`Hello World!`と表示されます。
また、プレーヤーの足元にダイヤモンド鉱石(Diamond Ore)が配置されます。
<br>

#### プログラム

```python
import mcpi.minecraft as minecraft
import mcpi.block as block
import server
import sys
mc = minecraft.Minecraft()
mc.postToChat("Hello world!")
playerPos = mc.player.getPos()
mc.setBlock(playerPos.x,playerPos.y-1,playerPos.z,block.DIAMOND_ORE)
```
https://github.com/arpruss/raspberryjammod/blob/master/mcpipy/helloworld.py

#### プログラムの解説

たった8行のプログラムとはいえ、見慣れない命令文ばかりだと思いますので、一つ一つ息子に説明することにしました。
<br>

##### (1) import文

```python
import mcpi.minecraft as minecraft
import mcpi.block as block
import server
import sys
```
Raspberry Jam ModやMinecraft Pi Editionと通信を行うモジュールを使用するためのおまじないで、同名のPythonプログラムが存在しています。
- mcpi/minecraft.py
- mcpi/block.py
- server.py
これらのファイルの中身について今は分からなくても気にすることはありません。

sysはPythonの標準モジュールです。このサンプルでは使われていないように見えますので、この行が無くても問題ないかもしれません。
<br>

##### (2) Minecraftオブジェクト

```python
mc = minecraft.Minecraft()
```
Minecraftと通信を行うためのオブジェクトを作成して、mcという変数に入れておきます。これ以降、変数mcを用いてメッセージを投げたり、ブロックを配置したりします。
<br>

##### (3) メッセージ送信

```python
mc.postToChat("Hello world!")
```

チャットウィンドウに`Hello world!`と表示します。ダブルクォート(`"`)またはシングルクォート(`'`)でくくった中に文字列を指定することができます。

息子には、いくつか表示したい文字列に置き換えて実行させてみることにしました。
<br>

##### (4) プレーヤーの座標取得

```python
playerPos = mc.player.getPos()
```

プレーヤーがMinecraft世界のどの場所にいるのかを知ることができます。変数playerPosがどんなものかは、次の命令文を見ると分かりますが、以下の値が整数で入っているようです。
- playerPos.x: プレーヤーのx座標
- playerPos.y: プレーヤーのy座標
- playerPos.z: プレーヤーのz座標
<br>

##### (5) ブロックの配置

```python
mc.setBlock(playerPos.x,playerPos.y-1,playerPos.z,block.DIAMOND_ORE)
```

ブロックを配置します。長いので一見すると難しく感じてしまうかもしれませんが、よく見ると難しくありません。

以下の通り、プレーヤーの座標からy方向(縦方向)だけ1少ない場所、つまに足元にダイヤモンド鉱石(Diamond Ore)を配置していることが分かります。

```python
mc.setBlock(X座標, Y座標, Z座標, ブロックの種類)
```

|引数  |値|
|:-----|:------|
|X座標|playerPos.x|
|Y座標|playerPos.y - 1|
|Z座標|playerPos.z|
|ブロックの種類|block.DIAMOND_ORE|


ダイアモンド鉱石以外のブロックを配置してみたいと思うはずです。ほかにどんなブロックを指定できるのでしょうか。
setBlockの4つ目の引数に、以下のように記載されているので、どうやら変数blockにヒミツがありそうです。

```python
block.DIAMOND_ORE
```

mcpi/block.pyファイルを見ると、内容は理解できなくても、たくさんのブロックの名前が記載されていることが分かります。

ここを参考に、息子にも好きなブロックを配置してもらうようにプログラムを変更して実行させてみました。たとえば、以下のようにすることで、ビーコンが配置されることが分かりました。

```python
block.BEACON
```
<br>

#### earth.py

次にearth.pyというサンプル実行してみました。

```shell
/py earth
```
<br>

#### 実行結果

![earth.py](earth.png)
少し時間がかかりますが、Minecraftのワールド内に大きな地球がつくられました。
<br>

#### プログラム

```python
#
# Code by Alexander Pruss and under the MIT license
#
# Needs Pillow
#

#
# earth.py [size [filename]]
#

from mine import *
import os.path,sys
from PIL import Image
from pysanka import egg, getPixel

mc = Minecraft()
pos = mc.player.getTilePos()

height = 100
filename = None

if len(sys.argv) > 1:
    height = int(sys.argv[1])
    if len(sys.argv) > 2:
        filename = sys.argv[2]
        if not os.path.isfile(filename):
            filename = os.path.dirname(os.path.realpath(sys.argv[0])) + "/" + filename    

if filename is None:
    filename = os.path.dirname(os.path.realpath(sys.argv[0])) + "/" + "nasaearth.jpg"
    
    
image = Image.open(filename).convert('RGB')

for (x,y,z,block,theta) in egg(h=height,block=None,sphere=True):
    mc.setBlock(x+pos.x,y+pos.y,z+pos.z,getPixel(image, (theta / (2*pi)) % 1, y / float(height), dither=10))

```
<br>

#### プログラムの解説

中のプログラムについての説明は、息子にはまだ難しいことと、自分も詳しく見ていませんので簡単に説明します。
<br>

##### (1) import文
```python
from mine import *
import os.path,sys
from PIL import Image
from pysanka import egg, getPixel
```

Python Image Libraryという画像処理を行うモジュールが使われています。earth.pyの実行には、このライブラリがインストールされている必要があります。  
プログラムが実行エラーとなった場合は、Pythonのパッケージ管理システム『pip』などを使って、piライブラリをインストールしてください。(`例) pip install pillow`)

また、mcpipyフォルダにpysanka.pyというPythonプログラムがあって、その中のegg, getPixelという関数が使われていて球状にブロックを配置しているようです。
<br>

##### (2) コマンド引数
```python
height = 100
filename = None

if len(sys.argv) > 1:
    height = int(sys.argv[1])
    if len(sys.argv) > 2:
        filename = sys.argv[2]
        if not os.path.isfile(filename):
            filename = os.path.dirname(os.path.realpath(sys.argv[0])) + "/" + filename    

if filename is None:
    filename = os.path.dirname(os.path.realpath(sys.argv[0])) + "/" + "nasaearth.jpg"
```

この処理を見ると、以下のコマンドの引数を指定することができるようです。
- サイズを指定する場合
```shell
/py earth サイズ
```
- サイズとマッピングする画像ファイルを指定する場合
```shell
/py earth サイズ 画像ファイル名
```

引数を指定しなかった場合、サイズは100、球にマッピングする画像ファイル名は nasaearth.jpg となります。
<br>

##### (3) ブロック配置

```python
image = Image.open(filename).convert('RGB')

for (x,y,z,block,theta) in egg(h=height,block=None,sphere=True):
    mc.setBlock(x+pos.x,y+pos.y,z+pos.z,getPixel(image, (theta / (2*pi)) % 1, y / float(height), dither=10))
```

ブロックを配置する処理になります。ブロックを配置する場所はegg()関数内で計算しています。また、getPixel()関数では配置すべきブロックを画像データから取得しているようです。

getPixel()関数に渡す引数は角度thetaなどを使って計算しているようですが、ここでは詳細について気にしないことにしましょう。

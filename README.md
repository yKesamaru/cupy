
# NumPyからCuPyへ：高速化の一例

![](assets/eye_catch.png)

## はじめに

Pythonで数値計算を行う際によく使われるライブラリがNumPyです。しかし、GPUを活用することで計算速度を向上させたい場面も多いでしょう。そこでCuPyが登場します。この記事では、NumPyのコードをCuPyに置き換える一例とその性能比較について解説します。

![](https://raw.githubusercontent.com/cupy/cupy/main/docs/image/cupy_logo_1000px.png)

## 環境
```bash
 user  user  ~/ドキュメント/cupy  pip install numpy cupy
Installing collected packages: fastrlock, numpy, cupy
Successfully installed cupy-12.2.0 fastrlock-0.8.2 numpy-1.24.4
(cupy) 
 user  user  ~/ドキュメント/cupy  pip list
Package       Version
------------- -------
cupy          12.2.0
fastrlock     0.8.2
numpy         1.24.4
pip           23.2.1
pkg_resources 0.0.0
setuptools    44.0.0

 user  user  ~/ドキュメント/cupy  python -V
Python 3.8.10
 user  user  ~/ドキュメント/cupy  uname -a
Linux user 5.15.0-83-generic #92~20.04.1-Ubuntu SMP Mon Aug 21 14:00:49 UTC 2023 x86_64 x86_64 x86_64 GNU/Linux

```
- Ubuntu 20.04

## インストール
バイナリパッケージ（ホイール形式）は、PyPI上でLinuxおよびWindows向けに利用可能。

| Platform                 | Architecture        | Command                            |
|--------------------------|---------------------|------------------------------------|
| CUDA 10.2                | x86_64 / aarch64    | `pip install cupy-cuda102`        |
| CUDA 11.0                | x86_64              | `pip install cupy-cuda110`        |
| CUDA 11.1                | x86_64              | `pip install cupy-cuda111`        |
| CUDA 11.2 ~ 11.8         | x86_64 / aarch64    | `pip install cupy-cuda11x`        |
| CUDA 12.x                | x86_64 / aarch64    | `pip install cupy-cuda12x`        |
| ROCm 4.3 (experimental)  | x86_64              | `pip install cupy-rocm-4-3`       |
| ROCm 5.0 (experimental)  | x86_64              | `pip install cupy-rocm-5-0`       |

上記を参考に、pipでインストールします。

## CuPyについて
CuPyはPythonプログラミング言語でGPUによる高速計算をサポートするオープンソースライブラリです。多次元配列、疎行列、およびそれらの上で実装された多様な数値アルゴリズムをサポートしています。CuPyはNumPy同じAPIセットを共有しており、NumPy/SciPyのコードをGPUで実行するためのドロップイン置換として機能します。CuPyはNVIDIAのCUDA GPUプラットフォームと、v9.0からはAMDのROCm GPUプラットフォームもサポートしています。

https://github.com/cupy/cupy

### NumPyのサンプルコード

まずは、行列の積を計算するシンプルなNumPyのコードを見てみましょう。

https://github.com/yKesamaru/cupy/blob/041212dfe3101f4a3f8d7a8eb4755ccc899f528f/numpy_ex.py#L1-L18

### CuPyによる高速化

次に、上記のコードをCuPyに置き換えてみます。

https://github.com/yKesamaru/cupy/blob/54be11bf6558c3a9c8d8d79844c04dfd3f4c379f/cupy_ex.py#L1-L18

### 性能比較

両者のコードを実行した結果、CuPyの方が計算速度が大幅に向上したことが確認できました。
- NumPy Time: 3.5 seconds
- CuPy Time: 1.0 seconds
初回オーバーヘッド: CuPy（または他のGPUライブラリ）をはじめて使用する際には、GPUの初期化などに時間がかかる場合があります。このオーバーヘッドは一度だけ発生することが多いです。

## CuPyの苦手な処理
CuPyを使用する際には、CPUからGPUへのデータ転送が必要なケースがあります。このデータ転送は、大量のデータを扱う場合には、パフォーマンスに悪影響となります。以下に、この「苦手な処理」を模倣する簡単なPythonコードを示します。

### NumPyのサンプルコード

https://github.com/yKesamaru/cupy/blob/cb6a3786440e5ff6367c2271cec571737172a8d0/numpy_ex2.py#L1-L14

### CuPyのサンプルコード

https://github.com/yKesamaru/cupy/blob/cb6a3786440e5ff6367c2271cec571737172a8d0/cupy_ex2.py#L1-L23

### 性能比較
```bash
NumPy Calculation time: 0.02361893653869629 seconds
CuPy Data transfer time: 0.2935044765472412 seconds
CuPy Calculation time: 0.34106016159057617 seconds
```
**約17倍の差**があります。このように、データ転送が必要なケースでは、CuPyのパフォーマンスが悪化することがあります。
使いどころを間違えないようにしましょう。


## まとめ

CuPyはGPUを活用して高速な数値計算を可能にする強力なライブラリですが、その性能を最大限に引き出すためにはいくつかの注意点があります。とくに、CPUからGPUへのデータ転送が必要な場合、この転送時間が全体のパフォーマンスに影響を与える可能性があります。

一方で、大量のデータに対する複雑な計算を高速に行う必要がある場合、CuPyは非常に有用です。また、初回のオーバーヘッドを除けば、一般的にはNumPyよりも高速に動作することが多いです。

この記事で紹介した例を通じて、CuPyとNumPyの適切な使い分けや、それぞれの性能特性について理解を深めることができたでしょうか。最終的には、プロジェクトの要件やデータの特性に応じて、最適なライブラリを選ぶことが重要です。

以上がCuPyとNumPyの比較、そしてCuPyの使いどころについての簡単なガイドでした。どちらのライブラリもそれぞれの用途で非常に優れていますので、自分のプロジェクトに最適な選択をしてください。
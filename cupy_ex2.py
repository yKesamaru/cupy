import time

import numpy as np

import cupy as cp

# NumPyで大量のデータを生成
n_elements = 10**7  # 要素数
numpy_array = np.random.rand(n_elements)

# CPUからGPUへのデータ転送（これが苦手な処理）
start_time_transfer = time.time()  # 転送タイム計測開始
cupy_array = cp.asarray(numpy_array)  # CPUからGPUへ転送
end_time_transfer = time.time()  # 転送タイム計測終了

print(f"CuPy Data transfer time: {end_time_transfer - start_time_transfer} seconds")  # 転送にかかった時間を表示

# 何らかのGPU処理（例：要素ごとの平方根の計算）
start_time_calc = time.time()  # 計算タイム計測開始
result_cupy = cp.sqrt(cupy_array)
end_time_calc = time.time()  # 計算タイム計測終了

print(f"CuPy Calculation time: {end_time_calc - start_time_calc} seconds")  # 計算にかかった時間を表示

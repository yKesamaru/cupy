import time

import numpy as np

# NumPyで大量のデータを生成
n_elements = 10**7  # 要素数
numpy_array = np.random.rand(n_elements)

# 何らかのCPU処理（例：要素ごとの平方根の計算）
start_time_calc = time.time()  # 計算タイム計測開始
result_numpy = np.sqrt(numpy_array)
end_time_calc = time.time()  # 計算タイム計測終了

print(f"NumPy Calculation time: {end_time_calc - start_time_calc} seconds")  # 計算にかかった時間を表示

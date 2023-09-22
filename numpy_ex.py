import time

import numpy as np

# タイム計測開始
start_time = time.time()

# 行列生成
a = np.random.rand(5000, 5000)
b = np.random.rand(5000, 5000)

# 行列の積
result = np.dot(a, b)

# タイム計測終了
end_time = time.time()

print(f"NumPy Time: {end_time - start_time} seconds")

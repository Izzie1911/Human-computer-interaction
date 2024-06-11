import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO



# Đọc dữ liệu vào DataFrame
df = pd.read_csv("output.csv")
print(df.columns)
print(df["Time"])
df['Time'] = pd.to_datetime(df['Time'], unit='ns')

# Vẽ biểu đồ
plt.figure(figsize=(10, 6))
plt.plot(df['Time'], df['leRatio'], label='leRatio')
plt.plot(df['Time'], df['reRatio'], label='reRatio')
plt.plot(df['Time'], df['Ratio'], label='Ratio')
plt.xlabel('Time')
plt.ylabel('Values')
plt.title('Plot of leRatio, reRatio, and Ratio over Time')
plt.legend()
plt.grid(True)
plt.show()
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.stats import linregress

# Đọc dữ liệu (đảm bảo đường dẫn đúng với tệp của bạn)
df = pd.read_csv('epa-sea-level.csv')

# Loại bỏ các dòng có giá trị NaN trong cột 'Year' và 'CSIRO Adjusted Sea Level'
df = df.dropna(subset=['Year', 'CSIRO Adjusted Sea Level'])

# Vẽ đồ thị
def draw_plot():
    plt.figure(figsize=(10, 6))

    # Vẽ dữ liệu
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Data', color='blue')

    # Vẽ đường hồi quy đầu tiên (dữ liệu từ năm 1880 đến hiện tại)
    slope1, intercept1, r_value1, p_value1, std_err1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended1 = np.arange(1880, 2051)
    plt.plot(years_extended1, slope1 * years_extended1 + intercept1, label='Best Fit Line (1880)', color='red')

    # Vẽ đường hồi quy thứ hai (dữ liệu từ năm 2000 đến hiện tại)
    df_recent = df[df['Year'] >= 2000]
    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_extended2 = np.arange(2000, 2051)
    plt.plot(years_extended2, slope2 * years_extended2 + intercept2, label='Best Fit Line (2000)', color='green')

    # Thêm nhãn và tiêu đề
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Sea Level Rise Over Time')

    # Cập nhật các nhãn trục x
    plt.xticks(np.arange(1850, 2100, step=25))

    # Thêm legend
    plt.legend()

# Gọi hàm vẽ đồ thị
draw_plot()

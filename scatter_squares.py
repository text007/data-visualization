import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

# 传递 x,y 坐标，c 线条颜色，edgecolor 线条轮廓，s 线条的尺寸
plt.scatter(x_values, y_values, c = y_values, cmap = plt.cm.Blues, edgecolor='none', s = 400)

# 设置图表标题给坐标轴加标签
plt.title('Squares Numbers', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Square of Value', fontsize=14)

# 设置刻度标记大小
plt.tick_params(axis='both', which='major', labelsize=14)

# 设置每个坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])

# plt.show()  # 打开查看器显示图形
plt.savefig('squares_plot.png', boox_inches = 'tight') # 保存图片

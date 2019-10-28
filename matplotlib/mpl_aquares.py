import matplotlib.pyplot as plt # 导入模块

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25] # 创建列表
plt.plot(input_values, squares, linewidth=5) #将列表传递个plot函数，并线条粗细

# 设置图表标题，并给坐标轴加上标签
plt.title('Squares Numbers', fontsize=24) # 指定主标题，并设置字体大小
plt.xlabel('Value', fontsize=14)    # 指定轴标题，并设置字体大小
plt.ylabel('Square of Value', fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)  # 设置参数axis值为both，代表要设置横纵的刻度标记，标记大小为14

plt.show()  # 打开查看器显示图形

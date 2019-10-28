import pygal

from die import Die

# 创建一个d6
die_1 = Die()
die_2 = Die(10)

# 抛几次骰子，并将结果存储在一个列表中
results = []
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# 分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)    # count() 方法用于统计列表里某个元素出现的次数
    frequencies.append(frequency)

# print(frequencies)

# 对结果进行可视化
hist = pygal.Bar()

hist.title = 'Results of rolling a D6 and a D10 50000 times'  # 标题
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']  # x 轴坐标
hist.x_title = 'Result' # x轴标题
hist.y_title = 'Frequency of Result'    # y 轴标题

hist.add('D6 + D10', frequencies)    # 传递图表标签，数据
hist.render_to_file('die_visual.svg')   # 保存成.xvg文件

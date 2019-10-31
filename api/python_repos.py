import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# 执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print('Status code:', r.status_code)

# 将API响应存储在一个变量中
response_dict = r.json()

# 处理结果
print('Total repositories:', response_dict['total_count'])

# 探索有关仓库的信息
repo_dicts = response_dict['items']
# print('Repositories returned:', len(repo_dicts))



# 研究第一个仓库
# repo_dict = repo_dicts[0]
# print('\nkeys:', len(repo_dict))
# for key in sorted(repo_dict.keys()):
#     print(key)

names, plot_dicts = [], []
# print('\nSelected information about each repository:')
for repo_dict in repo_dicts:
    # print('Name:', repo_dict['name'])
    # print('Owner:', repo_dict['owner']['login'])
    # print('Stars:', repo_dict['stargazers_count'])
    # print('Repository:', repo_dict['html_url'])
    # print('Created:', repo_dict['created_at'])
    # print('Updated:', repo_dict['updated_at'])
    # print('Description:', repo_dict['description'])

    names.append(repo_dict['name'])
    

    plot_dict = {
        'value':repo_dict['stargazers_count'], # 星数
        'label':repo_dict['description'],   # 项目描述
        'xlink':repo_dict['html_url'], # 给对应的条形图赋予对应的连接
    }
    plot_dicts.append(plot_dict)

# 可视化
my_style = LS('#333366', base_style=LCS)

my_config = pygal.Config()  # Config() 定制图表的外观
my_config.x_label_rotation = 45 # 设置让标签绕x轴旋转45度
my_config.show_legend = False   # 隐藏图例
my_config.title_font_size = 24  # 图表标题大小
my_config.label_font_size = 14  # 图表副标为题x轴标题的大小
my_config.major_label_font_size = 18    # 主标签大小
my_config.truncate_label = 15   # 项目名缩短到15个字符
my_config.show_y_guides = False # 隐藏图表水平线
my_config.width = 1000  # 设置图表宽度

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python Projects on Github'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('pyrhon_repos.svg')

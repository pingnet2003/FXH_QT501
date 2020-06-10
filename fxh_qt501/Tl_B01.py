# pip install echarts-countries-pypkg
# pip install echarts-china-provinces-pypkg
# pip install echarts-china-cities-pypkg
# pip install echarts-china-counties-pypkg
# pip install echarts-china-misc-pypkg

from pyecharts import Map    #pip install pyecharts==0.5.10  pip3 install pyecharts-snapshot
import math

# data
province_distribution = {'河南': 10,'广东': 9,'福建': 8,'浙江': 7,'江苏': 6}
# 隐私数据，不作展示
provice = list(province_distribution.keys())
values = list(province_distribution.values())
for i in range(len(values)):
    values[i]=math.floor(values[i])
# map 函数 地图主要用于地理区域数据的可视化
map = Map("中国地图", '中国地图2', width=1200, height=600)
map.add("", provice, values, visual_range=[0, 10], maptype='china', is_visualmap=True,is_label_show=True,
        visual_text_color='#000')
# is_label_show=True用于显示省份标注
# 图表输出  通过render()函数输出为html文件
map.render(path="中国地图.html")

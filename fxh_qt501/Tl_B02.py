import numpy as np                     # pip3 install numpy
import matplotlib.pyplot as plt        # pip3 install matplotlib
import os
'''
统计的数据来源：来自4个文件,分别对应4个部位。
   其中格式如下：序号、库存时间、Etag、LotNo、部位、Size、入库时间、入库数量、出库时间、出库数量、Ticketid、库别、生产线、单据号
Function: 测算出每个文件的“平均库存时间”,以 柱状图 方式 显示
'''

data_path=r'E:\\vscode_2020\\vstestfxh\\fxh_qt501\\fxh_qt501\\source_file\\lfpis'
data_filenames=['midsole.csv','ms.csv','OUTSOLE.csv','ph.csv']

#结果输出参数设定
output_path='./output'
if not os.path.exists(output_path):
    os.makedirs(output_path)

#收集数据
def collect_data():
    #初始化返回结果
    data_arr_list=[]
    #遍历要导入文件的列表
    for data_filename in data_filenames:
        #文件完整路径
        data_file=os.path.join(data_path,data_filename)
        #通过 numpy 把CSV文件导入到 numpy 数组 data_str 中
        # CSV文件 是以,分割,每列均当成是string型,第一行忽略
        data_arr=np.loadtxt(data_file,delimiter=',',dtype='str',skiprows=1)        
        # 写入 结果列表 中
        data_arr_list.append(data_arr)
    return data_arr_list

#处理数据
def process_data(data_arr_list):
    #初始化返回结果
    in_stock_min_list =[]
    #遍历要数据列表
    for data_arr in data_arr_list:
        #取第2列(库存时间)
        in_stock_str_col=data_arr[:,1]
        #去除 " 
        in_stock_col=np.core.defchararray.replace(in_stock_str_col,'"','')
        # 查看 维度/Size 等
        # print('Shape:',in_stock_col.shape)
        # print('ndim:',in_stock_col.ndim)
        # print('Size:',in_stock_col.size)
        #转化为float型
        in_stock_col_f=in_stock_col.astype('float')
        # 写入 结果列表 中
        in_stock_min_list.append(in_stock_col_f)
    return in_stock_min_list

#分析数据
def analyze_data(in_stock_min_list):
    #初始化返回结果
    in_stock_mean_list=[]
    for i,in_stock_min in enumerate(in_stock_min_list):
        #求平均值
        in_stock_mean=np.mean(in_stock_min)
        # print('平均时间为:',(data_filenames[i],in_stock_mean))
        # 写入 结果列表 中
        in_stock_mean_list.append(in_stock_mean)
    print(in_stock_mean_list)
    return in_stock_mean_list

#展示结果
def show_results(in_stock_mean_list):
    #用 matplotlib 库中的 pyplot 来画出 图形
    plt.figure()

    plt.bar(range(len(in_stock_mean_list)),in_stock_mean_list)
    #显示
    plt.show()
    pass

def main():
    #收集数据
    data_arr_list = collect_data()    
    #处理数据
    in_stock_min_list= process_data(data_arr_list)
    #分析数据
    in_stock_mean_list=analyze_data(in_stock_min_list)
    #展示结果
    show_results(in_stock_mean_list)

if __name__=='__main__':
    main()
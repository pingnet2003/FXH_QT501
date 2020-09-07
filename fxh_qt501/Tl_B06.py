import os
import numpy as np
import matplotlib.pyplot as plt

'''
统计的数据来源：来自4个文件,分别对应4个部位。
   其中格式如下：序号、库存时间、Etag、LotNo、部位、Size、入库时间、入库数量、出库时间、出库数量、Ticketid、库别、生产线、单据号
Function: 以柱状图的方式，对比显示 ML1、01A 的 4个鞋部位 平均库存时间天数 。 X 轴为 部位及两条线别，Y 轴为平均库存时间天数
'''

data_path=r'E:\\vscode_2020\\vstestfxh\\fxh_qt501\\fxh_qt501\\source_file\\lfpis'
data_filenames=['midsole.csv','ms.csv','outsole.csv','ph.csv']

bar_label_list=['Mid','Ms','Rb','Ph']

#解决 matplotlib 中文显示问题,仅适用于Windows系统
plt.rcParams['font.sans-serif']=['SimHei']

#结果输出的路径
output_path=r'./output'
#目录不存在的话，就创建
if not os.path.exists(output_path):
    os.makedirs(output_path)

#收集&处理数据
def collect_data():
    #初始化返回结果
    ml1_data_arr_list=[]
    a01_data_arr_list=[]
    #遍历要导入文件的列表
    for data_filename in data_filenames:
        #文件完整路径
        data_file=os.path.join(data_path,data_filename)
        #通过 numpy 把CSV文件导入到 numpy 数组 data_str 中
        # CSV文件 是以,分割,每列均当成是string型,第一行忽略
        all_data_arr=np.loadtxt(data_file,delimiter=',',dtype='str',skiprows=1)
        # 取得库存时间列
        stock_time_data_arr_01=np.core.defchararray.replace(all_data_arr[:,1],'"','')  
        stock_time_data_arr_01=stock_time_data_arr_01.reshape(-1,1)
        # 取得生产线
        prod_line_data_arr_01=np.core.defchararray.replace(all_data_arr[:,12],'"','') 
        prod_line_data_arr_01=prod_line_data_arr_01.reshape(-1,1)
        #以横向方式 合并两个数组 axis=1 代表是 横向
        all_data_arrs=np.concatenate([stock_time_data_arr_01,prod_line_data_arr_01],axis=1)
        # print(all_data_arrs)
        # 过滤出 ML1 生产线,并求出库存时间平均值
        ml1_data_arr=all_data_arrs[all_data_arrs[:,1]=='LF ML1']
        ml1_data_arr_value=np.mean(ml1_data_arr[:,0].astype('float'))
        # 过滤出 01A 生产线,并求出库存时间平均值
        a01_data_arr=all_data_arrs[all_data_arrs[:,1]=='LF 01A']
        a01_data_arr_value=np.mean(a01_data_arr[:,0].astype('float'))
        # 写入 结果列表 中
        ml1_data_arr_list.append(ml1_data_arr_value)
        a01_data_arr_list.append(a01_data_arr_value)

    print(ml1_data_arr_list)
    print(a01_data_arr_list)
    return ml1_data_arr_list,a01_data_arr_list

#保存&展示结果
def show_result(ml1_data_arr_list,a01_data_arr_list):
    #柱状图位置
    bar_locs=np.arange(4)
    #柱状图宽度
    bar_width=0.35
    #柱状图 X 轴标识
    xtick_labels=[bar_label_list[i] for i in range(4)]
    
    #用 matplotlib 库中的 pyplot 来画出 图形
    plt.figure()
    #柱状图
    plt.bar(bar_locs,ml1_data_arr_list,width=bar_width,color='g',alpha=0.7,label='ML1')
    plt.bar(bar_locs+bar_width,a01_data_arr_list,width=bar_width,color='r',alpha=0.7,label='01A')
    plt.xticks(bar_locs+bar_width/2,xtick_labels,rotation=45)
    plt.ylabel='平均库存时间(单位:天)'
    plt.title('柱状图')
    plt.legend(loc='best')
    plt.tight_layout()
    plt.savefig(os.path.join(output_path,'group_bar.png'))
    plt.show()
    
def main():
    ml1_data_arr_list,a01_data_arr_list=collect_data()
    show_result(ml1_data_arr_list,a01_data_arr_list)

if __name__=='__main__':
    main()
import os
import numpy as np
import matplotlib.pyplot as plt

'''
统计的数据来源：来自4个文件,分别对应4个部位。
   其中格式如下：序号、库存时间、Etag、LotNo、部位、Size、入库时间、入库数量、出库时间、出库数量、Ticketid、库别、生产线、单据号
Function: 测算出4个部位的“平均库存时间”,以 饼图 方式 显示
'''

#源文件路径及文件名
data_file_path=r'E:\\vscode_2020\\vstestfxh\\fxh_qt501\\fxh_qt501\\source_file\\lfpis'
data_filenames=['midsole.csv','ms.csv','OUTSOLE.csv','ph.csv']
#要过滤的数据列表
filter_str_list=['MIDSOLE','MS','OUTSOLE','PH']

#结果输出的路径
output_path='./output'
#目录不存在的话，就创建
if not os.path.exists(output_path):
    os.makedirs(output_path)

#收集&处理数据
def collect_process_data():
    #初始化返回结果
    data_col_list=[]
    #遍历要导入文件的列表
    for data_filename in data_filenames:
        #文件完整路径
        data_file=os.path.join(data_file_path,data_filename)
        #通过 numpy 把CSV文件导入到 numpy 数组 data_str 中
        # CSV文件 是以,分割,每列均当成是string型,第一行忽略
        data_arr=np.loadtxt(data_file,dtype='str',delimiter=',',skiprows=1)
        #取第5列数据,并去掉双引号
        data_col=np.core.defchararray.replace(data_arr[:,4],'"','')        
        #因为以上得到的是一维数组，所以需要转置
        data_col=data_col.reshape(-1,1)
        # print(data_col.shape)
        # print(data_col.ndim)
        # 写入 结果列表 中
        data_col_list.append(data_col)
    #将结果列表合并为一个结果
    data_col_all=np.concatenate(data_col_list)  
    # print(data_col_all.shape)
    return data_col_all

#过滤数据
def filter_data(data_col_all):    
    #初始化返回结果
    data_filter_list=[]
    #遍历要筛选的列表
    for filter_str in filter_str_list:
        #按筛选条件过滤数据
        #因为data_col_all中只有1列,故用如下写法
        data_filter=data_col_all[data_col_all==filter_str]
        #取得过滤后结果的行数
        data_filter=data_filter.shape[0]
        # print(data_filter)
        #追加到结果集中
        data_filter_list.append(data_filter)
    return data_filter_list

#保存&展示结果
def save_show_result_pie(data):    
    #用 matplotlib 库中的 pyplot 来画出 图形
    plt.figure()
    #用 PIE 饼图来显示
    plt.pie(data,labels=['Midsole','Ms','Outsole','PH'],explode=(0.05,0.05,0,0),shadow=True,autopct='%.2f%%')
    plt.axis('equal')
    plt.tight_layout()
    plt.savefig(os.path.join(output_path,'./result_pie.png'))
    plt.show()

def main():
    data_col_all=collect_process_data()
    data = filter_data(data_col_all)
    save_show_result_pie(data)

if __name__ == '__main__':
    main()


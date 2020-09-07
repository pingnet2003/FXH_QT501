import os
import numpy as np
import matplotlib.pyplot as plt

'''
统计的数据来源：来自4个文件,分别对应4个部位。
   其中格式如下：序号、库存时间、Etag、LotNo、部位、Size、入库时间、入库数量、出库时间、出库数量、Ticketid、库别、生产线、单据号
Function: 以直方图的方式，对比显示 Outsole,PH的 库存时间天数 对应的记录数。 X 轴为库存时间天数，Y 轴为记录数
'''

data_path=r'E:\\vscode_2020\\vstestfxh\\fxh_qt501\\fxh_qt501\\source_file\\lfpis'
data_filenames=['midsole.csv','ms.csv','OUTSOLE.csv','ph.csv']

#结果输出参数设定
output_path='./output'
if not os.path.exists(output_path):
    os.makedirs(output_path)

#直方图参数
hist_range=(0,30)
n_bins=30

#收集&处理数据
def collect_process_data():
    #初始化返回结果
    data_arr_list=[]
    #遍历要导入文件的列表
    for data_filename in data_filenames:
        #文件完整路径
        data_file=os.path.join(data_path,data_filename)
        #通过 numpy 把CSV文件导入到 numpy 数组 data_str 中
        # CSV文件 是以,分割,每列均当成是string型,第一行忽略
        data_arr_str=np.loadtxt(data_file,dtype='str',skiprows=1,delimiter=',')
        # 只取第2列：库存时间(天)
        data_arr_col1=np.core.defchararray.replace(data_arr_str[:,1],'"','')
        #因为以上得到的是一维数组，所以需要转置
        data_arr1=data_arr_col1.reshape(-1,1)        
        # 只取第5列：鞋部位
        data_arr_col4=np.core.defchararray.replace(data_arr_str[:,4],'"','')
        #因为以上得到的是一维数组，所以需要转置
        data_arr4=data_arr_col4.reshape(-1,1)
        #以横向方式 合并两个数组 axis=1 代表是 横向
        data_arr=np.concatenate([data_arr1,data_arr4],axis=1)
        # 写入 结果列表 中
        data_arr_list.append(data_arr)

    #将列表合并成一个数组(以纵向方式)
    all_data_arr_list=np.concatenate(data_arr_list,axis=0)
    
    #取出OUTSOLE
    Outsole_data_arr=all_data_arr_list[all_data_arr_list[:,1]=='OUTSOLE']          

    #取出OUTSOLE中小于30天的库存
    Outsole_data30_arr=Outsole_data_arr[Outsole_data_arr[:,0].astype('float')<30.0]    
    #取出OUTSOLE中大于30天的库存
    Outsole_data60_arr=Outsole_data_arr[Outsole_data_arr[:,0].astype('float')>=30.0]        
    print(Outsole_data60_arr.shape)

    #只取第1列,并转化为float型
    Outsole_data30_arr=Outsole_data30_arr[:,0].astype('float')
    Outsole_data30_arr=Outsole_data30_arr.reshape(-1,1)
    # print(Outsole_data30_arr)
    
    #取出 PH
    Ph_data_arr=all_data_arr_list[all_data_arr_list[:,1]=='PH']    

    #取出 PH 中小于30天的库存
    Ph_data30_arr=Ph_data_arr[Ph_data_arr[:,0].astype('float')<30.0]    
    #取出 PH 中大于30天的库存
    Ph_data60_arr=Ph_data_arr[Ph_data_arr[:,0].astype('float')>=30.0]        
    print(Ph_data60_arr.shape)

    #只取第1列,并转化为float型
    Ph_data30_arr=Ph_data30_arr[:,0].astype('float')
    Ph_data30_arr=Ph_data30_arr.reshape(-1,1)
    
    return Outsole_data30_arr,Ph_data30_arr

def analyze_data(Outsole_data30_arr,Ph_data30_arr):    
    Outsole_list,Outsole_bin_edges=np.histogram(Outsole_data30_arr,range=hist_range,bins=n_bins)    
    print('Outsole 直方图统计信息:{}'.format(Outsole_list))
    print('Outsole 直方图分组边界:{}'.format(Outsole_bin_edges))
    Ph_list,Ph_bin_edges=np.histogram(Ph_data30_arr,range=hist_range,bins=n_bins)
    print('PH 直方图统计信息:{}'.format(Ph_list))
    print('PH 直方图分组边界:{}'.format(Ph_bin_edges))
    pass

#保存&展示结果
def save_show_result(Outsole_data30_arr,Ph_data30_arr):
    # print(Outsole_data_arr[0:3,0])         
    # np.savetxt('./r2.csv',Outsole_data_arr,delimiter=',',fmt='%.2f',comments='')
    #用 matplotlib 库中的 pyplot 来画出 图形
    fig=plt.figure(figsize=(10,5))
    #加入直方图1
    ax1=fig.add_subplot(1,2,1)
    #加入直方图2, 与直方图1 的Y 坐标等值
    ax2=fig.add_subplot(1,2,2,sharey=ax1)

    #直方图1
    ax1.hist(Outsole_data30_arr,range=hist_range,bins=n_bins)
    #X 坐标值
    ax1.set_xticks(range(0,30,1))
    #直方图1 标题
    ax1.set_title('Outsole Stock Time')
    #直方图1 的 Y 坐标
    ax1.set_ylabel('Count')
    
    ax2.hist(Ph_data30_arr,range=hist_range,bins=n_bins)
    ax2.set_xticks(range(0,30,1))
    ax2.set_title('PH Stock Time')
    ax2.set_ylabel('Count')

    # plt.xticks(range(0,4),['midsole','ms','OUTSOLE','ph'],rotation=45)  
    # 直方图布局  
    plt.tight_layout()
    #保存
    plt.savefig(os.path.join(output_path,'type_histogram.png'))
    #显示
    plt.show()

def main():
    Outsole_data30_arr,Ph_data30_arr=collect_process_data()
    analyze_data(Outsole_data30_arr,Ph_data30_arr)
    save_show_result(Outsole_data30_arr,Ph_data30_arr)
    # pass

if __name__=='__main__':
    main()
    
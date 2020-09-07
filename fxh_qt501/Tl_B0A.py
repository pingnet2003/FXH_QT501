# -*- coding:utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import os

data_file=r'D:\\vscode_2020\\vstestfxh\\fxh_qt501\\fxh_qt501\\source_file\\sfpis\\rb090.csv'
model_file=r'D:\\vscode_2020\\vstestfxh\\fxh_qt501\\fxh_qt501\\source_file\\sfpis\\100.csv'

output_path=r'./output'
if not os.path.exists(output_path):
    os.makedirs(output_path)

def collect_data():
    '''
    收集数据：用pandas的 read_csv 函数来读取数据(encoding='gbk' 是为了读取中文字符)
    '''
    data_df=pd.read_csv(data_file)
    model_df=pd.read_csv(model_file,encoding='gbk')
    return data_df,model_df

def process_data(data_df,model_df):
    '''
    处理数据：用pandas的 merge 函数来合并两个数据集
    '''
    #先在data_df 中，新增一列，用来合并 rb090_stock_no 与 rb090_component 两列
    data_df['component']=data_df['RB090_STOCK_NO'].str.cat(data_df['RB090_COMPONENT'],sep='_')
    data_df['WO020_LOT_NO']=data_df['RB090_LOT_NO'].astype('str')

    merge_df=pd.merge(data_df,model_df,on='WO020_LOT_NO',how='inner')
    print(merge_df.head())
    print(merge_df.describe())

    return merge_df

def analyze_data(merge_df):
    '''
    分析数据：用pandas的 groupby 函数，以model 来合并 in_qty
    '''
    model_group=merge_df.groupby('MODEL')['RB090_IN_QTY'].sum()
    #对结果以降序排列
    model_group.sort_values(ascending=False,inplace=True)
    return model_group    

def show_save_result(model_group):
    '''
    保存结果: 存成CSV文件,形成直方图
    '''
    model_group.to_csv(os.path.join(output_path,'model_group.csv'))
    model_group.plot(kind='bar',rot=45)
    plt.tight_layout()
    plt.show()    

def main():
    data_df,model_df=collect_data()
    merge_df=process_data(data_df,model_df)
    model_group=analyze_data(merge_df)
    show_save_result(model_group)

if __name__=='__main__':
    main()

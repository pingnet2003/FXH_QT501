import pandas as pd
import os
import matplotlib.pyplot as plt

data_file=r'E:\\vscode_2020\\vstestfxh\\fxh_qt501\\fxh_qt501\\source_file\\sfpis\\rb090.csv'

#输出位置
output_path=r'./output'
if not os.path.exists(output_path):
    os.makedirs(output_path)

def collect_data():
    '''
    收集数据：用pandas的 read_csv 函数来读取数据
    '''
    data_df=pd.read_csv(data_file)
    return data_df

def inspect_data(data_df):
    '''
    查看数据:通过 info、head、describe 函数来 读取基本信息
    '''    
    print(data_df.info())
    print('-'*20)
    print(data_df.head())
    print('-'*20)
    print(data_df.describe())
    pass

def process_data(data_df):    
    '''
    清洗数据：清除 为空值的记录
    '''    
    # cln_data_df=data_df.dropna()
    # print(cln_data_df.info())

    # 过滤数据：只取ML1线的数据
    cond_ml1= (data_df['RB090_PROD_LINE']=='SF ML1')
    cond_ml1_data=data_df[cond_ml1]
    # print(cond_ml1_data)
    pass

def analyze_data(data_df):
    '''
    分析、加工数据：以Stock_no分类,合计 in_qty,out_qty
    '''    
    # 以 in_qty 降序排列
    top20_qty=data_df.sort_values(by='RB090_IN_QTY',ascending=False).head(20)
    # print(top20_qty)
    grouped_df=data_df.groupby('RB090_STOCK_NO')
    group_result=grouped_df['RB090_IN_QTY','RB090_OUT_QTY'].sum()
    return group_result    

def show_save_result(group_result):
    '''
    保存结果: 存成CSV文件,形成直方图(in_qty& out_qty堆叠)
    '''
    group_result.to_csv(os.path.join(output_path,'group_result.csv'))
    # group_result.plot(kind='bar',x='Stock_no',y='In_qtys')
    group_result.plot.bar(stacked=True)
    plt.title('In qty/Outqty')
    plt.tight_layout()
    plt.legend(loc='best')
    plt.savefig(os.path.join(output_path,'group_result.png'))
    plt.show()    

def main():
    #收集数据
    data_df=collect_data()
    #查看数据
    # inspect_data(data_df)
    #清洗数据
    process_data(data_df)
    #分析、加工数据
    group_result=analyze_data(data_df)
    #保存结果
    show_save_result(group_result)

if __name__ == '__main__':
    main()

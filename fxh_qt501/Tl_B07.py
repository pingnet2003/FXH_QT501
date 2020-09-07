import pandas as pd
import os
import matplotlib.pyplot as plt

data_file=r'E:\\vscode_2020\\vstestfxh\\fxh_qt501\\fxh_qt501\\source_file\\sfpis\\rb090.csv'

#
output_path='./output'
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
    print(data_df.info)
    # print('-------------------'*3)
    # print(data_df.head())
    # print('-------------------'*3)
    # print('共{}行,共{}列'.format(data_df.shape[0],data_df.shape[1]))
    # print('-------------------'*3)
    # print(data_df.describe())    

def analyze_data(data_df):
    '''
    分析数据：以鞋部位分类,计算记录数
    '''
    #查鞋部位共有几种分类
    component_col=data_df['RB090_COMPONENT']
    component_categories=component_col.unique()
    print('部位类别为:')
    print(component_categories)

    #以鞋部位分类,计算记录数
    categories_grouped=data_df.groupby('RB090_COMPONENT')
    categories_count=categories_grouped['RB090_COMPONENT'].count()
    categories_in_sum=categories_grouped['RB090_IN_QTY'].sum()
    categories_out_sum=categories_grouped['RB090_OUT_QTY'].sum()

    return categories_count,categories_in_sum,categories_out_sum

def save_show_result(categories_count,categories_in_sum,categories_out_sum):
    '''
    显示结果，并保存结果到图片
    '''
    #保存到CSV文件
    categories_count.to_csv(os.path.join(output_path,'category_Count.csv'))
    categories_in_sum.to_csv(os.path.join(output_path,'category_in_qty.csv'))
    categories_out_sum.to_csv(os.path.join(output_path,'category_out_qty.csv'))
    #以直方图方式显示
    categories_count.plot(kind='bar')
    plt.title('Category Count')
    plt.tight_layout()
    plt.savefig(os.path.join(output_path,'category_count.png'))
    plt.show()
    #以直方图方式显示
    categories_in_sum.plot(kind='bar')
    plt.title('Category In Sum Qty')
    plt.tight_layout()
    plt.savefig(os.path.join(output_path,'category_in_qty.png'))
    plt.show()

def main():
    data_df=collect_data()
    inspect_data(data_df)
    categories_count,categories_in_sum,categories_out_sum=analyze_data(data_df)
    save_show_result(categories_count,categories_in_sum,categories_out_sum)

if __name__=='__main__':
    main()

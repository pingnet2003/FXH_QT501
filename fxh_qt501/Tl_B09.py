import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import os

data_file=r'E:\\vscode_2020\\vstestfxh\\fxh_qt501\\fxh_qt501\\source_file\\sfpis\\wo020.csv'

#Output
Output_path='./output'
if not os.path.exists(Output_path):
    os.makedirs(Output_path)

#收集数据
def collect_data():
    '''
    收集数据：用pandas的 read_csv 函数来读取数据
    '''
    # 定义要读入的列名
    # cols=['MODEL','1','2','3','4']
    # data_df=pd.read_csv(data_file,usecols=cols)
    data_df=pd.read_csv(data_file)
    #空白部分,以0填入
    clean_data_df=data_df.fillna(0)
    print(clean_data_df.info())
    print(clean_data_df.head())
    return clean_data_df    

def analyze_by_type(data_df,attr):
    '''
    分析数据：比较不同Model类别，attr属性值分布
    '''
    sns.boxplot(data=data_df,x='MODEL',y=attr)
    plt.show()    

def analyze_dual_variables(data_df,var1,var2):
    """
        双变量数据分布查看
    """
    sns.jointplot(x=var1,y=var2,data=data_df)
    plt.show()

def analyze_var_relationship(data_df):
    """
        可视化变量间关系
    """
    corr_df=data_df.corr()    
    sns.heatmap(corr_df)    
    plt.show()

def main():
    data_df=collect_data()
    # analyze_by_type(data_df,'1')
    # analyze_dual_variables(data_df,'1','2')
    analyze_var_relationship(data_df)

if __name__=='__main__':
    main()
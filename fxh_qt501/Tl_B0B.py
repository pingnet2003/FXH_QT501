import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data_file=r'D:\\vscode_2020\\vstestfxh\\fxh_qt501\\fxh_qt501\\source_file\\sfpis\\200.csv'

output_path='./output'
if not os.path.exists(output_path):
    os.makedirs(output_path)

def collect_data():
    ''' 以panda方式导入数据,仅导入需要的列
    '''
    cols_arr=['LOT_NO','COMPONENT','DATE_IN','IN_QTY','DATE_OUT','STOCK_NO']
    data_df=pd.read_csv(data_file,usecols=cols_arr)
    return data_df

def process_data(data_df):
    '''以'STOCK_NO','COMPONENT'排序(都以升序)
    '''
    data_df.sort_values(['STOCK_NO','COMPONENT'],ascending=[True,True],inplace=True)    
    return data_df
    pass

def analyze_data(data_df):
    '''以Panda的cut，把In_qty数据分为三等，并做数据透视
    '''
    data_df['Level']=pd.cut(data_df['IN_QTY'],bins=[-np.inf,11,24,np.inf],labels=['Low','Middle','High'])
    stock_df=pd.pivot_table(data_df,index='STOCK_NO',columns=['Level'],values=['IN_QTY'],aggfunc='count')
    stock_df.fillna(0,inplace=True)
    return stock_df    
    pass

def show_save_result(stock_df ):
    '''把数据展现并保存
    '''
    stock_df.to_csv(os.path.join(output_path,'stock_df.csv'))
    stock_df.plot(kind='bar',stacked=True,title='In_qty')
    plt.tight_layout()
    plt.show()
    pass

def main():
    data_df=collect_data()
    data_df=process_data(data_df)
    stock_df = analyze_data(data_df)
    show_save_result(stock_df )

if __name__=='__main__':
    main()
# Author: Jangwoo Lee, Eawag & ETH Zurich (as of 2020)
# Related publication: To be updated...
# Purpose of this code: To calculate GPM (gene per million)

import pandas as pd
import os
import numpy as np

os.chdir('C:/Users/leejangw/AppData/Local/Programs/Python/Scripts/New_folder_3/test_github') # setting working directory

### to calculate the rpk for every orfs (to calculate PMSF in the end)
df=pd.read_csv('M17_genes.coverage.csv',sep=',',skip_blank_lines=True,index_col=None) # 
df.columns = ['name', 'avr_coverage', 'ref_length']
readno=df['ref_length']*df['avr_coverage']/150 # to calculate read no. (=ref.length x avr.coverage / read length of 150bp)
readno=readno.tolist()
readno=pd.DataFrame(readno,columns=['readno'])

RPK=readno['readno']*1000/df['ref_length'] # to calculate RPK (=read no. x 1000 / ref.length)
RPK=RPK.tolist()
RPK=pd.DataFrame(RPK,columns=['RPK'])

df_new=pd.concat([df,readno,RPK],axis=1) # to merge three dataframes (readno, RPK ro df)
df_new.to_csv('M17_genes.coverage_v2.csv',sep=',',index=False) # to save the final results as a 'coverage.v2.csv' file

### to calculate the per million scaling factor (PMSF) for each sample
df_PMSF=pd.read_csv('M17_genes.coverage_v2.csv',sep=',',skip_blank_lines=True,index_col=None)
PMSF=df_PMSF['RPK'].sum()/1000000

### to calculate Gene per Million (GPM) for each ORF
df_GPM=pd.read_csv('M17_prodigal_v2_readno_RPK.csv',sep=',',skip_blank_lines=True,index_col=None)
GPM=df_GPM['RPK']/PMSF # to calculate GPM (=RPK / PMSF)
GPM=GPM.tolist()
GPM=pd.DataFrame(GPM,columns=['GPM'])
df_new_2=pd.concat([df_GPM,GPM],axis=1) # to merge two dataframes (GPM to df_GPM)
df_new_2.to_csv('M17_prodigal_v2_readno_RPK_GPM.csv',sep=',',index=False) # to save the final results as a 'v2_readno_RPK_GPM.csv' file
 



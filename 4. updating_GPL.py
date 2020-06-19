# Author: Jangwoo Lee, Eawag & ETH Zurich (as of 2020)
# Related publication: To be updated...
# Purpose of this code: To calculate GPL (gene per liter) using 16S qPCR data & GP16S values

import pandas as pd
import os

os.chdir('C:/Users/leejangw/AppData/Local/Programs/Python/Scripts/New_folder_3/test_github') # setting working directory

df_16S=pd.read_csv('nrp72_16Scopy.csv',sep=',',skip_blank_lines=True,index_col=None) # qPCR results (unit: copies/mL)

### to calculate GPL --> GP16S X 16S copies per mL (df_16S) X 1000 (for correcting mL to L) 
df=pd.read_csv('M17_prodigal_v2_readno_RPK_GPM_GP16S.csv',sep=',',skip_blank_lines=True,index_col=None)
df['GPL']=df['GP16S']*df_16S.loc[0,'16S_copy']*1000
sub_df=df.loc[(df['avr_coverage']>0)]
sub_df.to_csv('M17_prodigal_v3.csv',sep=',',index=False) # the final dataframe where GPL values were updates


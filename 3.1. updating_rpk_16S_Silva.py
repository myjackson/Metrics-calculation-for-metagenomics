# Author: Jangwoo Lee, Eawag & ETH Zurich (as of 2020)
# Related publication: To be updated...
# Purpose of this code: To calculate RPK for 16S rRNA genes

import pandas as pd
import os
import numpy as np

os.chdir('C:/Users/leejangw/AppData/Local/Programs/Python/Scripts/New_folder_3/test_github') # setting working directory

df_ref=pd.read_csv('M17_genes.coverage_v2.csv',sep=',',skip_blank_lines=True,index_col=False) # previously updated coverage files for all the orfs in the sample (M17 in this case)
df=pd.read_csv('M17_prodigal_Silva.csv',sep=',',skip_blank_lines=True,index_col=False) # the main dataframe; the identified 16S rRNA genes using SILVA as a reference database; here the 16S rRNA gene search was performed for the assembled orfs
df_new=df[(df['pident']>=85.0) & (df['length']>=200)] # we used a stricter cut-off criteria (e.g. cutoff length 200 for 16S gene vs 100 for ARGs) in order to minimize the over-representation of 16S rRNA genes due to the imbalance between ARGs (e.g. SARG v2.0) and 16S rRNA gene databases (SILVA v138.0). 
df_new.to_csv('M17_prodigal_Silva_v1.csv',sep=',',index=False) # to save the updated 16S file

df_2=pd.read_csv('M17_prodigal_Silva_v1.csv',sep=',',skip_blank_lines=True,index_col=False) # to read the newly updated 16S data file 

ls=[] # un empty list where the rpk values will be updated

### a look-up table for updating rpk values from 'df_ref' file
for i in range(len(df_2['qseqid'].tolist())):
    if df_2.loc[i,'qseqid'] in df_ref['name'].tolist():
        num=np.where(df_ref['name']==df_2.loc[i,'qseqid'])
        ls.append(df_ref.loc[num[0][0],'RPK'])
    else:
        ls.append('NA')

df_new=pd.DataFrame(ls,columns=['RPK']) # to convert rpk list to a dataframe (with column name of 'RPK')
pd.concat([df_2,df_new],axis=1).to_csv('M17_prodigal_Silva_v2.csv',sep=',',index=False) # to merge two dataframes and finally generate a rpk-updated 16S dataframe

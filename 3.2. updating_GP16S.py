# Author: Jangwoo Lee, Eawag & ETH Zurich (as of 2020)
# Related publication: To be updated...
# Purpose of this code: To calculate RPK for 16S rRNA gene & GP16S (genes per a 16S rRNA gene)

import pandas as pd
import os

os.chdir('C:/Users/leejangw/AppData/Local/Programs/Python/Scripts/New_folder_3/test_github') # setting working directory

df_16S=pd.read_csv('M17_prodigal_Silva_v2.csv',sep=',',skip_blank_lines=True,index_col=None)
RPK_16S=df_16S['RPK'].sum() # to calculate RPK for 16S rRNA genes (summing up all the RPK values for 16S genes identified)

df_ARG=pd.read_csv('M17_prodigal_v2_readno_RPK_GPM.csv',sep=',',skip_blank_lines=True,index_col=None)
df_ARG['GP16S']=df_ARG['RPK']/RPK_16S # to calculate GP16S value for each gene (RPK for each gene devided by RPK_16S)
df_ARG.to_csv('M17_prodigal_v2_readno_RPK_GPM_GP16S.csv',sep=',',index=False) # to save the final result 


        
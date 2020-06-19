# Author: Jangwoo Lee, Eawag & ETH Zurich (as of 2020)
# Related publication: To be updated...
# Purpose of this code: To find average coverage (avr.cov) and recerence length (ref.len) for each orf from reference datafile and update/merge those information to the main dataframe.

import pandas as pd
import os
import numpy as np

os.chdir('C:/Users/leejangw/AppData/Local/Programs/Python/Scripts/New_folder_3/test_github') # setting working directory

df_0=pd.read_csv('M17_prodigal.csv',sep=',',skip_blank_lines=True,index_col=None) # to read raw datafile (blastp results for the orfs predicted by Prodigal)
df=df_0[(df_0['pident']>=85.0) & (df_0['length']>=100)] # to subset the orf that fulfils quality criteria (pidend = 85 %, length = 100 bp in our case)
df.to_csv('M17_prodigal_v1.csv',sep=',',index=False) # to save the previous results in another file

df=pd.read_csv('M17_prodigal_v1.csv',sep=',',skip_blank_lines=True,index_col=None) # to read dataframe to which avr.cov and ref.len will be updated
df_ref=pd.read_csv('M17_genes.coverage.csv',sep=',',skip_blank_lines=True,index_col=False) # a reference data file (where avr.cov & ref.len are calculated)
df_ref.columns = ['Name', 'Average_coverage', 'Reference_length'] # the list where column names are saved

ls_ref_1=[] # a reference list_1 (for Name)
ls_ref_1=df_ref['Name'].tolist()     

ls_ref_2=[] # a reference list_2 (for Average_coverage)
ls_ref_2=df_ref['Average_coverage'].tolist() 

ls_ref_3=[] # a reference list_3 (for Reference_length)
ls_ref_3=df_ref['Reference_length'].tolist()

ls_results_1=[] # an empty list_1 (where the Average_coverage will be updated)
ls_results_2=[] # an empty list_2 (where the Reference_length will be updated)

### a look-up table algorithm 
for i in range(len(df['qseqid'])):
    obj=df.loc[i,'qseqid']
    if obj in ls_ref_1:
        num=np.where(df_ref['Name']==obj)
        ls_results_1.append(ls_ref_2[num[0][0]])
        ls_results_2.append(ls_ref_3[num[0][0]])
    else:
        ls_results_1.append('NA')
        ls_results_2.append('NA')

df_new_1=pd.DataFrame(ls_results_1,columns=['avr_coverage']) # to create another dataframe for 'avr_coveage' column
df_new_2=pd.DataFrame(ls_results_2,columns=['ref_length']) # to create another dataframe for 'ref_length' column
df_new=pd.concat([df_new_1,df_new_2],axis=1) # to merge two dataframes (df_new_1 to df_new_2)
df_merged=pd.concat([df,df_new],axis=1) # to merge two dataframes (df_new to df)
df_merged.to_csv('M17_prodigal_v2.csv',sep=',',index=False) # to save the updated file to version 6 file (.v6.csv)



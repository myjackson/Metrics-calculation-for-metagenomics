# Author: Jangwoo Lee, Eawag & ETH Zurich (as of 2020)
# Related publication: To be updated...
# Purpose of this code: To calculate read no. (the number of reads assigned to an orf) & RPK (reads per kilobase).

import pandas as pd
import os

os.chdir('C:/Users/leejangw/AppData/Local/Programs/Python/Scripts/New_folder_3/test_github') # setting working directory

df_read=pd.read_csv('M17_prodigal_v2.csv',sep=',',skip_blank_lines=True,index_col=None) # the main dataset where redno will be updated

### to calculate the Number of Assigned Reads to Each Gene (readno)
readno=df_read['ref_length']*df_read['avr_coverage']/150 # to calculate the number of assigned reads (read no. = ref.length x avr.coverage / read length of 150 bp)
readno=readno.tolist()
readno=pd.DataFrame(readno,columns=['readno'])
df_new=pd.concat([df_read,readno],axis=1) # to merge two dataframes (readno to df_read)
df_new.to_csv('M17_prodigal_v2_readno.csv',sep=',',index=False) # to save the final results as a 'v2_readno.csv' file

### to calculate the Reads per Kilobase (RPK)
df_RPK=pd.read_csv('M17_prodigal_v2_readno.csv',sep=',',skip_blank_lines=True,index_col=None)
RPK=df_RPK['readno']*1000/df_RPK['ref_length'] # to calculate RPK (=read no. / ref.length x 1000) 
RPK=RPK.tolist()
RPK=pd.DataFrame(RPK,columns=['RPK'])
df_new_2=pd.concat([df_RPK,RPK],axis=1) # to merge two dataframes (RPK to df_RPK)
df_new_2.to_csv('M17_prodigal_v2_readno_RPK.csv',sep=',',index=False) # to save the final results as a 'v2_readno_RPK.csv' file
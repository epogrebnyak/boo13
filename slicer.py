# -*- coding: utf-8 -*-
"""Create reduced datasets based on *all2013.csv* and *inn.csv*"""

import pandas as pd

from column_names import colname_to_varname_dict as SUB
NON_MONETARY_COLUMNS = ['inn', 'year', 'okved1', 'region', 'title']
MY_COLS = NON_MONETARY_COLUMNS + [x for x in SUB.keys()]

# COMMENT: In this file it would help to have docstrings in the methods to explain what they do

def shorten(df, new_colnames=MY_COLS, replace_colnames_dict=SUB):
    return df[new_colnames].rename(columns=replace_colnames_dict)

def flags(df):
    N = len(df)
    # активы = пассивы
    flag1 = abs(df.ta-df.tp).sum()/N
    # внеоборотные активы + оборотные активы = активы    
    flag2 = abs(df.ta_fix + df.ta_nonfix - df.ta).sum()/N
    # капитал + долгосрочные обязательства + краткосрочные обязательства = всего пассивы
    flag3 = abs(df.tp_cap+df.tp_short+df.tp_long-df.tp).sum()/N
    return flag1, flag2, flag3    

def check_balance(df, treshold = 0.1):
    for flag in flags(df):
        assert flag < treshold
        # COMMENT: Here can also do:
        # if flag>=threshold:
        #   raise Exception("Flag {} >= threshold {}".format(flag, threshold))
            
# COMMENT: fileds -> typo
def _extract_fileds_from_compact_df(compact_df_prev, fields = ['sales', 'of']):
    sub = {x:x+"_prev" for x in fields} 
    df2 = compact_df_prev[fields].rename(columns=sub)
    df2['inn'] = compact_df_prev['inn']
    return df2 

def get_prev_compact_df():
    df_prev = pd.read_csv("data/all2012.csv", sep = ";")
    compact_df_prev = shorten(df_prev) 
    return _extract_fileds_from_compact_df(compact_df_prev, fields = ['sales', 'of'])

def make_main():
    df = pd.read_csv("data/all2013.csv", sep = ";")
    renamed_df = shorten(df)  
    
    # add fields from previous year
    df2 = get_prev_compact_df()
    merged_df = renamed_df.merge(df2, on='inn')
    
    merged_df.to_csv("data/merged.csv", sep = ";", index = False, encoding = "utf-8")
    
if __name__ == "__main__":
    # COMMENT: If this is where the memory crashes, consider reading the file in chunks
    # first answer on here:
    # http://stackoverflow.com/questions/31765123/pandas-dataframe-merge-memoryerror
    df = pd.read_csv("data/all2013.csv", sep = ";")
    renamed_df = shorten(df)  
    
    # add fields from previous year
    df2 = get_prev_compact_df()
    # COMMENT: If this is where the memory crashes, perhaps setting inn as the index can help.
    # If not, we can indeed look into sql solutions (they will still need indexes on inn for sure though)
    merged_df = renamed_df.merge(df2, on='inn')
    
    merged_df.to_csv("data/merged.csv", sep = ";", index = False, encoding = "utf-8")

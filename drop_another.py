import pandas as pd
import tqdm

df = pd.read_csv('month_avg_price.csv',encoding='utf-8-sig')

l=[]
for i in df.values:
    l.append([i[2],i[3]])


df_l_1 = pd.DataFrame(l,columns=['品名','地區'])
df_l = df_l_1.drop_duplicates(['品名','地區'])


name_total = []
for i in tqdm.tqdm(df_l.values):
    name = []
    for j in df.values:
        if j[2] == i[0] and j[3] == i[1]:
            name.append(j)
    name_df = pd.DataFrame(name,columns=['產品區域碼','月份','品名','地區','均價','均量'])
    name_df_sort = name_df.sort_values(by =['月份'])
    name_list = name_df_sort.values


    for n in name_list:
        name_total.append(n)
        #print(n)


total_df = pd.DataFrame(name_total,columns=['產品區域碼','月份','品名','地區','均價','均量'])           
    
print(total_df)
#df_sort = df.sort_values(by=['產品區域碼'])



total_df.to_csv('month_avg_price1.csv',index = False,encoding = 'utf-8-sig')


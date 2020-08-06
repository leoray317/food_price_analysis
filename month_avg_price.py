import pandas as pd
import tqdm 

def avg(x) :
    return round(sum(x)/len(x),2)


df  = pd.read_csv('total_same_name.csv')

#做出產品及其區域之列表
food_area_list = []
for i in df.values:
    food_area_list.append([i[3],i[5]])

food_area_df = pd.DataFrame(food_area_list,columns = ['name','area'])

food_area_df=food_area_df.drop_duplicates(['name','area'])

food_area_value  = food_area_df.values
#print(food_area)
food_area = []
for i, j in enumerate(food_area_value):
    food_area.append([i,j[0],j[1]])
    

#月份列表
month = ['01','02','03','04','05','06','07','08','09','10','11','12']


month_avg_list = []
for m in month:
    for fa in tqdm.tqdm(food_area):
            month_value = []
            month_price = []
            month_volumn = []
            area = []
            food = []
            code = []
            area_code = []
            for i in df.values:
                if i[1].split('.')[1] == m and i[3] == fa[1] and i[5] == fa[2]:
                    month_price.append(i[6]) 
                    month_volumn.append(i[7])
                    month_value.append(m)
                    area.append(i[5])
                    food.append(i[3])
                    code.append(fa[0])
                    area_code.append(i[4])
            try:
                month_avg_list.append([code[0],month_value[0],food[0],area_code[0],area[0],avg(month_price),avg(month_volumn)])
                #print([code[0],month_value[0],food[0],area[0],avg(month_price),avg(month_volumn)])
            except:
                continue
        

print(month_avg_list)

month_avg_df = pd.DataFrame(month_avg_list,columns = ['產品區域碼','月份','品名','地區碼','地區','均價','均量'])

month_avg_df.to_csv('month_avd_price.csv',encoding = 'utf-8-sig',index = False)

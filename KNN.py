from sklearn import datasets   #數據庫
from sklearn.model_selection import train_test_split #取用模型選擇中的測試集與訓練集
from sklearn.neighbors import KNeighborsClassifier #訓練方式
import pandas as pd
import numpy as np
from matplotlib import pyplot  as plt

iris = pd.read_csv('new_how.csv',encoding = 'utf-8-sig')
iris_three = iris.drop("Unnamed: 0", axis = 1).drop('品名',axis = 1).drop('日期',axis = 1)
price = iris_three['價格'].tolist()
del price[0]
price.append(31.2)
iris_three['back_price'] = price

climate = pd.read_excel('final.xlsx',encoding = 'utf-8-sig')
climate_four = climate.drop("時間", axis = 1).drop('價格',axis = 1).drop('時間.1',axis = 1).drop('相對溼度(%)',axis = 1)

combin = pd.concat([iris_three,climate_four],axis=1)
    
iris_X =combin.iloc[:,1:].values
iris_y_pro =iris_three.iloc[:,:1].values
iris_y_list=[]
for i in iris_y_pro:
    iris_y_list.append(i[0])

iris_y = np.array(iris_y_list,dtype=int)

print(iris_X)
print(iris_y)

X_train, X_test, y_train, y_test = train_test_split(iris_X, iris_y, test_size=0.3)

knn = KNeighborsClassifier()
knn.fit(X_train, y_train)

predict_line = list(knn.predict(X_test))
ture_line = list(y_test)

#date= list(iris['日期'].values)
#print(len(list(iris_X)))
#print(len(list(iris_y)))
#print(len(predict_line))
#print(len(ture_line))
#print(len(date))


plt.plot(predict_line, color=(255/255,100/255,100/255))
plt.plot(ture_line, '--', color=(100/255,100/255,255/255))
plt.show()

'''


iris = datasets.load_iris()
iris_X = iris.data
iris_y = iris.target


print(iris_X)
print(iris_y)


X_train, X_test, y_train, y_test = train_test_split(iris_X, iris_y, test_size=0.3)


knn = KNeighborsClassifier()
knn.fit(X_train, y_train)

print(knn.predict(X_test))
print(y_test)
'''
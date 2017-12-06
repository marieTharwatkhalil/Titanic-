import pandas as pd
import matplotlib.pyplot as plt

Titanic = pd.read_csv("train.csv")

sur = Titanic.loc[Titanic['Survived']== 1]

survived_all = sur.loc[:,'Survived':'Pclass']
surv_num = survived_all['Survived'].count()+1

class_a = survived_all.loc[survived_all['Pclass'] == 1 ]
a_surv_num = class_a['Pclass'].count() +1

class_b = survived_all.loc[survived_all['Pclass'] == 2 ]
b_surv_num = class_b['Pclass'].count()

class_c = survived_all.loc[survived_all['Pclass'] == 3]
c_surv_num = class_c['Pclass'].count()

print("Total survived = " +str(surv_num)+"\n"
      +" class A survived = " + str(a_surv_num)+"\n"
      +" class B survived = " + str(b_surv_num)+"\n"
      + " class C survived = " + str(c_surv_num))
y = [a_surv_num, b_surv_num, c_surv_num]
x = ["Class A" ,"Class B " , "Class C"]



plt.bar(x,y,.1 )
plt.show()


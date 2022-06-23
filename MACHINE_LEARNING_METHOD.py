import pypyodbc 
import pandas as pd
#CONNECT TO SQL SERVER TO TAKE DATA
db = pypyodbc.connect(
    'Driver={SQL Server};'
    'Server=DESKTOP-ALKJBUB;'
    'Database=PERSON;'
    'Trusted_Connection=True;'
)

sql=("select * from PERSON_INFO")
#READ DATA
df1=pd.read_sql(sql,db)
df1=pd.DataFrame(df1)
#DEFINE DEPENDENT AND INDEPENDENT VALUES
x=df1.iloc[:,3:-1]
y=df1.iloc[:,-1]
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import r2_score
#DROP NULL VALUES FROM EVERY ROWS
x.dropna(axis=0,inplace=True)
#MAKE ENCODE EVERY COLUMNS
x=pd.get_dummies(x)
#DEFINE X TRAIN END Y TRAIN
x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=42,test_size=0.25)
#TEACH TO MACHINE TO PREDICT VALUE
x_train=StandardScaler().fit_transform(x_train)
x_test=StandardScaler().fit_transform(x_test)
lr=LogisticRegression()
lr.fit(x_train,y_train)
y_pred=lr.predict(x_test)
r2_score(y_test,y_pred)
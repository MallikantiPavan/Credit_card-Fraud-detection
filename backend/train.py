# Credit card fraud
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
import joblib
from sklearn.linear_model import LogisticRegression

data=pd.read_csv(r'C:\Users\pavan\Downloads\archive\creditcard.csv')

scalar_time = StandardScaler()
scalar_amount = StandardScaler()

data['Time']=scalar_time.fit_transform(data[['Time']])
data['Amount']=scalar_amount.fit_transform(data[['Amount']])




joblib.dump(scalar_time, "scaler_time.pkl")
joblib.dump(scalar_amount, "scaler_amount.pkl")
print("sucess")

x=data.drop(columns=['Class'],axis=1)
#x = data[['Amount', 'Time']]
y=data['Class']
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2, random_state=42, stratify=y)

# model = RandomForestClassifier(
#     n_estimators=300,
#     max_depth=15,
#     random_state=42,
#     class_weight="balanced_subsample",
#     n_jobs=-1
# )
# model.fit(x_train,y_train)


model = LogisticRegression(class_weight="balanced", max_iter=1000)
model.fit(x_train, y_train)

y_pred=model.predict(x_test)
# print('accuracy',accuracy_score(y_pred,y_test))
# print('Confusion matrix',confusion_matrix(y_pred,y_test))
# print('classification report',classification_report(y_pred,y_test))

joblib.dump(model,"credit.pkl")
print("model is saved")
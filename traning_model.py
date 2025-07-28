import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib

data = pd.read_csv('Student_Performance.csv')
data.columns = data.columns.str.strip()  

interest_names = data['Pass'].unique()

pass_map = {} 
for i in range(len(interest_names)):
    pass_map[interest_names[i]] = i 
data['Pass_encoded'] = data['Pass'].map(pass_map)

#interest_names = data['Pass'].unique()
#interest_map = {label: idx for idx, label in enumerate(interest_names)}
#data['Interest_encoded'] = data['Pass'].map(interest_map)

X = data[['Hours_Studied', 'Attendance']]
y = data['Pass_encoded']

model = DecisionTreeClassifier()
model.fit(X, y)

joblib.dump(model, 'model.pkl')
joblib.dump(pass_map, 'interest_map.pkl')

print('Model and mapping saved successfully.')

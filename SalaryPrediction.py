import pandas as pd
data = pd.read_csv("SalaryData.csv")
x = data['YearsExperience'].values
x = x.reshape(-1,1)
y = data['Salary']
from sklearn.linear_model import LinearRegression 
mind = LinearRegression()
model = mind.fit(x,y)
while(True):
    exp = input("\n                   Enter Your Years of Experience: ")
    exp = float(exp)
    if exp < 0 :
        print("Invalid Entry")
        break
    prediction = model.predict([[exp]])
    print("\n                       Your Salary:", prediction ,)
    if input("\n                      Do You Want To Continue[y,n]? ") != 'y':
        break
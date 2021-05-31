import pandas as pd
data = pd.read_csv("SalaryData.csv")
x = data['YearsExperience'].values
x = x.reshape(-1,1)
y = data['Salary']
from sklearn.linear_model import LinearRegression 
mind = LinearRegression()
model = mind.fit(x,y)
while(True):
    exp = input("\n \t\t\t Enter Your Years of Experience: ")
    exp = float(exp)
    if exp < 0 :
        print("\n \t\t\t Invalid Entry")
    prediction = model.predict([[exp]])
    print("\n \t\t\t Your Salary:", prediction ,)
    if input("\n \t\t\t Do You Want To Continue[y,n]? ") != 'y':
        break

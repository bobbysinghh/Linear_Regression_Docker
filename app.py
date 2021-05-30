import joblib
model=joblib.load('model.pk1')
while True:
 exp=int(input("Enter your experience in Year:  "))

 sal=str(model.predict([[exp]]))
 print('Your Expected Salary is {} '.format(sal))

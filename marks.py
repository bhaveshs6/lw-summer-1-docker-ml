import joblib
mind = joblib.load(‘model.pkl’)
x = float(input(‘Per day average study hours: ’))
print(‘Marks obtained: {}’.format(round(mind.predict([[x]]))

import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
dataset = pd.read_csv('grades.csv')
x = dataset.iloc[:, 17:20].values
y = dataset.iloc[:, 20].values
# print(x)
# print(y)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

naive = GaussianNB()
naive.fit(x_train, y_train)
predict = naive.predict(x_test)
acc = accuracy_score(y_test, predict)
print("Accuracy score:", acc)

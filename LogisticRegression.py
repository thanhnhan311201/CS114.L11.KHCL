import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn import preprocessing
from sklearn import metrics

data = pd.read_csv('fetal_health.csv', header=None)
data = data[1:].to_numpy()

data = data.astype(float)

X_train = data[:1500, 0:21]
X_test = data[1500:, 0:21]

print(data.shape)
print(X_train.shape, X_test.shape)

Y_train = data[:1500, 21]
Y_test = data[1500:, 21]

logreg = LogisticRegression(max_iter=1000000)

logreg.fit(X_train, Y_train)
Y_pred = logreg.predict(X_test)

print(metrics.confusion_matrix(Y_test, Y_pred, labels=[1.0, 2.0, 3.0]))
print(metrics.classification_report(Y_test, Y_pred, labels=[1.0, 2.0, 3.0]))


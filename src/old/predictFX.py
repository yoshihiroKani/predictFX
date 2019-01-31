# bases
import numpy as np
import pandas as pd
import codecs
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import RandomizedSearchCV
from sklearn.externals import joblib
from sklearn.datasets import load_iris
# preprocessing
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import Imputer
from sklearn.feature_selection import RFE  
# models
from sklearn.ensemble import GradientBoostingRegressor, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
# evaluation indexes
from sklearn.metrics import f1_score, accuracy_score

#データ読み込み
data = pd.read_csv('./data/USDJPY_AddedDiff_01_utf8.csv', header=0, dtype={'upis1':'int'})

DATE = data.iloc[:, [0]]
X = data.iloc[:, 1:4]
y = data.iloc[:, [5]]

## hold-out
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=5)

# pipeline
pipe_logistic = Pipeline([('scl',StandardScaler()),('est',LogisticRegression(random_state=1))])
pipe_gbc = Pipeline([('scl',StandardScaler()),('est',GradientBoostingClassifier(random_state=1))])

# 学習
pipes = [pipe_logistic, pipe_gbc]
names = ['pipe_logistic', 'pipe_gbc']

results_train = {}
results_test = {}
print('\n--- results ---\n')
for pipe, name in zip(pipes, names):
    #評価指標で分岐
    pipe.fit(X_train,y_train.as_matrix().ravel())
    y_pred = pd.DataFrame(pipe.predict(X_test))
    print('###### ' + str(name) + ' ######\n##')
    results_train[name] = f1_score(y_train.as_matrix().ravel(),pipe.predict(X_train))
    results_test[name] = f1_score(y_test.as_matrix().ravel(),pipe.predict(X_test))
    print('##  train: ' + str(results_train[name]))
    print('##  test:  ' + str(results_test[name]))
    print('##\n#########################\n')

    y_pred = pd.DataFrame(pipe.predict(X_test), columns=['y_pred'])
    y_proba = pd.DataFrame(pipe.predict_proba(X_test)).iloc[:, [-1]]
    y_proba = y_proba.rename(columns={1 : '確率'}, inplace=False)

    df_con_2 = pd.concat([DATE, y_pred, y_proba], axis=1, join='inner')

    #予測結果出力
    display(df_con_2)

from mimetypes import encodings_map
import joblib
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from lightgbm import LGBMClassifier
import pandas as pd

#data preprocessing
path_to_data = './data/heart.csv'
df = pd.read_csv(path_to_data)

#getting numerical and categorical variables
numerical= df.drop(['HeartDisease'], axis=1).select_dtypes('number').columns
categorical = df.select_dtypes('object').columns

#X: features - y: target
X= df.drop('HeartDisease', axis=1)
y= df['HeartDisease']

#splitting data - 0.7 train - 0.3 test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

#One-Hot encoding on categorical data
ohe = OneHotEncoder()
ct = make_column_transformer((ohe, categorical),remainder='passthrough')

#LightGBM classifier object
lgbmc = LGBMClassifier(random_state=0)

#define pipe to avoid data leakage
pipe = make_pipeline(ct, lgbmc)
pipe.fit(X_train, y_train)
pipe.fit(X_train, y_train)
pipe.score(X_test, y_test)
y_pred = pipe.predict_proba(X_test)

#save model into pickle file
joblib.dump(pipe, './model/lgbm_model.pkl')
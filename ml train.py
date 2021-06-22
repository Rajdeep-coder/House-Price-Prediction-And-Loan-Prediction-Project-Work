import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt
#import seaborn as sns

pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)


# Get clean data
df = pd.read_csv(r"F:\House Price Prediction Project work\ohe_data_reduce_cat_class.csv")


"""## Split Dataset in train and test"""

X = df.drop("price", axis=1)
y = df['price']
print('Shape of X = ', X.shape)
print('Shape of y = ', y.shape)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=51)
print('Shape of X_train = ', X_train.shape)
print('Shape of y_train = ', y_train.shape)
print('Shape of X_test = ', X_test.shape)
print('Shape of y_test = ', y_test.shape)

"""## Feature Scaling"""

from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
sc.fit(X_train)
X_train = sc.transform(X_train)
X_test = sc.transform(X_test)

"""## Machine Learning Model Training

## Linear Regression
"""

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error

lr = LinearRegression()
lr_lasso = Lasso()
lr_ridge = Ridge()


def rmse(y_test, y_pred):
    return np.sqrt(mean_squared_error(y_test, y_pred))


lr.fit(X_train, y_train)
lr_score = lr.score(X_test, y_test)  # with all num var 0.7842744111909903
lr_rmse = rmse(y_test, lr.predict(X_test))


# Lasso
lr_lasso.fit(X_train, y_train)
lr_lasso_score = lr_lasso.score(X_test, y_test)  # with balcony 0.5162364637824872
lr_lasso_rmse = rmse(y_test, lr_lasso.predict(X_test))


"""## Support Vector Machine"""

from sklearn.svm import SVR

svr = SVR()
svr.fit(X_train, y_train)
svr_score = svr.score(X_test, y_test)  # with 0.2630802200711362
svr_rmse = rmse(y_test, svr.predict(X_test))


"""## Random Forest Regressor"""

from sklearn.ensemble import RandomForestRegressor

rfr = RandomForestRegressor()
rfr.fit(X_train, y_train)
rfr_score = rfr.score(X_test, y_test)  # with 0.8863376025408044
rfr_rmse = rmse(y_test, rfr.predict(X_test))



print(pd.DataFrame([{'Model': 'Linear Regression', 'Score': lr_score, "RMSE": lr_rmse},
                    {'Model': 'Lasso', 'Score': lr_lasso_score, "RMSE": lr_lasso_rmse},
                    {'Model': 'Support Vector Machine', 'Score': svr_score, "RMSE": svr_rmse},
                    {'Model': 'Random Forest', 'Score': rfr_score, "RMSE": rfr_rmse}],
                   columns=['Model', 'Score', 'RMSE']))


from sklearn.model_selection import cross_val_score

cvs_rfr2 = cross_val_score(RandomForestRegressor(), X_train, y_train, cv=10)
cvs_rfr2, cvs_rfr2.mean()  # 0.9652425691235843)'''


"""## Test Model"""

list(X.columns)


# it help to get predicted value of hosue  by providing features value
def predict_house_price(model, bath, balcony, total_sqft_int, bhk, price_per_sqft, area_type, availability, location):
    x = np.zeros(len(X.columns))  # create zero numpy array, len = 107 as input value for model

    # adding feature's value accorind to their column index
    x[0] = bath
    x[1] = balcony
    x[2] = total_sqft_int
    x[3] = bhk
    x[4] = price_per_sqft

    if "availability" == "Ready To Move":
        x[8] = 1

    if 'area_type' + area_type in X.columns:
        area_type_index = np.where(X.columns == "area_type" + area_type)[0][0]
        x[area_type_index] = 1

        # print(area_type_index)

    if 'location_' + location in X.columns:
        loc_index = np.where(X.columns == "location_" + location)[0][0]
        x[loc_index] = 1

        # print(loc_index)

    # print(x)

    # feature scaling
    x = sc.transform([x])[0]  # give 2d np array for feature scaling and get 1d scaled np array
    # print(x)

    return model.predict([x])[0]  # return the predicted value by train XGBoost model


predict_house_price(model=rfr, bath=3, balcony=2, total_sqft_int=1672, bhk=3, price_per_sqft=8971.291866,
                    area_type="Plot  Area", availability="Ready To Move", location="Devarabeesana Halli")

##test sample
# area_type  availability    location    bath    balcony price   total_sqft_int  bhk price_per_sqft
# 2  Super built-up Area Ready To Move   Devarabeesana Halli 3.0 2.0 150.0   1750.0  3   8571.428571

predict_house_price(model=rfr, bath=3, balcony=2, total_sqft_int=1750, bhk=3, price_per_sqft=8571.428571,
                    area_type="Super built-up", availability="Ready To Move", location="Devarabeesana Halli")

"""# Save model &amp; load model"""
import joblib

# save model
joblib.dump(rfr, 'bangalore_house_price_prediction_rfr_model.pkl')

# load model
bangalore_house_price_prediction_model = joblib.load("bangalore_house_price_prediction_rfr_model.pkl")

# predict house priceo3
result = predict_house_price(bangalore_house_price_prediction_model, bath=3, balcony=3, total_sqft_int=150, bhk=3,
                    price_per_sqft=8514.285714, area_type="Built-up Area", availability="Ready To Move",
                    location="Devarabeesana Halli")
print(result)
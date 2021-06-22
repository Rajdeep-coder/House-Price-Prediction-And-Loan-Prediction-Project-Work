import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

df = pd.read_csv('loan_num_data2.csv')
print("Shape of data : ", df.shape)

X = df.drop("Indicators", axis=1)
y = df['Indicators']
print('Shape of X = ', X.shape)
print('Shape of y = ', y.shape)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 51)
print('Shape of X_train = ', X_train.shape)
print('Shape of y_train = ', y_train.shape)
print('Shape of X_test = ', X_test.shape)
print('Shape of y_test = ', y_test.shape)

def rmse(y_test, y_pred):
    return np.sqrt(mean_squared_error(y_test, y_pred))

sc = StandardScaler()
sc.fit(X_train)
X_train= sc.transform(X_train)
X_test = sc.transform(X_test)


model = LogisticRegression()
model.fit(X_train, y_train)

LogisticRegression(C = 1.0, class_weight=None, dual=False, fit_intercept=True,
                  intercept_scaling=1, max_iter=100, multi_class='ovr', n_jobs=1, penalty='l2',
                  random_state=1, solver='liblinear', tol=0.0001, verbose=0, warm_start=False)

lrrr_score = model.score(X_test, y_test)
lrrr_rmse = rmse(y_test, model.predict(X_test))
print("Score : ", lrrr_score, "\nError : ", lrrr_rmse)


def predict_loan(model, Loan_Amount, Loan_Tenor, age, Housing_Rental, Monthly_Income, Office_Area, Loan_Purpose,
                        Gender, Marital_Status_num, Education_Level_num, Residential_Status, Employment_Type,
                        Nature_of_Business, Job_Position):
    x = np.zeros(len(X.columns))  # create zero numpy array, len = 107 as input value for model

    # adding feature's value accorind to their column index
    x[0] = Loan_Amount
    x[1] = Loan_Tenor
    x[2] = age
    x[3] = Housing_Rental
    x[4] = Monthly_Income
    x[5] = Office_Area

    if 'Loan_Purpose_' + Loan_Purpose in X.columns:
        Loan_Purpose_index = np.where(X.columns == 'Loan_Purpose_' + Loan_Purpose)[0][0]
        x[Loan_Purpose_index] = 1

    if 'Gender_M' in X.columns:
        gender_index = np.where(X.columns == 'Gender_M')[0][0]
        if Gender == 'Male':
            x[gender_index] = 1

    if 'Marital Status_num' in X.columns:
        Marital_index = np.where(X.columns == 'Marital Status_num')[0][0]
        if Marital_Status_num == 'Single':
            x[Marital_index] = 2
        elif Marital_Status_num == 'Married':
            x[Marital_index] = 1
        else:
            x[Marital_index] = 0

    if 'Education Level_num' in X.columns:
        Education_index = np.where(X.columns == 'Education Level_num')[0][0]
        if Education_Level_num == 'Secondary':
            x[Education_index] = 4
        elif Education_Level_num == 'Form 3 or below':
            x[Education_index] = 0
        elif Education_Level_num == 'Post Graduate':
            x[Education_index] = 1
        elif Education_Level_num == 'Post Secondary':
            x[Education_index] = 2
        elif Education_Level_num == 'University':
            x[Education_index] = 5
        else:
            x[Education_index] = 3

    if 'Residential Status_' + Residential_Status in X.columns:
        Residential_Status_index = np.where(X.columns == 'Residential Status_' + Residential_Status)[0][0]
        x[Residential_Status_index] = 1

    if 'Employment Type_' + Employment_Type in X.columns:
        Employment_index = np.where(X.columns == 'Employment Type_' + Employment_Type)[0][0]
        x[Employment_index] = 1

    if 'Nature of Business_' + Nature_of_Business in X.columns:
        Business_index = np.where(X.columns == 'Nature of Business_' + Nature_of_Business)[0][0]
        x[Business_index] = 1

    if 'Job Position_' + Job_Position in X.columns:
        Job_index = np.where(X.columns == 'Job Position_' + Job_Position)[0][0]
        x[Job_index] = 1

    # print(x)

    # feature scaling
    x = sc.transform([x])[0]  # give 2d np array for feature scaling and get 1d scaled np array
    x = np.array(x).reshape((1, -1))
    # print(x)

    return model.predict(x)

result = predict_loan(model=model, Loan_Amount=50000, Loan_Tenor=12, age=25, Housing_Rental=0, Monthly_Income=1900,
                      Office_Area=1, Loan_Purpose='Business', Gender='Male', Marital_Status_num='Single',
                      Education_Level_num='Post Graduate', Residential_Status='Self-owned Private Housing',
                      Employment_Type='Fixed Income Earner', Nature_of_Business='Professional',
                      Job_Position='Government/Semi-Government')
print(result)

import joblib

# save model
joblib.dump(model, 'loan_model.pkl')

# load model
loan_model = joblib.load("loan_model.pkl")

result = predict_loan(model=loan_model, Loan_Amount='50000', Loan_Tenor='12', age='25', Housing_Rental='0', Monthly_Income='1900',
                      Office_Area='1', Loan_Purpose='Business', Gender='Male', Marital_Status_num='Single',
                      Education_Level_num='Post Graduate', Residential_Status='Self-owned Private Housing',
                      Employment_Type='Fixed Income Earner', Nature_of_Business='Professional',
                      Job_Position='Government/Semi-Government')

print(str(result[0]))

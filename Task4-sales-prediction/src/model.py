import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load dataset
df = pd.read_csv("data/advertising.csv")

# Preprocess
df = pd.get_dummies(df, columns=['Platform', 'Target_Segment'], drop_first=True)
X = df.drop('Sales', axis=1)
y = df['Sales']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
print("MSE:", mean_squared_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))

# Feature importance
coef_df = pd.DataFrame(model.coef_, X.columns, columns=["Coefficient"])
print("\nAdvertising Impact:\n", coef_df.sort_values(by="Coefficient", ascending=False))

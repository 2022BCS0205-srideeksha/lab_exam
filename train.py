import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import json
import pickle

# Load dataset
df = pd.read_csv("https://raw.githubusercontent.com/jbrownlee/Datasets/master/winequality-red.csv", sep=";")

# FIX
df.columns = df.columns.str.strip()

X = df.drop("quality", axis=1)
y = df["quality"]

# Train model
model = LinearRegression()
model.fit(X, y)

pred = model.predict(X)

mse = mean_squared_error(y, pred)
r2 = r2_score(y, pred)

print("MSE:", mse)
print("R2:", r2)

# IMPORTANT: Print identity
print("Student: Sri Deekshaa | Roll No: 2022BCS0205")

# Save metrics
with open("metrics.json", "w") as f:
    json.dump({
        "mse": mse,
        "r2": r2,
        "name": "Sri Deekshaa",
        "roll_no": "2022BCS0205"
    }, f)

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)
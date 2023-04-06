import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# Load data
data = pd.read_csv("files_train.csv")

# Select relevant features
X = data[["file_ext", "original_size", "compression_method"]]  # feature - in
y = data["compression_ratio"]  # target - out

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Create and train the model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Make predictions
file_size = 1000
file_type = 2
compression_method = 1
# Create a new dataframe with matching column names
X_new = pd.DataFrame(
    [[file_type, file_size, compression_method]], columns=X.columns)

y_pred = model.predict(X_new)

# Print the predicted compression ratio
print("Predicted Compression Ratio:", y_pred[0])

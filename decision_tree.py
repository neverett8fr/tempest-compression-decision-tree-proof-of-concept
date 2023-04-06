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
model = RandomForestRegressor(n_estimators=100, random_state=12)
model.fit(X_train, y_train)

# Make predictions
file_size = 1000

for file_type in range(1, 5, 1):
    best_method = 0
    highest_ratio = 0
    for compression_method in range(1, 3, 1):
        x = pd.DataFrame(
            [[file_type, file_size, compression_method]],
            columns=X.columns
        )
        y = model.predict(x)
        if y[0] > highest_ratio:
            best_method = compression_method
            highest_ratio = y[0]

        print("method, file, predicted ratio",
              compression_method, file_type, y[0]
              )

    print("file type, best predicted method", file_type, best_method)

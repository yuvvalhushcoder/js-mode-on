"""
Data Classification Using AI (Project 2)
Trains and compares two simple classifiers on the Iris flower dataset.

Pipeline: load data -> understand it -> split train/test -> train -> evaluate -> predict new data
Install requirement once:  pip install scikit-learn pandas
"""

import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


# ---- 1. Load and understand the dataset ----
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df["species"] = [iris.target_names[i] for i in iris.target]

print("=== 1. Dataset overview ===")
print(f"Rows: {df.shape[0]}, Features: {df.shape[1] - 1}")
print(f"Classes: {', '.join(iris.target_names)}")
print("\nFirst 5 rows:")
print(df.head().to_string(index=False))
print("\nSamples per class:")
print(df["species"].value_counts().to_string())
print("\nMissing values:", int(df.isnull().sum().sum()))

# ---- 2. Split into training and testing sets ----
X, y = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
print("\n=== 2. Train/test split ===")
print(f"Training samples: {len(X_train)}  |  Testing samples: {len(X_test)}")

# ---- 3. Apply simple classification algorithms ----
models = {
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "K-Nearest Neighbors (k=5)": KNeighborsClassifier(n_neighbors=5),
}

print("\n=== 3. Training and evaluation ===")
results = {}
for name, model in models.items():
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    acc = accuracy_score(y_test, predictions)
    results[name] = acc
    print(f"\n--- {name} ---")
    print(f"Accuracy: {acc * 100:.1f}%")
    print("Confusion matrix (rows = actual, columns = predicted):")
    print(confusion_matrix(y_test, predictions))
    print(classification_report(y_test, predictions, target_names=iris.target_names))

best = max(results, key=results.get)
print(f"Best model on this test set: {best} ({results[best] * 100:.1f}%)")

# ---- 4. Test with completely new data ----
# Measurements: sepal length, sepal width, petal length, petal width (cm)
new_flowers = [
    [5.0, 3.4, 1.5, 0.2],   # looks like a small flower with tiny petals
    [6.0, 2.8, 4.5, 1.4],   # medium-sized
    [7.2, 3.0, 5.8, 1.9],   # large flower with big petals
]
print("\n=== 4. Predictions on new, unseen flowers ===")
final_model = models[best]
for flower, label in zip(new_flowers, final_model.predict(new_flowers)):
    print(f"{flower} -> {iris.target_names[label]}")
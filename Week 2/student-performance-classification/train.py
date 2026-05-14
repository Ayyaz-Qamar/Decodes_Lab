import os
import pandas as pd
import pickle

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# =========================
# LOAD DATASET (SAFE PATH)
# =========================
DATA_PATH = os.path.join("data", "StudentsPerformance.csv")

df = pd.read_csv(DATA_PATH)

# =========================
# CREATE TARGET COLUMN
# =========================
df["average_score"] = (
    df["math score"] +
    df["reading score"] +
    df["writing score"]
) / 3

def label_performance(score):
    if score >= 80:
        return "Excellent"
    elif score >= 50:
        return "Average"
    else:
        return "Poor"

df["Performance"] = df["average_score"].apply(label_performance)

# =========================
# FEATURES / TARGET
# =========================
X = df.drop(
    [
        "math score",
        "reading score",
        "writing score",
        "average_score",
        "Performance"
    ],
    axis=1
)

y = df["Performance"]

# =========================
# ENCODING
# =========================
encoders = {}

for col in X.columns:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col])
    encoders[col] = le

target_encoder = LabelEncoder()
y = target_encoder.fit_transform(y)

# =========================
# TRAIN TEST SPLIT
# =========================
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# =========================
# MODEL TRAINING
# =========================
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# =========================
# EVALUATION
# =========================
pred = model.predict(X_test)
acc = accuracy_score(y_test, pred)

print("\n=========================")
print("MODEL ACCURACY:", acc)
print("=========================\n")

# =========================
# SAVE MODEL ARTIFACTS
# =========================
os.makedirs("models", exist_ok=True)

pickle.dump(model, open("models/student_model.pkl", "wb"))
pickle.dump(encoders, open("models/encoders.pkl", "wb"))
pickle.dump(target_encoder, open("models/target_encoder.pkl", "wb"))

print("Model and encoders saved successfully in /models folder.")
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# ==========================
# Load Dataset
# ==========================
df = pd.read_csv("../datasets/Disease_symptom_and_patient_profile_dataset.csv")

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

# ==========================
# Encode Features
# ==========================
label_encoders = {}

for col in df.select_dtypes(include="object").columns:
    if col != "Disease":
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        label_encoders[col] = le

# ==========================
# Encode Target Variable
# ==========================
disease_encoder = LabelEncoder()
df["Disease"] = disease_encoder.fit_transform(df["Disease"])

# ==========================
# Features and Target
# ==========================
X = df.drop("Disease", axis=1)
y = df["Disease"]

print("\nFeatures Used:")
print(X.columns.tolist())

# ==========================
# Split Dataset
# ==========================
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining Samples:", len(X_train))
print("Testing Samples:", len(X_test))

# ==========================
# Train Model
# ==========================
model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)

# ==========================
# Evaluate Model
# ==========================
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print(f"\nModel Accuracy: {accuracy * 100:.2f}%")

# ==========================
# Save Model Files
# ==========================
joblib.dump(model, "disease_model.pkl")
joblib.dump(disease_encoder, "disease_encoder.pkl")
joblib.dump(label_encoders, "feature_encoders.pkl")

print("\nModel Saved Successfully!")
print("Created Files:")
print("- disease_model.pkl")
print("- disease_encoder.pkl")
print("- feature_encoders.pkl")
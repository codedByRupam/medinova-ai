import pandas as pd

df = pd.read_csv("../datasets/Disease_symptom_and_patient_profile_dataset.csv")

print(df.columns)
print(df.head())
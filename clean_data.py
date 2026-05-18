import pandas as pd

df = pd.read_csv("student_dropout_dataset_v3 (1).csv")

df_cleaned = df.dropna()

df_cleaned.to_csv("student_dropout_cleaned.csv", index=False)

print("Original:", df.shape)
print("Bereinigt:", df_cleaned.shape)
print(df_cleaned.isna().sum())
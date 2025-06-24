import pandas as pd
from sklearn.ensemble import IsolationForest

# Veri setini oku
df = pd.read_csv("sample_input.csv")

# Sayısal sütunları filtrele
numeric_df = df.select_dtypes(include='number')

# Model eğitimi ve anomali tahmini
model = IsolationForest(contamination=0.05)
df['anomaly'] = model.fit_predict(numeric_df)
df['anomaly'] = df['anomaly'].map({1: 0, -1: 1})

# Sonucu CSV olarak kaydet
df.to_csv("sample_output.csv", index=False)



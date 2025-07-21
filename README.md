 🔎 AnomalyDetector

AnomalyDetector is a lightweight Python-based tool for identifying anomalies in numerical datasets using machine learning.

It takes a CSV file as input, analyzes the data using the Isolation Forest algorithm, and outputs a new CSV file with anomaly labels.

---

 🚀 Features

- 📊 Accepts any CSV with numerical columns
- 🧠 Uses Isolation Forest for unsupervised anomaly detection
- ✅ Outputs labeled results with anomaly flags
- 🔁 Fast, simple, and efficient for small to medium datasets



 🛠️ Usage

```bash
python anomaly_detector.py input.csv output.csv

 📁 Example Output

| feature_1 | feature_2 | ... | anomaly |
|-----------|-----------|-----|---------|
| 10.2      | 93.4      | ... | 0       |
| 888.1     | 0.2       | ... | 1       |



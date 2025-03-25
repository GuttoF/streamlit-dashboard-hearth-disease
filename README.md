# Heart Disease Analysis Dashboard

## 📊 Overview

This project provides an interactive dashboard for analyzing heart disease risk factors using processed clinical data. The dashboard is built with Streamlit and leverages enhanced heart disease data stored in DuckDB.

## 🛠️ Project Structure

```bash
streamlit-dashboard-hearth-disease/

├── LICENSE
├── README.md
├── data
│   ├── interim
│   │   └── db.db
│   ├── processed
│   │   └── db_processed.db
│   └── raw
│       └── heart.csv
├── notebooks
│   └── analysis.ipynb
├── pyproject.toml
├── src
│   └── main.py
├── utils
│   ├── __init__.py
│   ├── csv_to_db.py
│   ├── data_info.py
│   └── process_data.py
└── uv.lock
```

## 🔍 Data Processing

The data goes through an enhancement pipeline before being used in the dashboard:

1. **Source**: Original clinical data in `data/interim/db.db`
2. **Processing**:
   - Creation of derived features (risk scores, categories)
3. **Output**: Enhanced dataset in `data/processed/db_processed.db`, containing:
   - **14** original clinical features
   - **11** newly engineered features

### 🔑 Key Enhanced Features

- Cardiovascular risk classification
- Age groups
- Blood pressure categorization
- BMI estimation
- Activity level proxies

## 🚀 Streamlit Dashboard Features

### 📊 Planned Visualizations:

- **Demographic Overview**
  - Age distribution by heart disease status
  - Gender risk comparisons
  - Cardiovascular risk categories
- **Clinical Metrics**
  - Interactive correlation matrix
  - Blood pressure vs cholesterol trends
  - Heart rate anomaly analysis
- **Risk Analysis**
  - Custom risk score calculator
  - Feature importance visualization
  - Comparative risk profiles

### 🎛️ Interactive Elements

✅ Filters by age group, gender, and risk factors  
✅ Dynamic chart updates  
✅ Exportable reports and visualizations  
✅ Patient case studies drill-down  

## 🛠️ Setup & Usage

### 🚀 Run the dashboard

```bash
streamlit run src/dashboard.py
```

Access the interface at: [http://localhost:8501](http://localhost:8501)

## 📈 Data Flow

1. **Download** 🔽
2. **Processing** ⚙️
3. **Raw Data** 📂
4. **Enhanced Features Generation** 📊
5. **Interactive Visualizations** 📈
6. **Risk Insights** 💡

## 📅 Next Steps

- 📄 Create PDF report generation
- 🌍 Add multi-language support

⚠ **Note:** This dashboard is for educational purposes only. It is not intended for clinical or medical use.

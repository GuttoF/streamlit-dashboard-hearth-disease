# Heart Disease Analysis Dashboard

## 📊 Overview

This project provides an interactive dashboard for analyzing heart disease risk factors using processed clinical data. The dashboard is built with Streamlit and leverages enhanced heart disease data stored in DuckDB.

## 🛠️ Project Structure

```bash
streamlit-dashboard-hearth-disease/
├── Dockerfile
├── Dockerfile.dev
├── LICENSE
├── README.md
├── ansible
│   └── playbook.yml
├── data
│   ├── interim
│   │   └── db.db
│   ├── processed
│   │   └── db_processed.db
│   └── raw
│       └── heart.csv
├── deploy.sh
├── docker-compose.yml
├── main.tf
├── notebooks
│   └── analysis.ipynb
├── pyproject.toml
├── requirements.txt
├── src
│   ├── dashboard
│   │   └── components
│   │       ├── __init__.py
│   │       ├── filters.py
│   │       ├── plots.py
│   │       └── utils.py
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

### 📊 Planned Visualizations

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
streamlit run src/main.py
```

Access the interface at: [http://localhost:8501](http://localhost:8501)

## 📈 Data Flow

1. **Download** 🔽
2. **Processing** ⚙️
3. **Raw Data** 📂
4. **Enhanced Features Generation** 📊
5. **Interactive Visualizations** 📈
6. **Risk Insights** 💡

## Objective: Transform Data into Precise Clinical Decisions

### 1. Introduction: The Power of Visual Analysis

"Imagine being able to identify high-risk cardiac patients in seconds, with charts that speak the language of medicine. Our dashboard doesn’t just display numbers – it uncovers hidden patterns in your data, helping you save lives through proactive prevention."

### 2. Current Problem

**Challenges you face today:**

❌ Confusing and static spreadsheets
❌ Difficulty correlating multiple risk factors
❌ Time wasted on manual analyses

**Solution:**

✅ Interactive dashboard that updates in real time
✅ Intuitive visualization of 6 complementary charts
✅ Clinical filters for personalized analyses

### 3. Chart Demonstration

#### Chart 1: Age Risk Map

- **What it does:** Shows the distribution of diagnoses by age
- **Differential:** Instant color coding (blue = healthy, red = at risk)
- **Practical use:** Identify if patients aged 40-60 are your highest-risk population

#### Chart 2: Blood Pressure-Cholesterol Correlation

- **What it does:** Reveals the relationship between two key indicators
- **Differential:** Trendline predicting combined risk
- **Practical use:** Alert when a patient has both indicators elevated simultaneously

#### Chart 3: Gender Analysis

- **What it does:** Compares incidence between men and women
- **Differential:** Shows if the difference is statistically significant
- **Practical use:** Adapt preventive campaigns by gender

#### Chart 4: Factor Heatmap

- **What it does:** Measures how 12 clinical variables influence each other
- **Differential:** Warm colors = dangerous correlations
- **Practical use:** Discover that "diabetes + sedentary lifestyle" has a greater impact than each individually

#### Chart 5: Cardiac Performance by Symptom

- **What it does:** Compares heart rate across different types of pain
- **Differential:** Boxplots highlight outliers (severe cases)
- **Practical use:** Prioritize patients with atypical pain + irregular heartbeats

#### Chart 6: Control Panel

- **What it does:** Summarizes the most critical KPIs
- **Differential:** Real-time updates during consultations
- **Practical use:** Track metrics like "Average Cholesterol" and "% at Risk" per shift

### 4. Exclusive Benefits

**For your clinic:**

🔄 Reduction in analysis time
💾 Integration with existing systems (spreadsheets, electronic medical records)

🌐 **Accessibility:**

- Responsive (computer, tablet, or mobile)

⚠ **Note:** This dashboard is for educational purposes only. It is not intended for clinical or medical use.

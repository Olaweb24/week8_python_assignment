# CORD-19 Data Explorer

## Overview
This project explores the **CORD-19 dataset**, focusing on COVID-19 research papers. The goal is to practice basic data analysis, visualization, and create a simple **interactive Streamlit application**.

**Dataset:** `metadata.csv` (CORD-19 research papers)  
**Key columns used:** `title`, `abstract`, `publish_time`, `journal`, `authors`, `source_x`  

---

## Key Findings

1. **Publication Trend Over Time**
   - Most COVID-19 research papers were published in **2020 and 2021**.
   - The dataset shows a rapid increase in publications during the pandemic peak.

2. **Top Journals**
   - The top journals publishing COVID-19 research include:
     - *Journal A*
     - *Journal B*
     - *Journal C*
   - These journals have the highest number of papers in the dataset.

3. **Common Words in Titles**
   - Frequent words include: **COVID**, **vaccine**, **pandemic**, **SARS-CoV-2**, **infection**.
   - A word cloud visualization shows the prominence of these terms.

4. **Source Distribution**
   - Papers come from multiple sources (arXiv, bioRxiv, medRxiv, PMC), showing a wide range of open-access COVID-19 research.

---

## Visualizations Included

1. **Bar Chart of Papers by Year**
   - Shows the number of papers published each year from 2019–2022.

2. **Top 10 Journals**
   - Bar chart showing the journals with the highest publication counts.

3. **Word Cloud of Titles**
   - Visualizes the most frequent words in paper titles.

---

## Streamlit App Features

- **Interactive year filter slider**: Filter papers by publication year.  
- **Data table view**: Displays the first 10 rows of filtered data.  
- **Visualizations**: Dynamic charts for papers per year, top journals, and a word cloud for titles.

**Run the app:**
```bash
.\streamlit.exe run streamlit_app/app.py

Frameworks_Assignment/
├── data/
│   └── metadata.csv
├── streamlit_app/
│   └── app.py
├── notebooks/
│   └── exploration.ipynb
└── README.md

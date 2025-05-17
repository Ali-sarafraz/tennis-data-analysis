# 🎾 Tennis Data Exploration and Analysis

This project presents a comprehensive exploration of professional tennis data, with a focus on player demographics, performance metrics, match statistics, surface types, and betting behaviors. The objective is to generate insights that are valuable to fans, analysts, and sports professionals by analyzing the structure and dynamics of modern tennis.

---

## 📂 Project Structure

- 📓 `analysis.ipynb` — Main notebook for data exploration, cleaning, and visualization  
- 📊 `report.pptx` — Summary presentation of findings and visuals  
- 🛠 `make-dataset.py` — Script for transforming raw parquet data into clean CSV format  
- 📁 `tennis_data/` — Contains:
  - `csv-file/`: Cleaned datasets  
  - `raw/`: Original raw data in parquet format  
- 📄 `requirements.txt` — List of required Python packages

---

## 🎯 Objectives

- Ingest and clean raw tennis match data  
- Analyze player profiles and demographic trends  
- Study match-level metrics (duration, sets, breaks, etc.)  
- Evaluate tournament conditions (surface, geography)  
- Examine patterns in betting markets and outcomes  

---

## 🛠 Technologies & Libraries

- **Python**: Main programming language (via Jupyter Notebook)  
- **pandas**, **numpy**: Data manipulation  
- **matplotlib**, **seaborn**: Visualizations  
- **scipy**: Statistical analysis  

---

## 📊 Key Insights

### 👤 Player Demographics

- Total players: **596**  
- Handedness:
  - Right-handed: 244 (88.4%)  
  - Left-handed: 32 (11.6%)  
  - Ratio: ~7.6 right-handed to 1 left-handed

### 📐 Height vs. Ranking

- Spearman correlation: **p-value = 0.164**  
- Conclusion: No statistically significant correlation between player height and ATP ranking

### 🏆 Player Performance Highlights

- Most match wins:  
  - Milushev, Panaras Adam, Kalina Vit (each with 3 wins)  
- Top-10 opponents:  
  - Dimitrov G. has highest win rate (2 wins vs. top-10 ranked players)

### 🆕 Notable Recent Professionals (Turned Pro in 2019)

- Musetti L. — Rank: 27  
- Davidovich Fokina A. — Rank: 26  
- Cozbinov A. — Rank: 543 (only one with a recorded win)

### 🏁 Tournament Outcomes

- Total tournaments analyzed: **55**  
- Winners found in: **22 tournaments**  
- Missing winner data in: **33 tournaments** (potential for enrichment)

---

## ⏱️ Match Statistics

- Longest match: ~3h 34m (12,835 seconds)  
  - Weis Alexander vs. Domingues Joao  
- Average match duration: ~1h 40m (6,023 seconds)  
- Average sets per match: 2.33 (range: 1–3)  
- Breaks of serve:
  - Mean: 7  
  - Std Dev: 3  
  - 68% of matches had 4–10 breaks  

---

## 🌍 Country-Level Insights

- Total countries represented: **71**

### 👥 Top Countries by Player Count (Top 100)

1. Czech Republic — 9  
2. USA — 8  
3. Russia — 6  

### 📍 Countries with Most Matches Hosted

1. France — 79  
2. Tunisia — 79  
3. Argentina — 75  

### 🏟️ Countries with Most Stadiums

1. Argentina — 12  
2. China — 11  
3. Tunisia — 9  

---

## 🧱 Surface and Court Trends

- Hardcourt (Outdoor): **336** tournaments  
- Red Clay: **323** tournaments  
- Hardcourt (Indoor): **84** tournaments  

➡️ Outdoor hardcourts dominate, followed closely by red clay.

---

## 🎰 Betting Analysis

- Matches with bets: **315**  
- Avg. bets per match: **2.7**  
- Most frequent: **2 bets per match**

### 🔢 Bet Type Distribution

- Full-Time Result: 630  
- First Set Winner: 110  
- Total Games Won: 108  

### 💡 Betting Risk Insights

- Approx. 50% risk across bet types, suggesting a relatively efficient betting market  
- Full-time result bets are the most common  
- Set/game-specific bets are less frequent but present

---

## 📈 Notable Visualizations

- Player height vs. ATP ranking (scatter)  
- Breaks of serve per match (histogram)  
- Match game count comparisons (box plot by gender)  
- Double faults by gender (box plot)  
- Country comparisons (bar charts: players, matches, stadiums)  
- Court surface frequency (bar chart)  
- Bet type proportions (pie chart)

---

## 🚀 Getting Started

1. Clone the repository:

   ```bash
   git clone <https://github.com/Ali-sarafraz/tennis-data-analysis.git>
   cd tennis-data-analysis

2. install dependencies:
  
   ```bash
   pip install -r requirements.txt
3. Launch Jupyter Notebook:
   
   ```bash
   jupyter notebook analysis.ipynb

---

## 📬 Contact
For questions or collaboration inquiries, please open an issue or contact the project maintainer.
 
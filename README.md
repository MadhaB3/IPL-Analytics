# 🏏 IPL Cricket Analytics Project
### Player Performance & Team Strategy Analysis (2008–2025)

![Python](https://img.shields.io/badge/Python-3.12-blue)
![SQL](https://img.shields.io/badge/SQL-SQLite-green)
![PowerBI](https://img.shields.io/badge/PowerBI-Dashboard-yellow)

---

## 📌 Project Overview
A comprehensive end-to-end data analysis of 17 seasons 
of IPL cricket covering 278,205 ball-by-ball records 
across 1,169 matches from 2008 to 2025.

This project demonstrates the complete data analyst workflow:
Data Collection → Cleaning → SQL Database → EDA → 
Visualization → Storytelling Report

---

## 🎯 Problem Statement
Which batting and bowling combinations give IPL teams 
the highest win probability, and which undervalued 
players should franchises target in the next auction?

---

## 📊 Key Findings
| Finding | Insight |
|---|---|
| Scoring Rate | Grew 15% from 1.33 to 1.53 runs/ball |
| Top Batter | Virat Kohli — 8,661 runs all time |
| Top Bowler | YS Chahal — 221 wickets all time |
| Best Economy | SP Narine — 6.80 runs per over |
| Best Venue | Eden Gardens — 9.43 runs per over |
| Death Over King | AB de Villiers — 225 SR in overs 16-20 |

---

## 🗂️ Project Structure
```
ipl-analytics/
├── data/
│   └── processed/      ← Cleaned datasets & CSV exports
├── sql/
│   └── load_data.py    ← Data cleaning & SQLite loader
├── notebooks/
│   └── 01_eda.ipynb    ← Full EDA with 6 analysis sections
├── dashboard/
│   └── IPL_Dashboard.pbix  ← Power BI dashboard
├── report/
│   └── IPL_Analysis_Report.pdf  ← Full analysis report
└── README.md
```

---

## 🔧 Tech Stack
| Tool | Purpose |
|---|---|
| Python (pandas) | Data cleaning & manipulation |
| Python (matplotlib, seaborn) | Data visualization |
| SQLite | Database & SQL queries |
| Power BI | Interactive dashboard |
| Jupyter Notebook | EDA & analysis |

---

## 📈 Analysis Sections
1. **Season Overview** — IPL growth trends 2008-2025
2. **Top Batsmen** — All time run scorers & strike rates
3. **Top Bowlers** — All time wicket takers & economy rates
4. **Team Performance** — Team dominance across seasons
5. **Death Over Analysis** — Best finishers & death bowlers
6. **Venue Intelligence** — Batting vs bowling friendly grounds

---

## 🚀 How to Run
1. Clone the repository:
```
git clone https://github.com/[YOUR USERNAME]/ipl-analytics
```
2. Install dependencies:
```
pip install -r requirements.txt
```
3. Run data loader:
```
python sql/load_data.py
```
4. Open notebook:
```
jupyter notebook notebooks/01_eda.ipynb
```

---

## 📸 Dashboard Preview
[Add screenshot of your Power BI dashboard here]

---

## 📄 Report
Full analysis report available in `report/IPL_Analysis_Report.pdf`

---

## 🙋 About Me
Built by **Madhav Bhatnagar** as a data analytics 
capstone project.

Connect with me on LinkedIn: [YOUR LINKEDIN URL]
```

---

## ✅ FINAL CHECKLIST before posting:

| Task | Status |
|---|---|
| GitHub repo is public | ✅ Check settings |
| README is updated | ✅ Paste above content |
| PDF report is uploaded | ✅ In report/ folder |
| Power BI file uploaded | ✅ In dashboard/ folder |
| LinkedIn post ready | ✅ Copy above |
| 4 images attached to post | ✅ From report/ folder |
| GitHub link added to post | ✅ Paste your link |
| Posted during IPL match time | ✅ Tonight! |

---

## 💡 One Last Tip

After you post — go to the comments and add:
```
For anyone interested — full code and analysis 
is available on my GitHub. Happy to answer any 
questions about the methodology! 🙌

# CA - Artificial Intelligence & Machine Learning Laboratory Coursework

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Prolog](https://img.shields.io/badge/Prolog-SWI--Prolog-orange.svg)](https://www.swi-prolog.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Completed-success.svg)]()

> **Course:** Artificial Intelligence & Machine Learning (Continuous Assessment / Practical Lab)  
> **Student:** Shruti Siddheshwar Thorat  
> **PRN:** 202401040053  
> **Roll No:** 16  
> **Batch:** A1  

---

## 📖 Repository Overview

This repository contains the laboratory assignments and practical implementations completed as part of the **Continuous Assessment (CA)** practical coursework for Artificial Intelligence & Machine Learning:

1. **[Practical 1.1: Intelligent Agent - Simple Reflex Agent](./Practical_1.1_Simple_Reflex_Agent/)**
   - Design and simulation of an autonomous **Smart Beach Cleaning Vacuum Cleaner**.
   - Implements condition-action reflex logic across 4 environmental percepts (`Plastic`, `Seaweed`, `Sharp Object`, `Clean`).
   - Handles hazards via avoidance heuristics and calculates an cumulative performance evaluation score.

2. **[Practical 1.2: Reasoning in Knowledge-Based Expert System](./Practical_1.2_Expert_System_Prolog/)**
   - Rule-based **Food Recommendation Expert System (`FoodieBot`)** authored in Prolog.
   - Declarative knowledge base encoding foods, flavors, meal types, and dietary preferences.
   - Dynamic contextual recommendations influenced by user mood and local weather conditions.

3. **[Practical 3: House Price Prediction Using Regression Models](./Practical_3_Regression_House_Price/)**
   - Comparative benchmark across **Simple Linear**, **Multiple Linear**, and **Polynomial Regression** models.
   - Features side-by-side implementations using **Scikit-learn** vs **Manual Mathematical Formulations** (Ordinary Least Squares and Gradient Descent).
   - Rigorous evaluation metrics ($\text{MSE}, \text{RMSE}, \text{MAE}, R^2$) with visualizations and convergence graphs.

---

## 📂 Repository Structure

```
CA/
├── Practical_1.1_Simple_Reflex_Agent/
│   ├── beach_cleaning_agent.py               # Autonomous reflex agent simulation
│   ├── Vaccumcleanerassignment.pdf           # Full academic report document
│   └── README.md                             # Flowchart, algorithm & execution documentation
├── Practical_1.2_Expert_System_Prolog/
│   ├── foodiebot.pl                          # Prolog knowledge base & inference engine
│   ├── prologassignment.pdf                  # Academic report document
│   └── README.md                             # Knowledge base rules & query guide
├── Practical_3_Regression_House_Price/
│   ├── Practical_3_House_Price_Prediction.ipynb # Executable Jupyter / Colab notebook
│   ├── house_price_prediction.py             # Standalone Python script
│   ├── Housing.csv                           # Housing dataset
│   ├── Regression_Assignment_Report.pdf      # Detailed practical report
│   └── README.md                             # Mathematical derivation & benchmarking
├── .gitignore                                # Standard exclusion rules
├── requirements.txt                          # Python dependencies
└── README.md                                 # Main laboratory guide
```

---

## 🛠️ Technologies Used

| Domain | Technologies & Libraries |
|---|---|
| **Intelligent Agents & ML** | Python 3.8+, Scikit-learn, Pandas, NumPy, Matplotlib |
| **Logic Programming** | Prolog (SWI-Prolog) |
| **Interactive Environments** | Jupyter Notebook, Google Colab, CLI |
| **Version Control** | Git, GitHub |

---

## 🚀 Key Highlights & Results

- **Simple Reflex Agent:** Successfully models autonomous cleaning decisions with hazard avoidance and quantitative score accumulation.
- **Prolog Inference:** Natural recursive query resolution with fallback handling for unparsed queries.
- **Regression Equivalence:** Manual math derivations produced exact identical results to Scikit-learn:
  - *Multiple Linear Regression:* Achieved top predictive accuracy ($R^2 \approx 0.5464$, $\text{RMSE} \approx 1.514 \times 10^6$).
  - Gradient descent converged stably within $10,000$ epochs at $\alpha = 0.03$.

---

## 💻 Installation & Execution Instructions

### Prerequisites
- Python 3.8 or higher.
- [SWI-Prolog](https://www.swi-prolog.org/) (for Practical 1.2).

### 1. Clone the Repository
```bash
git clone https://github.com/shruti-2506/CA.git
cd CA
```

### 2. Set Up Virtual Environment & Dependencies
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

pip install -r requirements.txt
```

### 3. Running Practicals
- **Run Practical 1.1 (Beach Cleaning Agent):**
  ```bash
  cd Practical_1.1_Simple_Reflex_Agent
  python beach_cleaning_agent.py
  ```

- **Run Practical 1.2 (Prolog FoodieBot):**
  ```bash
  cd Practical_1.2_Expert_System_Prolog
  swipl foodiebot.pl
  # In Prolog prompt:
  ?- foodiebot.
  ```

- **Run Practical 3 (Regression Models):**
  ```bash
  cd Practical_3_Regression_House_Price
  python house_price_prediction.py
  ```
  *(Or open `Practical_3_House_Price_Prediction.ipynb` in Jupyter Notebook / Google Colab)*

---

## 📄 License
This repository is authored for academic assessment and learning purposes.

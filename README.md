# 📊 Data Cleaning and Visualization Workflow

---

## 1. Project Title
Data Cleaning and Visualization Workflow for Experimental Dataset

---

## 2. Project Structure

phd-research-workflow/
│
├── data/
│   ├── sample_data.csv
│   └── cleaned_data.csv
│
├── src/
│   ├── clean_data.py
│   └── visualize_data.py
│
├── results/
│   ├── score_plot.png
│   └── temperature_humidity_plot.png
│
├── docs/
│   └── analysis_notes.md
│
├── README.md
└── .gitignore

---

## 3. Files and Folders Used

- data/sample_data.csv: Raw dataset  
- data/cleaned_data.csv: Cleaned dataset  
- src/clean_data.py: Data preprocessing script  
- src/visualize_data.py: Visualization script  
- results/: Stores generated plots  
- docs/analysis_notes.md: Analysis documentation  

---

## 4. How to Run the Project

### Step 1: Clean data
python src/clean_data.py

### Step 2: Visualize data
python src/visualize_data.py

---

## 5. Expected Outputs

- data/cleaned_data.csv  
- results/score_plot.png  
- results/temperature_humidity_plot.png  

---

## 6. Assumptions

- Missing values are filled using mean imputation  
- Dataset structure remains consistent  
- Median method can be used in future  

---

## 7. Future Scope

- Improve data cleaning techniques  
- Add outlier handling  
- Enhance visualization  
- Automate workflow  

---
# MAT2007 - Billionaire Statistics Project

Research Question: How do age distributions of male and female billionaires compare, and does this vary across countries?

# Dataset

This project uses the publicly available Billionaire Statistics Dataset (2023), containing 2,640 billionaire records. 
Source: https://www.kaggle.com/datasets/nelgiriyewithana/billionaires-statistics-dataset/

The analysis uses age, gender and country of citizenship. Rows with missing values in the relevant variables were removed using pandas dropna().

# Software Requirements
- Python 3
- pandas
- NumPy
- Matplotlib
- SciPy

Install dependencies using: python3 -m pip install pandas numpy matplotlib scipy

# How to Run

1. Download the repository
2. Keep the python script and CSV dataset in the same folder
3. Open the folder in Visual Studio Code
4. Run the following command in the terminal.

python3 BillionairesFinalCode.py

The program displays summary statistics and generates three figures

# Analysis

- Age distributions by gender, including mean age, skewness and excess kurtosis.
- Cumulative age distributions with approximate uncertainty bands
- Average age across five countries with the most billionaire records, with standard error bars.

# Main Findings

Male and female billionaires have broadly similar age distributions, although females are slightly younger on average. Age differences between genders vary across countries.

# Project Files
- BillionairesFinalCode.py - python analysis script
- Billionaires Statistics Dataset copy.csv - Dataset
- LaTeX.MAT2007.pdf - Final two page report
- LaTeX.MAT2007.zip - LaTeX sources files

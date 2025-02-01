# Python Challenge

## Summary
This repository contains two Python-based data analysis challenges: **PyBank** and **PyPoll**. The **PyBank** script analyzes financial records to determine key financial metrics, while the **PyPoll** script processes election data to count votes and determine the winning candidate. Both scripts read data from CSV files, perform necessary calculations, and output results both to the terminal and text files.

## Repository Structure
```
python-challenge/
│
├── PyBank/
│   ├── Resources/
│   │   ├── budget_data.csv
│   ├── analysis/
│   │   ├── financial_analysis.txt
│   ├── main.py
│
├── PyPoll/
│   ├── Resources/
│   │   ├── election_data.csv
│   ├── analysis/
│   │   ├── election_results.txt
│   ├── main.py
```

## PyBank: Financial Analysis
### Objective
Analyze a company's financial records from `budget_data.csv` and calculate key financial metrics.

### Tasks
- Count the total number of months in the dataset.
- Compute the net total amount of "Profit/Losses" over the period.
- Determine the average change in "Profit/Losses" across the dataset.
- Identify the greatest increase and decrease in profits (including the corresponding dates).
- Print the analysis results to the terminal and export them to a text file.

## PyPoll: Election Analysis
### Objective
Automate vote counting using `election_data.csv` to determine election results.

### Tasks
- Count the total number of votes cast.
- Generate a complete list of candidates who received votes.
- Calculate the percentage and total number of votes each candidate won.
- Determine the winner based on the popular vote.
- Print the analysis results to the terminal and export them to a text file.

## Installation and Usage
1. Clone this repository:
   ```sh
   git clone https://github.com/your-username/python-challenge.git
   ```
2. Navigate to the project directory:
   ```sh
   cd python-challenge
   ```
3. Run the scripts:
   - PyBank:
     ```sh
     python PyBank/main.py
     ```
   - PyPoll:
     ```sh
     python PyPoll/main.py
     ```
4. Check the `analysis/` folder for the exported text results.

## Dependencies
- Python 3.x
- Pandas (optional but recommended for data analysis)




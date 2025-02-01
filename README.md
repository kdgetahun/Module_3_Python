# Module_3_Python
PyBank and PyPoll Scripts
-
Python Challenge

Overview

This project consists of two Python challenges—PyBank and PyPoll—which involve analyzing financial records and election data, respectively. The scripts utilize Python to automate data processing, replacing the need for manual calculations in Excel.

Repository Structure

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

PyBank: Financial Analysis

Objective

Analyze a company's financial records from budget_data.csv and calculate key financial metrics.

Tasks

Count the total number of months in the dataset.

Compute the net total amount of "Profit/Losses" over the period.

Determine the average change in "Profit/Losses" across the dataset.

Identify the greatest increase and decrease in profits (including the corresponding dates).

Print the analysis results to the terminal and export them to a text file.

Sample Output

Financial Analysis
----------------------------
Total Months: 86
Total: $22564198
Average Change: $-8311.11
Greatest Increase in Profits: Aug-16 ($1862002)
Greatest Decrease in Profits: Feb-14 ($-1825558)

PyPoll: Election Analysis

Objective

Automate vote counting using election_data.csv to determine election results.

Tasks

Count the total number of votes cast.

Generate a complete list of candidates who received votes.

Calculate the percentage and total number of votes each candidate won.

Determine the winner based on the popular vote.

Print the analysis results to the terminal and export them to a text file.

Sample Output

Election Results
-------------------------
Total Votes: 369711
-------------------------
Charles Casper Stockham: 23.049% (85213)
Diana DeGette: 73.812% (272892)
Raymon Anthony Doane: 3.139% (11606)
-------------------------
Winner: Diana DeGette
-------------------------

Installation and Usage

Clone this repository:

git clone https://github.com/your-username/python-challenge.git

Navigate to the project directory:

cd python-challenge

Run the scripts:

PyBank:

python PyBank/main.py

PyPoll:

python PyPoll/main.py

Check the analysis/ folder for the exported text results.

Dependencies

Python 3.x

Pandas (optional but recommended for data analysis)

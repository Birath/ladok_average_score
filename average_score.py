import tabula
import pandas as pd

import sys
if len(sys.argv) != 2:
    print("Pass the pdf of results")

amount = 0
total_score = 0
df = tabula.read_pdf(sys.argv[1], pages='all', silent=True)

for page in df:
    scope_column = "Scope" if "Completed courses Scope" not in page.columns else "Completed courses Scope"
    for row in page.itertuples(False, None):
        index = 0 if pd.isna(row[1]) else 1
        if pd.isna(row[2]):
            continue
        if not "(" in row[index] and row[2] != "G" and row[2] in ["3", "4", "5"]:
            amount += 1
            total_score += int(row[2])
            

print("Total Grade", total_score)
print("Courses", amount)
print("Average Score:", total_score/amount)

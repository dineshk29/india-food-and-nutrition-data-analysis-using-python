import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
a = {"NID": pd.Series([101, 102, 103, 104, 105, 106, 107, 108, 109, 110]),
     "NUTRITION NAME": pd.Series(["CALORIES", "TOTAL FAT", "SATURATED FAT", "TRANS FAT", "CHOLESTROL", "SODIUM", "CARBOHYDRATES", "FIBER", "SUGAR", "PROTEIN"]),
     "FISH CURRY": pd.Series([290, 15, 5,0, 0.085, 0.9, 10, 3, 5, 15]),
     "CHICKEN BIRYANI": pd.Series([380, 12, 4, 0, 0.9,0.98, 50, 2, 5, 8]),
     "TANDOORI CHICKEN": pd.Series([260, 12, 3, 0, 0.1, 0.78, 3, 1, 1, 15]),
     "PALAK PANNER": pd.Series([260, 20, 2, 0, 0.0045, 0.73, 10, 4, 5, 12]),
     "DAL": pd.Series([330, 15, 5,0, 0.04, 0.74, 35, 8, 4, 14]),
     "ALOO GOBI": pd.Series([120, 8, 1, 0, 0, 0.46, 10, 4, 3,3])}
b = pd.DataFrame(a)
print(" INDIAN FOODS AND NUTRITION ANALYSIS    ")
print()
print(b)
print(" BEFORE COLUMN INSERTION    ")
print()
print(b)
print("    AFTER COLUMN INSERTION    ")
print()
b['TOTAL']=b['FISH CURRY']+b['DAL']
print(b)
print(" BEFORE ROW INSERTION    ")
print()
print(b)
print("     AFTER ROW INSEERTION  ")
print()
new_row = pd.DataFrame(
    {
        "NID": [111],
        "NUTRITION NAME": ["IRON"],
        "FISH CURRY": [15],
        "CHICKEN BIRYANI": [20],
        "TANDOORI CHICKEN": [10],
        "PALAK PANNER": [15],
        "DAL": [20],
        "ALOO GOBI": [6], })
b = pd.concat([b, new_row], ignore_index=True)
print(b)
print("     READ COLUMN VALUES   ")
print()
print(b['FISH CURRY'])
print(b)
print("      READ ROW  VALUES   ")
print(b.loc[5])
print("    READ ROW VALUES WITH INDEX   ")
print(b.loc[5][6])
print("    BEFORE COLUMN UPDATE ")
print(b)
print("      AFTER  COLUMN UPDATE    ")
b['ALOO GOBI'][9]=20000
print()
print(b)
print("     AFTER ROW UPDATE    ")
print()
b.loc[3,"NUTRITION NAME"]="fattty"
print(b)
print("   AFTER COLUMN DELETE   ")
print()
b.pop('TOTAL')
print(b)
print("    AFTER ROW DELETE   ")
print()
n=b.drop(3)
print(n)
print()
print("    DATA PREPROCESSING  ")
print("  DATA COLLECTION ")
a = {"NID": pd.Series([101, 102, 103, 104, 105, 106, 107, 108, 109, 110]),
     "NUTRITION NAME": pd.Series(["CALORIES", "TOTAL FAT", "SATURATED FAT", "TRANS FAT", "CHOLESTROL", "SODIUM", "CARBOHYDRATES", "FIBER", "SUGAR", "PROTEIN"]),
     "FISH CURRY": pd.Series([290, 15, 5,0, 0.085, 0.9, 10, 3, 5, 15]),
     "CHICKEN BIRYANI": pd.Series([380, 12, 4, 0, 0.9,0.98, 50, 2, 5, 8]),
     "TANDOORI CHICKEN": pd.Series([260, 12, 3, 0, np.nan, 0.78, 3, 1, 1, 15]),
     "PALAK PANNER": pd.Series([260, np.nan, 2, 0, 0.0045, 0.73, 10, 4, 5, 12]),
     "DAL": pd.Series([330, 15, 5,0, 0.04, 0.74, 35, 8, 4, 14]),
     "ALOO GOBI": pd.Series([120, 8, 1, 0, 0, 0.46, 10, np.nan, 3,3])}
b = pd.DataFrame(a)

print("       DATA  CLEANING  ")
print()
print("     BY USING ISNULL() ")
print()
x=b.isnull()
print(x)
print()
print("     BY USING NOTNULL()   ")
x=b.notnull()
print(x)
print("    DATA INTERGRATION  ")
print()
print("    BY USING bfill()  ")
x=b.fillna(method="bfill")
print(x)
print()
print("     BY USING pad()   ")
print()
x=b.fillna(method="pad")
print(x)
print()
print("      BY USING fillna()  ")
x=b.fillna(270)
print(x)
plt.scatter(b['NID'],b['DAL'])
plt.xlabel("NUTRION IDS'S")
plt.ylabel("N")
plt.colorbar()
plt.title("Relation B/W SID & Sub1")
plt.legend("Scale in 1 mm")
plt.show()
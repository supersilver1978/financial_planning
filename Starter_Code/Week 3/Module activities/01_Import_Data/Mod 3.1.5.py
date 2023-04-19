import pandas as pd

from pathlib import Path
csvpath = Path("C:\Users\super\Desktop\FinTech-Workspace\Week 3\01_Import_Data\sales.csv")
sales_dataframe = pd.read.csv(csvpath)
sales_dataframe.head()

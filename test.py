
import pandas as pd
data_csv = pd.read_csv("C:\\Users\\ADMIN\\Desktop\\df.csv")    
print(data_csv.isnull().sum())
import pandas as pd
import os

data = []

directories = ["./combined_data/"]

for directory in directories:
    for file in os.listdir(directory):
        print(file)
        if file.endswith(".csv"):
            year = file.split('_')[0]
            df = pd.read_csv(directory + file)
            print("Row count is: " + str(len(df)))
            print("Column count is: " + str(len(df.columns)))
            

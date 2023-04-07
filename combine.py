import pandas as pd
import os

data = []

directories = ["./data/advanced_stats/", "./data/shooting_opponent/", "./data/shooting_team/", "./data/total_opponent/", "./data/total_team/"]

for directory in directories:
    print("Getting files from directory " + directory)
    for file in os.listdir(directory):
        print("Reading from file " + file)
        if file.endswith(".csv"):
            year = file.split('_')[0]
            print("Relative file path is " + directory + file)
            df = pd.read_csv(directory + file)
            df['Year'] = int(year)
            data.append(df)
    all_data = pd.concat(data, ignore_index=True)
    last_slash_index = directory.rfind("/")
    second_last_slash_index = directory.rfind("/", 0, last_slash_index)
    substring = directory[second_last_slash_index+1:last_slash_index]
    new_excel_sheet = "./combined_data/" + substring + ".csv"
    all_data.to_csv(new_excel_sheet, index=False)
    data=[]

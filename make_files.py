import os
import csv

# Set the directory where you want to create the CSV files
directories = ["./data/advanced_stats/", "./data/shooting_opponent/", "./data/shooting_team/", "./data/total_opponent/", "./data/total_team/"]


# Loop over each year from 2001 to 2020
for directory in directories:
    for year in range(2001, 2021):
        # Create the filename for the CSV file
        filename = str(year) + '_advanced.csv'
        
        # Create the full path for the CSV file
        filepath = os.path.join(directory, filename)
        
        # Create the CSV file with headers
        with open(filepath, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Header 1', 'Header 2', 'Header 3'])
        
        # Print a message to confirm the CSV file was created
        print(f'Created CSV file: {filename}')

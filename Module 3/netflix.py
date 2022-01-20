# Modules
import os
import csv

#Read
# Prompt user for video lookup
video = input("What show or movie are you looking for? ")

# Set path for file
csvpath = os.path.join("..", "Resources", "netflix_ratings.csv")

# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    # Loop through looking for the video
    for row in csvreader:
        if row[0] == video:
            print(f"{row[0]} is rated {row[1]} with a rating of {row[5]}")
            
#WRITE
file_outpath = os.path.join("..", "output", "Employee_Data.txt")

#w:write, a:append
with open(file_outpath, "w") as textfile:
    employee_data = (
        
    )
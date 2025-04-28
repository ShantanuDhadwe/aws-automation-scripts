import csv

# Define the grade threshold
threshold = 80

# Read and analyze the CSV file
with open('students.csv', 'r') as file:
    reader = csv.DictReader(file)
    print(f"Students with grades above {threshold}:")
    for row in reader:
        if int(row['Grade']) > threshold:
            print(f"{row['Name']} (Grade: {row['Grade']})")

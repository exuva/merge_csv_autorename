import os
import csv
# import shutil

# Get the directory where the Python script is located
script_directory = os.path.dirname(__file__)

# Define the folder containing the CSV files
folder_path = os.path.join(script_directory, "data")

# Get a list of CSV files in the folder
csv_files = [f for f in os.listdir(folder_path) if f.endswith(".csv")]

# Find the file with the most columns (maximum header length)
max_columns_file = max(csv_files, key=lambda file_name: len(next(csv.reader(open(os.path.join(folder_path, file_name), "r", newline=""), delimiter=";"))))

# Read the header from the file with the most columns
with open(os.path.join(folder_path, max_columns_file), "r", newline="") as file:
    header_to_copy = next(csv.reader(file, delimiter=";"))


# Iterate through each CSV file and copy the header
for file_name in csv_files:
    file_path = os.path.join(folder_path, file_name)
    data = []

    with open(file_path, "r", newline="") as file:
        reader = csv.reader(file, delimiter=";")
        for row in reader:
            data.append(row)

    # Update the header in the current file
    original_header = data[0]
    data[0] = header_to_copy

    # Print the differences between the original header and the copied header
    differences = set(original_header) ^ set(header_to_copy)
    print(f"Processed: {file_name}")
    print("Differences:")
    print("+----------------+----------------+")
    print("| Original Header | Copied Header  |")
    print("+----------------+----------------+")

    for item in differences:
        original_present = "Yes" if item in original_header else "No"
        copied_present = "Yes" if item in header_to_copy else "No"
        print(f"| {item:<16}| {original_present:<16}| {copied_present:<16}|")

    print("+----------------+----------------+")

    # Print the position of each element in the header if it was not in the original header
    position_dict = {element: position for position, element in enumerate(header_to_copy, start=1)}
    for element in differences:
        if element in header_to_copy:
            position = position_dict[element]
            print(f"Element '{element}' is at position {position} in the header.")

    # Add a new column with the value "0" from the second row onwards at the specified position
    for i in range(1, len(data)):
        for element in differences:
            if element in header_to_copy:
                position = position_dict[element]
                data[i].insert(position - 1, "0")

    # Write the modified data back to the CSV file
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerows(data)
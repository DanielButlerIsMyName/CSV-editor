from csv_handling import read_csv_file, write_csv_file
from search_functions import first_row_contains_values, all_rows_containing_values

input_csv_file_path = input("File path to csv that should be searched: ")
export_csv_file_path = input("File path to csv that should be exported to: ")

input_values = input("Enter the values that should be searched for (comma-separated): ")
values = input_values.split(",")

for value in input_values: # optional: strip whitespaces and convert to lowercase
  values.append(value.strip())


input_csv_file_data = read_csv_file(input_csv_file_path)
export_csv_file_data = read_csv_file(export_csv_file_path)

found_rows = all_rows_containing_values(input_csv_file_data, values)
found_row = first_row_contains_values(input_csv_file_data, values)

print("Found row:")
print(found_row)

print("Found rows:")
for row in found_rows:
  write_csv_file(export_csv_file_path, row)
  print(row)
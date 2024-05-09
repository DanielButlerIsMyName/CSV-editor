from csv_handling import read_csv_file, write_csv_file
from search_functions import first_row_contains_values, all_rows_containing_values, rows_matching_regex

input_csv_file_path = input("File path to csv that should be searched: ")
export_csv_file_path = input("File path to csv that should be exported to: ")

regex_input = input("Enter the regex pattern that should be searched for: ")
regex = ".*" + regex_input + ".*"

input_csv_file_data = read_csv_file(input_csv_file_path)
export_csv_file_data = read_csv_file(export_csv_file_path)

found_rows = rows_matching_regex(input_csv_file_data, regex)

for row in found_rows:
  write_csv_file(export_csv_file_path, row)


import re


def first_row_contains_values(csv_data, values): # returns the first row that contains any of the values
  print("Searching for first row containing values...")
  for row in csv_data:
    for col in row:
      if col in values:
        return row
      
def all_rows_containing_values(csv_data, values): # returns all rows that contain any of the values
  print("Searching for rows containing values...")
  result = []
  for row in csv_data:
    for col in row:
      if col in values:
        result.append(row)
  return result

def rows_matching_regex(csv_data, pattern):
  print("Searching for rows matching regex pattern...")
  result = []
  for row in csv_data:
    for col in row:
      if re.search(pattern, col):
        result.append(row)
        break
  return result
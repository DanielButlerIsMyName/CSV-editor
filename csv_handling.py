import csv

def read_csv_file(file_path):
  print("Reading csv file...")
  with open(file_path, 'r') as file:
    csv_reader = csv.reader(file)
    rows = list(csv_reader)
    return rows
  
def write_csv_file(file_path, row):
  print("Writing to csv file...")
  with open(file_path, 'a', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(row)
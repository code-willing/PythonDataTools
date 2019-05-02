import sys
import argparse
import csv

parser = argparse.ArgumentParser(description='Verify number of columns in all rows match number of columns in header row')
parser.add_argument('-f', '--file', help="File to read from", required=True)
parser.add_argument('-d', '--delimiter', help="CSV Delimiter(defaults to ',')", default=',')
parser.add_argument('--no_header', help="Specify that CSV has no header", action='store_true')

args = parser.parse_args()

line_num = 1

with open(args.file, 'r') as input_file:
  header_row = input_file.readline().split(args.delimiter)
  header_cols = len(header_row)

  print("Number of Header Columns: " + str(header_cols))

  for line in input_file:
    line_num += 1
    line_values = line.split(args.delimiter)

    if len(line_values) != header_cols:
        print("Mismatched number of columns at line: " + str(line_num))
        print("Number of columns at line " + str(line_num) + ": " + str(len(line_values)) + '\n')

        if not args.no_header:
          print("Header:\n" + " | ".join(header_row))

        print("Mismatched row:\n" + " | ".join(line_values))
        exit()

print("File OK, Lines Read: " + str(line_num))

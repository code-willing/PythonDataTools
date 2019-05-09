''' Get the total value of a column '''

from __future__ import print_function

import csv
import sys, os
import argparse

parser = argparse.ArgumentParser(description='Get the total value of a column in a CSV file')
parser.add_argument('-f', '--file', help="File to read from", required=True)
parser.add_argument('-c', '--column', help="Column number to sum(starting with 1)", type=int)
parser.add_argument('-n', '--column_name', help="Column name to sum(Assumes header row exists)")
parser.add_argument('-d', '--delimiter', help="CSV Delimiter(defaults to ',')", default=',')
parser.add_argument('--has_header', help="Specify that CSV has a header", action='store_true')

args = parser.parse_args()

column_total = 0
lines_read = 0

##could probably replace this with pandas,
##but pandas is optional
with open(args.file, 'r') as input_file:
  if args.column_name is not None:
    reader = csv.DictReader((x.replace('\0', "") for x in input_file), delimiter=args.delimiter)
    for row in reader:
      lines_read += 1
      column_total += int(row[args.column_name])

  elif args.column is not None:
    reader = csv.reader((x.replace('\0', "") for x in input_file), delimiter=args.delimiter)

    ## skip header if it exists and we are looking for a column number
    if args.has_header:
      next(reader, None)

    for row in reader:
      lines_read += 1
      column_total += int(row[args.column - 1])

  else:
    print("You must specify either -c or -n.")
    parser.print_help()
    exit()

print("Lines read     : " + str(lines_read))
print("Total Sum      : " + str(column_total))

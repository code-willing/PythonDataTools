''' Get a subset of delimited columns from a data file '''

from __future__ import print_function

import sys
import argparse
import csv

parser = argparse.ArgumentParser(description='Get a columnwise subset of a CSV file')
parser.add_argument('-f', '--file', help="File to read from", required=True)
parser.add_argument('-c', '--columns', help="Column numbers to cut(starting with 1)")
parser.add_argument('-n', '--column_names', help="Column names to cut(Assumes header row exists)")
parser.add_argument('-d', '--delimiter', help="CSV Delimiter(defaults to ',')", default=',')
parser.add_argument('--skip_header', help="Skip header when cutting by number", action='store_true')

args = parser.parse_args()

##could probably replace this with pandas,
##but pandas is optional


with open(args.file, 'r') as input_file:
  if args.column_names is not None:
    print(args.delimiter.join(args.column_names.split(args.delimiter)) + ',')
    header_names = args.column_names.split(',')
    reader = csv.DictReader(input_file, delimiter=args.delimiter)

    ## there is a more pythonical way to do this
    ## probably some insane generator
    for row in reader:
      print(args.delimiter.join)
      for name in header_names:
        print(row[name] + args.delimiter, end='')
      print()

  elif args.columns is not None:
    indices = args.columns.split(',')
    reader = csv.reader(input_file, delimiter=args.delimiter)

    ## skip header if it exists and we are looking for a column number
    if args.skip_header:
      next(reader, None)
    for row in reader:
      for index in indices:
        print(row[int(index) - 1] + args.delimiter, end='')
      print()
  else:
    parser.print_help()
    exit()



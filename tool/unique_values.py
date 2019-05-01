import sys
import argparse
import csv

parser = argparse.ArgumentParser(description='Get the unique values in a column in a CSV file')
parser.add_argument('-f', '--file', help="File to read from", required=True)
parser.add_argument('-c', '--column', help="Column number to check(starting with 1)", type=int)
parser.add_argument('-n', '--column_name', help="Column name to check(Assumes header row exists)")
parser.add_argument('-d', '--delimiter', help="CSV Delimiter(defaults to ',')", default=',')
parser.add_argument('--has_header', help="Specify that CSV has no header", action='store_true')

args = parser.parse_args()

sym = set()

##could probably replace this with pandas,
##but pandas is optional
with open(args.file, 'r') as input_file:
  if args.column_name is not None:
    reader = csv.DictReader((x.replace('\0', "") for x in input_file), delimiter=args.delimiter)
    [sym.add(row[args.column_name]) for row in reader]

  elif args.column is not None:
    reader = csv.reader((x.replace('\0', "") for x in input_file), delimiter=args.delimiter)

    ## skip header if it exists and we are looking for a column number
    if args.has_header:
      next(reader, None)
  
    [sym.add(row[args.column - 1]) for row in reader]

  else:
    print("You must specify either -c or -n.")
    parser.print_help()
    exit()

print("Number of Unique Values in column: " + str(len(list(sym))))
print('[' + ','.join(sorted(list(sym))) + ']')

''' Check sort order by column'''

from __future__ import print_function

import csv
import sys, os
import argparse

parser = argparse.ArgumentParser(description='Check if a column in a delimited data file is sorted')
parser.add_argument('-f', '--file', help="File to read from", required=True)
parser.add_argument('-c', '--column', help="Column number to check(starting with 1)", type=int)
parser.add_argument('-n', '--column_name', help="Column name to check(Assumes header row exists)")
parser.add_argument('-d', '--delimiter', help="CSV Delimiter(defaults to ',')", default=',')
parser.add_argument('-o', '--order', help="Specify 'asc' or 'desc'(defaults to 'asc')", default='asc')
parser.add_argument('--has_header', help="Specify that CSV has a header", action='store_true')

args = parser.parse_args()

current_val = None
whole_curr_row = None
lines_read = 1

def argument_error(): 
  parser.print_help()
  exit()

def out_of_order(row_first, row_second, current_line, order):
  print("Not in " + order + " order:")
  print("Line " + str(current_line - 1) + ": " + args.delimiter.join(row_first))
  print("Line " + str(current_line) + ": " + args.delimiter.join(row_second))  
  exit()

with open(args.file, 'r') as input_file:
  if args.column_name is not None:
    reader = csv.DictReader((x.replace('\0', "") for x in input_file), delimiter=args.delimiter)

    row = next(reader)
    ## read value from first line as current then go to next line
    ## this is just to have an initial value
    current_val = row[args.column_name]
    whole_curr_row = row

    for csvrow in reader:
      lines_read += 1
      tmp_val = csvrow[args.column_name]

      if args.order == 'asc':
        if tmp_val < current_val:
          out_of_order(list(whole_curr_row.values()), list(csvrow.values()), lines_read, 'ascending')
      elif args.order == 'desc':
        if tmp_val > current_val:
          out_of_order(list(whole_curr_row.values()), list(csvrow.values()), lines_read, 'descending')
      else:
        argument_error()
      current_val = tmp_val
      whole_curr_row = csvrow

  elif args.column is not None:
    reader = csv.reader((x.replace('\0', "") for x in input_file), delimiter=args.delimiter)
    row = next(reader, None)

    ## skip header if it exists and we are looking for a column number
    if args.has_header:
      lines_read += 1
      row = next(reader, None)

    ## read value from first line as current then go to next line
    ## this is just to have an initial value
    current_val = row[args.column - 1]
    whole_curr_row = row

    for csvrow in reader:
      lines_read += 1
      tmp_val = csvrow[args.column - 1]

      if args.order == 'asc':
        if tmp_val < current_val:
          out_of_order(whole_curr_row, csvrow, lines_read, 'ascending')
      elif args.order == 'desc':
        if tmp_val > current_val:
          out_of_order(whole_curr_row, csvrow, lines_read, 'descending')
      else:
        argument_error()
      current_val = tmp_val
      whole_curr_row = csvrow

  else:
    print("You must specify either -c or -n.")
    argument_error()

print("Order OK\nLines Read: " + str(lines_read))

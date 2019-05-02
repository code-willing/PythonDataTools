# PythonDataTools

Python scripts for manipulating data files

## cut_columns.py

Get a column slice of a delimited data file

### Example Usage

#### Cutting a CSV file by column number

```
$ cat ../test/test_2.csv
column1,column2,column3,column4,
1,1,1,1,
2,1,1,1,
3,2,1,1,
4,3,2,1,
5,4,3,2,

$ python cut_columns.py -f ../test/test_2.csv -c 1,2
column1,column2,
1,1,
2,1,
3,2,
4,3,
5,4,
```

#### Cutting a CSV by column name

```
$ cat ../test/test_2.csv
column1,column2,column3,column4,
1,1,1,1,
2,1,1,1,
3,2,1,1,
4,3,2,1,
5,4,3,2,

$ python cut_columns.py -f ../test/test_2.csv -n column1, column2
column1,column2
1,1,
2,1,
3,2,
4,3,
5,4,
```

## sum_column.py

Get the total sum of a column in a delimited data file

## unique_values.py

Get the unique values from a column in a delimited data file

## verify_columns.py

Verfiy that all rows in delimited data have the same number of columns

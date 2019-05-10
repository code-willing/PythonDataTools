''' Not very robust testing suite '''

from __future__ import print_function

import sys
import subprocess

num_tests = 0.0
total_pass = 0.0

def assert_equals(first, second):
  if first == second: return True
  return False

def assert_not_equals(first, second):
  if first != second: return True
  return False

def run_script(command):
  return subprocess.check_output(command).decode('ascii')

def test_sum_column_by_number_with_header_py3():
  expected_res = "Lines read     : 5\nTotal Sum      : 5\n"
  return assert_equals(run_script(['python3', '../tool/sum_column.py', '-f', '../test_data/test_1.csv', '-c', '1', '--has_header']), expected_res)

def test_sum_column_by_number_with_header_py2():
  expected_res = "Lines read     : 5\nTotal Sum      : 5\n"
  return assert_equals(run_script(['python2', '../tool/sum_column.py', '-f', '../test_data/test_1.csv', '-c', '1', '--has_header']), expected_res)

def test_sum_column_by_number_no_header_py3():
  expected_res = "Lines read     : 5\nTotal Sum      : 5\n"
  return assert_equals(run_script(['python3', '../tool/sum_column.py', '-f', '../test_data/test_4.csv', '-c', '1']), expected_res)

def test_sum_column_by_number_no_header_py2():
  expected_res = "Lines read     : 5\nTotal Sum      : 5\n"
  return assert_equals(run_script(['python2', '../tool/sum_column.py', '-f', '../test_data/test_4.csv', '-c', '1']), expected_res)

def test(test_func):
  global num_tests, total_pass
  num_tests += 1.0
  print("TEST  : %s" % (test_func.__name__))
  print("RESULT: ", end='')
  if test_func():
    total_pass += 1.0
    print("PASS")
  else:
    print("FAIL")
  print()

if __name__ == '__main__':
  test(test_sum_column_by_number_with_header_py3)
  test(test_sum_column_by_number_with_header_py2)
  test(test_sum_column_by_number_no_header_py3)
  test(test_sum_column_by_number_no_header_py2)

  print("RESULTS: %f / %f = %f%% TESTS PASSED" % (total_pass, num_tests, (total_pass / num_tests) * 100.0))

#!/bin/bash
test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run linear_search python search.py -i toydata/lorem_ipsum_data.txt -t dolor -a linear
assert_in_stdout 2
assert_exit_code 0

run binary_search python search.py -i toydata/lorem_ipsum_data.txt -t dolor -a binary
assert_in_stdout 2
assert_exit_code 0

run check_styling pycodestyle *.py tests/unit/*.py
assert_exit_code 0
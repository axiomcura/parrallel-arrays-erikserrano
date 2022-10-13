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

run plot_gtex plot_gtex.py \
--gene_reads GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz \
--sample_attributes GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt \
--gene ACTA2 \
--output_file ACTA2.png \
--fig_width 12 \
--fig_height 5 \
--threshold 200000
assert_in_stdout 2
assert_exit_code 0
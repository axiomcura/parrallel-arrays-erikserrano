#!/bin/bash
test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

wget https://github.com/swe4s/lectures/raw/master/data_integration/gtex/GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz -O GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz
wget https://storage.googleapis.com/gtex_analysis_v8/annotations/GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt -O GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt

run linear_search python ../../search.py -i ../../toydata/lorem_ipsum_data.txt -t dolor -a linear
assert_in_stdout 2
assert_exit_code 0

run binary_search python ../../search.py -i ../../toydata/lorem_ipsum_data.txt -t dolor -a linear
assert_in_stdout 2
assert_exit_code 0

# running plot_gtex
run plot_gtex ../../plot_gtex.py \
--gene_reads GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz \
--sample_attributes GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt \
--gene ACTA2 \
--output_file ACTA2.png \
--fig_width 12 \
--fig_height 5 \
--threshold 200000
assert_in_stdout 2
assert_exit_code 0
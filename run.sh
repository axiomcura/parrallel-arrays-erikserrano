#!/bin/bash
set -e


# execute Program
plot_gtex.py \
--gene_reads GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz \
--sample_attributes GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt \
--gene ACTA2 \
--output_file ACTA2.png

# running functional, unit and styling tests
./test_search.sh
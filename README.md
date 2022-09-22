
# plot_gtex

- [plot_gtex](#plot_gtex)
  - [v0.1 Update](#v01-update)
  - [Installation](#installation)
    - [Installing Anaconda](#installing-anaconda)
    - [plot_gtex install](#plot_gtex-install)
  - [Documentation](#documentation)
  - [Usage](#usage)
    - [Download data](#download-data)
    - [Use Case](#use-case)

`plot_gtex` is a simple Conmmand Line Interface (CLI) tool that generates a box plot that that captures all reads counts across all tissue types of a single gene.

## v0.1 Update

Wea are happy to announce our first release of `plot_gtex`! Features added in this program are:

- Fully supported CLI
- Plots all read counts across all tissues when specifying a gene of interest
  - Users can control the size of the plot with the CLI parameters
- can read compressed read files

## Installation

### Installing Anaconda

Installation of of `plot_gtex` requires user to have the conda package manager install.

If your machine does not have `anaconda` installed, please follow the official documentation on how to install it:

- [MacOS](https://docs.anaconda.com/anaconda/install/mac-os/)
- [Linux](https://docs.anaconda.com/anaconda/install/linux/)
- [Windows](https://docs.anaconda.com/anaconda/install/windows/)

After installing continue to the next section on how to install `plot_gtex`.

### plot_gtex install

Installing  `plot_gtex` is very simple! This section assume that you that you have anaconda installed as your package manager.

If not please refer to [Installing Anaconda](#installing-anaconda) section

First clone this respository in to your working directory:

```text
git clone https://github.com/cu-swe4s-fall-2022/assignment-3-parallel-arrays-axiomcura.git
```

and change to directory into the downloaded directory containing the source code.

```text
cd assignment-3-parallel-arrays-axiomcura/
```

After downloading the repository, create an environment that contains all the required dependencies

```text
conda create -n plot_viz python=3.10 -y
```

Next to to activate you environment by typing:

```text
conda activate plot_viz
```

Now that you have you environment installed and activated you can installing the package by typing:

```text
pip install -e .
```

This will install the required packages for `plot_gtex` in your environment.

and you are done!

## Documentation

You can display the help documentation by typing:

```Text
plot_gtex.py -h
```

The output looks like:

``` Text
usage: plot_gtex.py [-h] -gr GENE_READS -s SAMPLE_ATTRIBUTES -g GENE -o OUTPUT [-wt FIG_WIDTH] [-ht FIG_HEIGHT]

Generates box plot of gene counts

options:
  -h, --help            show this help message and exit
  -gr GENE_READS, --gene_reads GENE_READS
                        compressed file that contains gene reads
  -s SAMPLE_ATTRIBUTES, --sample_attributes SAMPLE_ATTRIBUTES
                        file that contains meta data information of samples
  -g GENE, --gene GENE  gene of interest
  -o OUTPUT, --output_file OUTPUT
                        Name of generated output plot
  -wt FIG_WIDTH, --fig_width FIG_WIDTH
                        Figure width size
  -ht FIG_HEIGHT, --fig_height FIG_HEIGHT
                        Figure height size
```

- `gr`: refer to the compressed gene read files that contains all recorded gene reads of all samples within all tissues
- `s`: refers to a file that contains all the sample metadata. This includes the sample name, where it was collected, etc.
- `-g` is your gene of interest. `plot_gtex` will collect all read counts of a given gene across all tissues.
- `wt` width size of the generated plot (default=10)
- `ht` high size of generated plot (default=4)

## Usage

### Download data

To follow along with the usage example please download these datasets in the same directory where the code is:

```text
wget https://github.com/swe4s/lectures/raw/master/data_integration/gtex/GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz
```

```text
wget https://storage.googleapis.com/gtex_analysis_v8/annotations/GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt
```

After downloading the dataset, you can follow along on how to use `plot_gtxt`

### Use Case

In this example, we are going to search for the `ACTA2` across all tissue samples

```text
plot_gtex.py \
--gene_reads GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz \
--sample_attributes GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt \
--gene ACTA2 \
--output_file ACTA2.png
```

Here we are opening to files. The `--gene_reads` file contains all gene read counts recorded per sample.

The `--sample_attributes` takes a regular text file that contains metadata information about samples like: tissue collected from, method of extraction, etc.

The `--gene` is your gene of interests you are searching for within the provided files.

`--output_file` is the name of the generated plot

One can change the dimensions of the generated plot by using the `--fig_width` and `--fig_height` parameters.

Below is the is the sample example with changed figure dimentions:

```
plot_gtex.py \
--gene_reads GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz \
--sample_attributes GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt \
--gene ACTA2 \
--output_file ACTA2.png \
--fig_width 12 \
--fig_height 5 
```

By default, the figure width and height are set to 10, 4 respectively.

If sucessfull, the program finishes with these print statement:

```text
MESSAGE: plot saved in: ACTA2.png
Analysis complete!
```

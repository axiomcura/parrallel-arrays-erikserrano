
# plot_gtex

- [plot_gtex](#plot_gtex)
  - [Installation](#installation)
    - [Installing Anaconda](#installing-anaconda)
    - [plot_gtex install](#plot_gtex-install)
  - [Documentation](#documentation)
  - [Usage](#usage)
    - [Download data](#download-data)
    - [Execute plot_gtex](#execute-plot_gtex)

`plot_gtex` is a simple CLI tools that generates a box plot that that captures all reads counts across all tissue types of a single gene.

## Installation

### Installing Anaconda

Installation of of `plot_gtex` requires user to have the conda package manager install.

If you machine does not have `anaconda` installed, please follow the official documentation on how to install it:

- [MacOS](https://docs.anaconda.com/anaconda/install/mac-os/)
- [Linux](https://docs.anaconda.com/anaconda/install/linux/)
- [Windows](https://docs.anaconda.com/anaconda/install/windows/)

After installing continue to the next section on how to install `plot_gtex`.

### plot_gtex install

Installing  `plot_gtex` is very simple! This section assums that you that you have anaconda installed as your package manager.

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
conda env create -f plot_gtex.yaml python=3.10
```

and you are done!

## Documentation

## Usage

### Download data

To follow along with the usage example please download these datasets in the same directory where the code is:

```text
wget https://github.com/swe4s/lectures/raw/master/data_integration/gtex/GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz
```

```text
wget https://storage.googleapis.com/gtex_analysis_v8/annotations/GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt
```

### Execute plot_gtex

How
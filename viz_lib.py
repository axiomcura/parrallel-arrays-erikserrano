"""
viz_lib module
Developer: Erik Serrano

Module contains functions used for plotting data collected form the gene read
counts and gene attributes datasets

* make_box_plot - generates box plot of all gene counts across all tissue types
"""
from typing import Optional
from pathlib import Path
import matplotlib.pyplot as plt


def make_box_plot(
    data: list[list[str, int]],
    gene_name: str,
    output_file: str,
    fig_width: Optional[int] = 10,
    fig_height: Optional[int] = 4,
) -> None:
    """Generates box plots from grouped gene counts. Where the x axis
    represents tissue sample and y axis is the gene read counts.

    Generated image will be saved in .png format in current working directory

    Parameters
    ----------
    data : list[list[str, int]]
        list of nested list, where the first element is the tissue type and the
        second element is an array of all gene counts collected from tissue
        type samples
    gene_name : str
        name of the gene searched. Will be used to plot
    output_file : str
        name of generated box plot file
    fig_width: int,
        width size of the figure
    fig_height : int
        height size of the figure

    Return
    ------
    None
        Generates a box plot file image in current working directory
    """
    # setting output path
    out_path_obj = Path(output_file)
    parent_path = out_path_obj.parent
    out_name = out_path_obj.name

    save_path = parent_path / f"{out_name}"

    # setting up plot figure
    _, ax = plt.subplots(figsize=(fig_width, fig_height), dpi=300)

    # data prep for plotting
    sample_types = [group_samples[0] for group_samples in data]
    read_counts = [sample_types[1] for sample_types in data]

    # plot data
    plt.boxplot(read_counts)

    # axis formatting
    ax.set_xticklabels(sample_types)
    ax.ticklabel_format(style="plain", axis="y")

    # figure labeling
    plt.title(f"{gene_name} read counts across all tissue samples")
    plt.xlabel("SMTS")
    plt.ylabel("Gene Read Counts")
    plt.xticks(rotation=90)

    # squeezes plot into figure dimensions
    plt.tight_layout()

    # save figure
    plt.savefig(save_path)

    return None

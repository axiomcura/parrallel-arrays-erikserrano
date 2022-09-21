import matplotlib.pyplot as plt


def make_box_plot(
    data: list[list[str, int]], gene_name: str, output_file: str
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

    Return
    ------
    None
        Generates a box plot file image in current working directory
    """

    _, ax = plt.subplots(figsize=(10, 4), dpi=300)

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

    out_file = f"{output_file}.png"
    plt.savefig(out_file)

    return None

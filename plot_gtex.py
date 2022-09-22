"""
plot_gtex.py CLI Tool
Developer: Erik Serrano

plot_gtex is a CLI tool that takes in read counts and gene attributes dataset
to generate boxplot.

The generated boxplot contains the counts of your gene of interests across all
tissue samples.
"""
import sys
import gzip
import argparse
from utils import linear_search
from utils import binary_search
from utils import index_list
from viz_lib import make_box_plot


def load_samples(sample_file: str) -> list[list[str]]:
    """Reads sample file and generates a list of lists. Where each nested lists
    represents a row entry within the the sample file.

    Parameters
    ----------
    sample_file : str
        path to sample file

    Returns
    -------
    list[list[str]]
        return a list that contains two groups. The first group is the haeder
        list and the second group is a list of list that contains all the row
        entries of the sample file.

    Raises
    ------
    FileNotFoundError
        Raised if the provided sample_file path does not exist
    PermissionError
        Raised if you do not have permission to read the sample file
    """
    header = None
    samples = []

    try:
        with open(sample_file, "r") as datafile:
            for idx, row_entry in enumerate(datafile):

                # first row is the header
                if idx == 0:
                    header_info = row_entry.rstrip().split("\t")
                    header = header_info

                # store row data entries
                else:
                    row_entries = row_entry.rstrip().split("\t")
                    samples.append(row_entries)
    except FileNotFoundError as e:
        e_type = e.__class__.__name__
        e_msg = f"File path provided does not exists"
        print(f"{e_type}: {e_msg}")
        sys.exit(1)
    except PermissionError as e:
        e_type = e.__class__.__name__
        e_msg = f"You do not have permission to open this file"
        print(f"{e_type}: {e_msg}")
        sys.exit(1)

    return [header, samples]


def load_reads(reads_file: str) -> list[list[str]]:
    """Loads in gene reads

    Parameters
    ----------
    reads_file : str
        path to reads file

    Returns
    -------
    list[list[str]]
        Returns a list of two nested lists. The first list contains a list of
        column names and the second list is a list of lists containing gene
        read data.

    Raises
    ------
    ValueError
        Raised if a non-compressed file is provided
    FileNotFoundError
        Raised if the the path provided does not point to file
    PermissionError
        Raised if you do not have read permissions
    Exception
        Unexpected error captured

    """
    header_array = None
    entries = []
    try:
        with gzip.open(reads_file, "rt") as reads:
            for idx, row in enumerate(reads):

                # skipping first two lines
                if idx <= 1:
                    continue
                # getting header row
                elif idx == 2:
                    header = row.rstrip().split("\t")
                    header_array = header
                else:
                    entry_list = row.rstrip().split("\t")
                    entries.append(entry_list)

    except ValueError as e:
        e_type = e.__class__.__name__
        e_msg = "File provided is not a compressed file"
        print(f"{e_type}: {e_msg}")
    except FileNotFoundError as e:
        e_type = e.__class__.__name__
        e_msg = f"Unable to find: {reads_file}"
        print(f"{e_type}: {e_msg}")
    except PermissionError as e:
        e_type = e.__class__.__name__
        e_msg = f"Unable to open: {reads_file}"
        print(f"{e_type}: {e_msg}")
    except Exception as e:
        e_type = e.__class__.__name__
        e_msg = f"Unexpected error encountered"
        print(f"{e_type}: {e_msg}")

    return [header_array, entries]


def group_samples_by_tissues(
    samples: list[list[str]], sample_id_col_idx: int, group_col_idx: int
) -> list[list[str]]:
    """Groups sample ids to their appropriate sample group.

    Parameters
    ----------
    samples : list[list[str]]
        A list of lists, where each list within the list is a row entry in the
        sample file

    sample_id_col_idx : int
        Index value that points to the id column in the sample data entries

    group_col_idx : int
        Index value that points to the group column in the sample data entries

    Returns
    -------
    list(list[str])
        A list contain two lists. Where the first list is the list of groups
        and the second list is the samples associated with a group.

    """

    # initializing group and member lists
    sample_groups = []
    group_members = []

    # iterate all samples and group them based on tissue group
    for row_idx, sample_entry in enumerate(samples):

        # selecting data from sample entry
        sample_name = sample_entry[sample_id_col_idx]
        current_group = sample_entry[group_col_idx]

        # searching if the current group is in the groups array
        try:
            current_group_idx = linear_search(current_group, sample_groups)

        # if the value is not found, start tracking
        except ValueError:
            current_group_idx = len(sample_groups)
            sample_groups.append(current_group)
            group_members.append([])

        # if the group exists within the sample_groups array, use the idx
        # position of the current group and append it to the members list
        group_members[current_group_idx].append(sample_name)

    return list(zip(sample_groups, group_members))


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generates box plot of gene counts"
    )
    parser.add_argument(
        "-gr",
        "--gene_reads",
        type=str,
        dest="gene_reads",
        required=True,
        help="compressed file that contains gene reads",
    )
    parser.add_argument(
        "-s",
        "--sample_attributes",
        type=str,
        dest="sample_attributes",
        required=True,
        help="file that contains meta data information of samples",
    )
    parser.add_argument(
        "-g",
        "--gene",
        type=str,
        dest="gene",
        required=True,
        help="gene of interest",
    )
    parser.add_argument(
        "-o",
        "--output_file",
        type=str,
        dest="output",
        required=True,
        help="Name of generated output plot",
    )
    parser.add_argument(
        "-wt",
        "--fig_width",
        type=str,
        dest="fig_width",
        default=10,
        required=False,
        help="Figure width size",
    )
    parser.add_argument(
        "-ht",
        "--fig_height",
        type=str,
        dest="fig_height",
        default=4,
        required=False,
        help="Figure height size",
    )
    args = parser.parse_args()

    # loading sample data
    sample_header, samples = load_samples(args.sample_attributes)
    reads_header, reads = load_reads(args.gene_reads)

    # find the group and sample_id column indx within the header info
    try:
        sample_group_col_idx = linear_search(
            target="SMTS", sel_array=sample_header
        )
    except ValueError as e:
        e_type = e.__class__.__name__
        e_msg = f"Unable to find tissue group column in gene attributes file"
        print(f"{e_type}: {e_msg}")
        sys.exit(1)

    try:
        sample_id_col_idx = linear_search(
            target="SAMPID", sel_array=sample_header
        )
    except ValueError as e:
        e_type = e.__class__.__name__
        e_msg = f"Unable to sample id column in gene attributes file"
        print(f"{e_type}: {e_msg}")
        sys.exit(1)

    # now group sample entries to their tissue types
    group_members = group_samples_by_tissues(
        samples,
        sample_id_col_idx=sample_id_col_idx,
        group_col_idx=sample_group_col_idx,
    )

    # indexing reads_header for binary searches
    reads_header = index_list(reads_header)

    # get gene column in reads data
    try:
        gene_name_col_idx = binary_search(
            target="Description", indexed_sel_array=reads_header
        )
    except ValueError as e:
        e_type = e.__class__.__name__
        e_msg = "Unable to find gene column in gene reads header"
        print(f"{e_type}: {e_msg}")
        sys.exit(1)

    # iterate all genes reads data and index genes
    genes = []
    for read_entry in reads:
        gene_name_entry = read_entry[gene_name_col_idx]
        genes.append(gene_name_entry)

    # now collecting read counts of one gene of all samples per tissue
    try:
        gene_idx_pos = linear_search(target=args.gene, sel_array=genes)
    except ValueError as e:
        e_type = e.__class__.__name__
        e_msg = f"Unable to {args.gene} gene in gene column"
        print(f"{e_type}: {e_msg}")
        sys.exit(1)

    # getting row entry position based on where the GOI is located
    gene_reads_entry = reads[gene_idx_pos]

    # iterating all tissue samples with associated sample members
    grouped_read_counts = []
    for tissue_samp, sample_members in group_members:

        # collecting all gene read counts within each sample member
        counts = []
        for sample_member in sample_members:

            # conduct a binary search to find samples
            # -- if the value is not found, skip it and go to the next
            try:
                sample_col_idx = binary_search(sample_member, reads_header)
            except ValueError:
                continue

            # get gene read count from gene reads entry by using gene index pos
            count = int(gene_reads_entry[sample_col_idx])
            counts.append(count)

        grouped_read_counts.append([tissue_samp, counts])

    # plot the the collected grouped_read_counts
    make_box_plot(
        data=grouped_read_counts,
        gene_name=args.gene,
        output_file=args.output,
        fig_width=args.fig_width,
        fig_height=args.fig_height,
    )

    print("Analysis complete!")
    sys.exit(0)


if __name__ == "__main__":
    main()

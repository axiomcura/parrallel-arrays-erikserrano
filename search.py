"""
search.py

Simple script that searches for a target value within an input file. Currently
supported search algorithms are: linear and binary searches:

Users have the option to shuffle the loaded data as well with the `-s` flag
"""
import sys
import utils
import random
import argparse


def main() -> int:

    # CLI argument handler
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-i", "--input", dest="input", type=str, help="path to data"
    )
    parser.add_argument(
        "-t",
        "--target",
        dest="target",
        required=True,
        type=str,
        help="value to find in given toy data",
    )
    parser.add_argument(
        "-a",
        "--algorithm",
        dest="algorithm",
        type=str,
        choices=["linear", "binary"],
        default="linear",
        help="Selecting search algorithm. choices=[linear, binary]",
    )
    parser.add_argument(
        "-s",
        "--shuffle",
        dest="shuffle",
        default=False,
        action="store_true",
        help="shuffles toy data",
    )
    args = parser.parse_args()

    # open input file
    with open(args.input, "r") as f:
        # clean contents
        lorem_ipsum_data = (
            f.read().rstrip("\n").replace(".", "").replace(",", "")
        )

        # create list
        toy_conts = lorem_ipsum_data.split()

        # shuffle list if `-s` is used
        if args.shuffle is True:
            random.shuffle(toy_conts)

    # selecting algorithm
    # -- linear search
    if args.algorithm == "linear":
        try:
            index = utils.linear_search(args.target, toy_conts)
            print(index)
            sys.exit(0)
        except ValueError as e:
            e_type = e.__class__.__name__
            e_msg = f"Unable to find target value `{args.target}`"
            print(f"{e_type}: {e_msg}")
            sys.exit(1)
        except TypeError as e:
            e_type = e.__class__.__name__
            e_msg = "Provided data is not a list or tuple"
            print(f"{e_type}: {e_msg}")
            sys.exit(1)
        except RuntimeError as e:
            e_type = e.__class__.__name__
            e_msg = "Empty list provided for linear search"
            print(f"{e_type}: {e_msg}")
            sys.exit(1)
        except Exception as e:
            e_type = e.__class__.__name__
            e_msg = "Unknown error captured"
            print(f"{e_msg} -> {e_type}")
            sys.exit(1)

    # -- binary search
    if args.algorithm == "binary":

        # creating index array
        try:
            indexed_array = utils.index_list(toy_conts)
        except TypeError as e:
            e_type = e.__class__.__name__
            e_msg = "Provided data is not a list or tuple"
            print(f"{e_type}: {e_msg}")
            sys.exit(1)
        except ValueError as e:
            e_type = e.__class__.__name__
            e_msg = "Input data does not have any "
            print(f"{e_type}: {e_msg}")
            sys.exit(1)

        # conducting binary search with indexed array
        try:
            index = utils.binary_search(args.target, indexed_array)
            print(index)
            sys.exit(0)
        except ValueError as e:
            e_type = e.__class__.__name__
            e_msg = f"Unable to find target value {args.target}"
            print(f"{e_type}: {e_msg}")
            sys.exit(1)
        except Exception as e:
            e_type = e.__class__.__name__
            e_msg = "Unknown error captured"
            print(f"{e_msg} -> {e_type}")
            sys.exit(1)


if __name__ == "__main__":
    main()

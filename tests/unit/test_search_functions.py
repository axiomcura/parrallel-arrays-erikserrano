"""
test_search_functions.py

testing module that tests both linear and binary search algorithm.

"""
import os
import pickle
import random
import unittest

import utils


class SearchAlgorithms(unittest.TestCase):
    def test_linear_search_1(self) -> None:
        """Positive test case, where it searches target that exists within
        array"""

        # ints test
        with open("int_data.pickle", "rb") as f:
            test_data1 = pickle.load(f)

        index1 = utils.linear_search(2, test_data1)
        self.assertEqual(index1, 2)

        # strings tst
        with open("string_data.pickle", "rb") as f:
            test_data2 = pickle.load(f)

        index2 = utils.linear_search("consectetur", test_data2)
        self.assertEqual(index2, 5)

        # mix type test
        with open("mixed_char_data.pickle", "rb") as f:
            test_data3 = pickle.load(f)

        index3 = utils.linear_search("CRTW", test_data3)
        self.assertEqual(index3, 6)

    def test_linear_search_2(self) -> None:
        """Negative test case where a target is not found within the provided
        array"""
        with open("string_data.pickle", "rb") as f:
            test_data = pickle.load(f)

        self.assertRaises(ValueError, utils.linear_search, 3, test_data)

    def test_linear_search_3(self) -> None:
        """Tests multiple of integer arrays"""
        with open("multi_line_ints.pickle", "rb") as f:
            loaded_data = pickle.load(f)

            for int_list in loaded_data:
                index = utils.linear_search(4, int_list)
                self.assertEqual(type(index), int)
                self.assertTrue(index <= 9)

    def test_linear_search_4(self) -> None:
        """Testing with empty list"""
        empty_list = []
        target = "consectetur"

        self.assertRaises(
            RuntimeError, utils.linear_search, target, empty_list
        )
        pass

    def test_linear_search_5(self) -> None:
        """Testing linear search with non sequence object"""
        dict_obj = {"should": 1, "world": 2, "work": 3}
        set_obj = {"hello", "world"}
        target = "world"

        self.assertRaises(TypeError, utils.linear_search, target, dict_obj)
        self.assertRaises(TypeError, utils.linear_search, target, set_obj)

    def test_list_indexing(self) -> None:
        """Positive case"""
        with open("string_data.pickle", "rb") as f:
            load_data = pickle.load(f)

        indexed_array = utils.index_list(load_data)

        positive_case = [
            ["Lorem", 0],
            ["ipsum", 1],
            ["dolor", 2],
            ["sit", 3],
            ["amet", 4],
            ["consectetur", 5],
            ["adipiscing", 6],
            ["elit", 7],
        ]

        self.assertEqual(indexed_array, positive_case)

    def test_list_indexing2(self) -> None:
        """Negative test of list indexing"""
        with open("string_data.pickle", "rb") as f:
            load_data = pickle.load(f)

        indexed_array = utils.index_list(load_data)

        positive_case = [
            ("Lorem", 0),
            ("ipsum", 1),
            ("sit", 2),
            ("dolor", 3),
            ("amet", 4),
            ("consectetur", 5),
            ("elit", 6),
            ("adipiscing", 7),
        ]

        self.assertNotEqual(indexed_array, positive_case)

    def test_list_indexing3(self) -> None:
        """type checking with array indexing function. Raise type errors for
        non-sequence types (not list or tuples)
        """
        with open("string_data.pickle", "rb") as f:
            load_data = pickle.load(f)

            set_loaded_data = set(load_data)
            dict_loaded_data = {name: i for i, name in enumerate(load_data)}

            self.assertRaises(TypeError, utils.index_list, set_loaded_data)
            self.assertRaises(TypeError, utils.index_list, dict_loaded_data)

    def test_list_indexing4(self) -> None:
        """Negative test, providing an empty sequence type (list, tuple)"""

        empty_list = []
        empty_tuple = []

        self.assertRaises(ValueError, utils.index_list, empty_list)
        self.assertRaises(ValueError, utils.index_list, empty_tuple)

    def test_binary_search_1(self) -> None:
        """Binary search of randomly shuffled list test case where a target
        is not found within the provided array"""

        with open("string_data.pickle", "rb") as f:
            loaded_data = pickle.load(f)

            # 40 iterations of randomly shuffled data
            for _ in range(40):
                random.shuffle(loaded_data)
                indexed_array = utils.index_list(loaded_data)
                index = utils.binary_search("dolor", indexed_array)
                self.assertEqual(type(index), int)

    def test_binary_search_2(self) -> None:
        """applying multiple binary searches that lead to a negative case,
        capturing  exception
        """

        with open("string_data.pickle", "rb") as f:
            loaded_data = pickle.load(f)
            for _ in range(40):
                indexed_array = utils.index_list(loaded_data)
                self.assertRaises(
                    ValueError, utils.binary_search, "notfound", indexed_array
                )

    @classmethod
    def setUp(cls) -> None:
        """Setting up files for tests"""
        cls.mixed_chars_array = "mixed_char_data.pickle"
        cls.int_array = "int_data.pickle"
        cls.string_array = "string_data.pickle"
        cls.multi_line_ints = "multi_line_ints.pickle"

        # generating random words as "labels"
        random_words = (
            "Lorem ipsum dolor sit amet consectetur adipiscing elit".split()
        )

        # generating array of numbers
        number_list = [i for i in range(10)]

        # random array of numbers strings
        combined_array = random_words + number_list
        mix_list = random.choices(combined_array, k=6) + ["CRTW"]

        # writing out files
        with open(cls.mixed_chars_array, "wb") as f:
            pickle.dump(mix_list, f)

        with open(cls.int_array, "wb") as f:
            pickle.dump(number_list, f)

        with open(cls.string_array, "wb") as f:
            pickle.dump(random_words, f)

        with open(cls.multi_line_ints, "wb") as f:
            list_of_int_arrays = []

            # set of number lists
            num_list = [i for i in range(10)]

            for i in range(50):
                random.shuffle(num_list)
                list_of_int_arrays.append(num_list)

            pickle.dump(list_of_int_arrays, f)

    @classmethod
    def tearDown(cls) -> None:
        os.remove(cls.int_array)
        os.remove(cls.string_array)
        os.remove(cls.multi_line_ints)
        os.remove(cls.mixed_chars_array)


class MeanCalculationTest(unittest.TestCase):

    # ------------------------------
    # Mean Calculation Tests
    # ------------------------------
    def test_mean_empty_list(self) -> None:
        """Testing read_count_mean() with empty list"""
        read_counts = []
        mean = utils.read_count_mean(read_counts)
        self.assertEqual(0, mean)

    def test_mean_different_sequences(self) -> None:
        """Tests functionality of read_count_mean() with different Sequence
        types other than Lists
        """
        read_counts1 = []
        read_counts2 = ()
        read_counts3 = {}

        mean1 = utils.read_count_mean(read_counts1)
        self.assertEqual(0, mean1)
        self.assertRaises(TypeError, utils.read_count_mean, read_counts2)
        self.assertRaises(TypeError, utils.read_count_mean, read_counts3)

    def test_mean_only_int_vals(self) -> None:
        """Tests read_count_mean() on integer arrays"""
        with open("group_ints.pickle", "rb") as f:
            group_datasets = pickle.load(f)

        for group_data in group_datasets:
            group_name, read_counts = group_data[0], group_data[1]

            true_mean = round(sum(read_counts) / len(read_counts), 2)
            test_mean = utils.read_count_mean(read_counts)

            self.assertEqual(true_mean, test_mean)

    def test_mean_only_float_vals(self) -> None:
        with open("group_floats.pickle", "rb") as f:
            group_datasets = pickle.load(f)

        for group_data in group_datasets:
            group_name, read_counts = group_data[0], group_data[1]

            true_mean = round(sum(read_counts) / len(read_counts), 2)
            test_mean = utils.read_count_mean(read_counts)

            self.assertEqual(true_mean, test_mean)

    def test_mean_float_and_ints(self) -> None:
        with open("grouped_int_floats.pickle", "rb") as f:
            group_datasets = pickle.load(f)

        for group_data in group_datasets:
            group_name, read_counts = group_data[0], group_data[1]
            true_mean = round(sum(read_counts) / len(read_counts), 2)
            test_mean = utils.read_count_mean(read_counts)

            self.assertEqual(true_mean, test_mean)

    def test_mean_str(self) -> None:
        """Tests read_count_mean() when given strings to conduct the mean"""
        group_data = [["Blood"], ["a", "b", "c"]]
        self.assertRaises(TypeError, utils.read_count_mean, group_data)

    def test_mean_float_ints_str(self) -> None:
        """test read_count_mean() with group data that contains ints, floats,
        str"""
        with open("group_ints_floats_str.pickle", "rb") as f:
            group_datasets = pickle.load(f)

        for group_data in group_datasets:
            group_name, read_counts = group_data[0], group_data[1]
            self.assertRaises(TypeError, utils.read_count_mean, read_counts)

    def test_known_ints_mean(self) -> None:
        """Calculates mean of known array"""

        with open("seeded_array_counts_ints.pickle", "rb") as f:
            test_readcount_data = pickle.load(f)

        true_mean = 1910.51
        test_mean = utils.read_count_mean(test_readcount_data)

        self.assertEqual(true_mean, test_mean)

    # ------------------------------
    # Thresholding Tests
    # ------------------------------

    def test_filter_non_lists(self) -> None:
        """testing on non list objects"""
        grouped_data_1 = (("Blood"), (1, 2, 3, 4))
        grouped_data_2 = (("Blood"), (1.0, 2.0, 3.0, 4.0))
        grouped_data_3 = (("Blood"), (1, 2.0, 3, 4.0))
        grouped_data_4 = [("Blood"), (1, 2.0, 3, 4.0)]
        grouped_data_5 = (["Blood"], [1, 2, 3, 4])
        grouped_data_6 = (["Blood"], [1.0, 2, 3, 4.0])

        self.assertRaises(TypeError, utils.filter_by_mean, grouped_data_1)
        self.assertRaises(TypeError, utils.filter_by_mean, grouped_data_2)
        self.assertRaises(TypeError, utils.filter_by_mean, grouped_data_3)
        self.assertRaises(TypeError, utils.filter_by_mean, grouped_data_4)
        self.assertRaises(TypeError, utils.filter_by_mean, grouped_data_5)
        self.assertRaises(TypeError, utils.filter_by_mean, grouped_data_6)

    def test_filter_empty_list(self) -> None:
        """Testing if filtering process gets an empty list"""
        empty_array = []
        self.assertRaises(ValueError, utils.filter_by_mean, empty_array)

    def test_filter_missing_group(self) -> None:
        """Testing filter process if group name is missing"""
        test_data1 = [1, 2, 3, 4, 5]
        test_data2 = [1, 2.0, 3, 4.0, 5]

        self.assertRaises(TypeError, utils.filter_by_mean, test_data1)
        self.assertRaises(TypeError, utils.filter_by_mean, test_data2)

    def test_non_int_threshold(self) -> None:
        """Tests if threshold is a non int value"""
        with open("group_ints.pickle", "rb") as f:
            group_data = pickle.load(f)

        self.assertRaises(
            TypeError, utils.filter_by_mean, group_data, threshold="10"
        )
        self.assertRaises(
            TypeError, utils.filter_by_mean, group_data, threshold="ten"
        )

    # ------------------------------
    # Tests setup methods
    # ------------------------------
    @classmethod
    def setUp(cls) -> None:

        # file names
        cls.group_ints = "group_ints.pickle"
        cls.group_floats = "group_floats.pickle"
        cls.group_ints_floats = "grouped_int_floats.pickle"
        cls.group_ints_floats_str = "group_ints_floats_str.pickle"
        cls.seeded_array_counts_ints = "seeded_array_counts_ints.pickle"

        # setting up names and variables
        random_groups = ["Blood", "Kidney", "Brain"]
        lorem_ipsum_array = (
            "Lorem ipsum dolor sit amet consectetur adipiscing elit".split()
        )

        # generating toy data with different types
        grouped_ints = []
        grouped_floats = []
        grouped_int_floats = []
        grouped_int_floats_str = []
        for group in random_groups:

            # generating random value measurements
            read_counts_ints = [random.randint(0, 4000) for _ in range(200)]
            read_counts_floats = [
                round(random.random() * 1000, 2) for _ in range(200)
            ]
            read_counts_int_floats = random.choices(
                read_counts_ints + read_counts_floats, k=200
            )

            read_counts_floats_int_str = (
                read_counts_ints[:50] + read_counts_floats[:50]
            )
            for rand_word in lorem_ipsum_array:

                # updating element in array with string type
                indx_pos = random.randint(
                    0, len(read_counts_floats_int_str) - 1
                )
                read_counts_floats_int_str[indx_pos] = rand_word

            # creating toy group data
            results_ints = [group, read_counts_ints]
            results_floats = [group, read_counts_floats]
            results_int_floats = [group, read_counts_int_floats]
            results_int_floats_str = [group, read_counts_floats_int_str]

            # storing group toy data
            grouped_ints.append(results_ints)
            grouped_floats.append(results_floats)
            grouped_int_floats.append(results_int_floats)
            grouped_int_floats_str.append(results_int_floats_str)

        # writing out data files
        with open(cls.group_ints, mode="wb") as f:
            pickle.dump(grouped_ints, f)

        with open(cls.group_floats, mode="wb") as f:
            pickle.dump(grouped_floats, f)

        with open(cls.group_ints_floats, mode="wb") as f:
            pickle.dump(grouped_int_floats, f)

        with open(cls.group_ints_floats_str, mode="wb") as f:
            pickle.dump(grouped_int_floats_str, f)

        with open(cls.seeded_array_counts_ints, mode="wb") as f:
            random.seed(42)
            seeded_array = [random.randint(0, 4000) for _ in range(200)]
            pickle.dump(seeded_array, f)

    @classmethod
    def tearDown(cls) -> None:
        os.remove(cls.group_ints)
        os.remove(cls.group_floats)
        os.remove(cls.group_ints_floats)
        os.remove(cls.group_ints_floats_str)


if __name__ == "__main__":
    unittest.main()

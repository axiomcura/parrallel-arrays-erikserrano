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

        self.assertRaises(RuntimeError, utils.linear_search, target, empty_list)
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
        """Binary search of randomly shuffled list test case where a target is not found within
        the provided array"""

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


if __name__ == "__main__":
    unittest.main()

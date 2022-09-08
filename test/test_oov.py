import unittest
import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from oov_ngrams_testcases import OOVNgramsTestCases
from split_oov_ngrams_testcases import SplitOOVNgramsTestCases
from context_oov_ngrams_testcases import ContextOOVNgramsTestCases
from ngrams.oov_ngrams import OOVNgrams


class OOVNgramsTest(unittest.TestCase):
    def test_if_all_token_in_doc_isnot_oov(self):
        oov_ngrams = OOVNgrams()
        test_cases = OOVNgramsTestCases()
        self.assertEqual(
            oov_ngrams.create_ngrams(test_cases.case_1["docs"], 2),
            test_cases.case_1["expected"]
        )

    def test_if_all_token_in_doc_is_oov(self):
        oov_ngrams = OOVNgrams()
        test_cases = OOVNgramsTestCases()
        self.assertEqual(
            oov_ngrams.create_ngrams(test_cases.case_2["docs"], 2),
            test_cases.case_2["expected"]
        )

    # OOV in the beginning of doc
    def test_if_oov_in_beginning_and_context_size_bigger_than_doc_size_and_right_context_isnot_oov(self):
        oov_ngrams = OOVNgrams()
        test_cases = OOVNgramsTestCases()
        self.assertEqual(
            oov_ngrams.create_ngrams(test_cases.case_3["docs"], 5),
            test_cases.case_3["expected"]
        )

    def test_if_oov_in_beginning_and_context_size_smaller_than_doc_size_and_right_context_isnot_oov(self):
        oov_ngrams = OOVNgrams()
        test_cases = OOVNgramsTestCases()
        self.assertEqual(
            oov_ngrams.create_ngrams(test_cases.case_4["docs"], 2),
            test_cases.case_4["expected"]
        )
    
    def test_if_oov_in_beginning_and_right_context_isnot_oov(self):
        oov_ngrams = OOVNgrams()
        test_cases = OOVNgramsTestCases()
        self.assertEqual(
            oov_ngrams.create_ngrams(test_cases.case_5["docs"], 2),
            test_cases.case_5["expected"]
        )

    # OOV in the end of doc
    def test_if_oov_in_end_and_context_size_bigger_than_doc_size_and_right_context_isnot_oov(self):
        oov_ngrams = OOVNgrams()
        test_cases = OOVNgramsTestCases()
        self.assertEqual(
            oov_ngrams.create_ngrams(test_cases.case_6["docs"], 5),
            test_cases.case_6["expected"]
        )

    def test_if_oov_in_end_and_context_size_smaller_than_doc_size_and_right_context_isnot_oov(self):
        oov_ngrams = OOVNgrams()
        test_cases = OOVNgramsTestCases()
        self.assertEqual(
            oov_ngrams.create_ngrams(test_cases.case_7["docs"], 2),
            test_cases.case_7["expected"]
        )

    def test_if_oov_in_end_and_right_context_isnot_oov(self):
        oov_ngrams = OOVNgrams()
        test_cases = OOVNgramsTestCases()
        self.assertEqual(
            oov_ngrams.create_ngrams(test_cases.case_8["docs"], 3),
            test_cases.case_8["expected"]
        )

    # OOV in the middle of doc
    def test_if_oov_in_the_middle_left_and_right_context_doesnt_exist(self):
        oov_ngrams = OOVNgrams()
        test_cases = OOVNgramsTestCases()
        self.assertEqual(
            oov_ngrams.create_ngrams(test_cases.case_9["docs"], 2),
            test_cases.case_9["expected"]
        )

    def test_if_oov_in_anywhere(self):
        oov_ngrams = OOVNgrams()
        test_cases = OOVNgramsTestCases()
        self.assertEqual(
            oov_ngrams.create_ngrams(test_cases.case_10["docs"], 5),
            test_cases.case_10["expected"]
        )

    def test_if_ovv_in_the_middle_more_than_one(self):
        oov_ngrams = OOVNgrams()
        test_cases = OOVNgramsTestCases()
        self.assertEqual(
            oov_ngrams.create_ngrams(test_cases.case_11["docs"], 2),
            test_cases.case_11["expected"]
        )
    

class SplitOOVNGgramsTest(unittest.TestCase):
    def test_when_left_context_oov_chars_and_right_context_exist_1_ngrams(self):
        test_cases = SplitOOVNgramsTestCases()
        oov_ngrams = OOVNgrams()
        self.assertEqual(
            oov_ngrams.split_ngrams(test_cases.case_1["ngrams"]),
            test_cases.case_1["expected"]
        )

    def test_when_left_context_oov_chars_and_right_context_exist_more_than_1_ngrams(self):
        test_cases = SplitOOVNgramsTestCases()
        oov_ngrams = OOVNgrams()
        self.assertEqual(
            oov_ngrams.split_ngrams(test_cases.case_2["ngrams"]),
            test_cases.case_2["expected"]
        )

    def test_when_left_context_doesnot_exist(self):
        test_cases = SplitOOVNgramsTestCases()
        oov_ngrams = OOVNgrams()
        self.assertEqual(
            oov_ngrams.split_ngrams(test_cases.case_3["ngrams"]),
            test_cases.case_3["expected"]
        )

    def test_when_right_context_doesnot_exist(self):
        test_cases = SplitOOVNgramsTestCases()
        oov_ngrams = OOVNgrams()
        self.assertEqual(
            oov_ngrams.split_ngrams(test_cases.case_4["ngrams"]),
            test_cases.case_4["expected"]
        )

    def test_when_left_and_right_context_doesnot_exist(self):
        test_cases = SplitOOVNgramsTestCases()
        oov_ngrams = OOVNgrams()
        self.assertEqual(
            oov_ngrams.split_ngrams(test_cases.case_5["ngrams"]),
            test_cases.case_5["expected"]
        )

class ContextNGgramsTest(unittest.TestCase):
    def test_if_get_left_context(self):
        test_cases = ContextOOVNgramsTestCases()
        oov_ngrams = OOVNgrams()
        ngrams = oov_ngrams.create_ngrams(test_cases.case_1["docs"], context_size=3)
        self.assertEqual(
            oov_ngrams.left_context(ngrams),
            test_cases.case_1["expected"]
        )

    def test_if_get_right_context(self):
        test_cases = ContextOOVNgramsTestCases()
        oov_ngrams = OOVNgrams()
        ngrams = oov_ngrams.create_ngrams(test_cases.case_2["docs"], context_size=3)
        self.assertEqual(
            oov_ngrams.right_context(ngrams),
            test_cases.case_2["expected"]
        )

    def test_if_get_oov_context(self):
        test_cases = ContextOOVNgramsTestCases()
        oov_ngrams = OOVNgrams()
        ngrams = oov_ngrams.create_ngrams(test_cases.case_3["docs"], context_size=3)
        self.assertEqual(
            oov_ngrams.oov_context(ngrams),
            test_cases.case_3["expected"]
        )


if __name__ == '__main__':
    unittest.main()
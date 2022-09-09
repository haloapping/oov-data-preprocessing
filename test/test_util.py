import unittest
import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from ngrams.util import Util
from util_testcases import (
    PaddingTestCases,
    TokenToIdxTestCases,
    IdxToTokenTestCases,
    VocabsTestCases
)

class UtilTest(unittest.TestCase):
    def test_if_mode_is_post(self):
        util = Util()
        test_cases = PaddingTestCases()
        self.assertEqual(
            util.padding(docs=test_cases.case_1["docs"], mode="post", padding_val="</PAD>"),
            test_cases.case_1["expected"]
        )

    def test_if_mode_is_pre(self):
        util = Util()
        test_cases = PaddingTestCases()
        self.assertEqual(
            util.padding(docs=test_cases.case_2["docs"], mode="pre", padding_val="</PAD>"),
            test_cases.case_2["expected"]
        )

    def test_if_mode_isnot_available(self):
        util = Util()
        test_cases = PaddingTestCases()
        self.assertRaises(
            ValueError,
            util.padding,
            docs=test_cases.case_2["docs"],
            mode=test_cases.case_3["unknown_mode"],
            padding_val="</PAD>"
        )

    @unittest.skip("Not")
    def test_vocabs(self):
        util = Util()
        test_cases = VocabsTestCases()
        self.assertEqual(
            util.vocabs(test_cases.case_1["tokens"]),
            test_cases.case_1["vocabs"]
        )

    def test_token_to_idx(self):
        util = Util()
        test_cases = TokenToIdxTestCases()
        self.assertEqual(
            util.token_to_idx(test_cases.case_1["tokens"]),
            test_cases.case_1["token_to_idx"]
        )

    def test_idx_to_token(self):
        util = Util()
        test_cases = IdxToTokenTestCases()
        self.assertEqual(
            util.idx_to_token(test_cases.case_1["tokens"]),
            test_cases.case_1["idx_to_token"]
        )
class PaddingTestCases:
    def __init__(self):
        # post
        self.case_1 = {
            "docs": [
                ["Aku", "suka", "sama", "kamu", "."],
                ["Hari", "ini", "hujan"],
                ["Hi"],
                []
            ],
            "expected": [
                ["Aku", "suka", "sama", "kamu", "."],
                ["Hari", "ini", "hujan", "</PAD>", "</PAD>"],
                ["Hi", "</PAD>", "</PAD>", "</PAD>", "</PAD>"],
                ["</PAD>", "</PAD>", "</PAD>", "</PAD>", "</PAD>"]
            ]
        }

        # pre
        self.case_2 = {
            "docs": [
                [],
                ["Aku", "suka", "sama", "kamu", "."],
                ["Hari", "ini", "hujan"],
                ["Hi"]
            ],
            "expected": [
                ["</PAD>", "</PAD>", "</PAD>", "</PAD>", "</PAD>"],
                ["Aku", "suka", "sama", "kamu", "."],
                ["</PAD>", "</PAD>", "Hari", "ini", "hujan"],
                ["</PAD>", "</PAD>", "</PAD>", "</PAD>", "Hi"]
            ]
        }

        # unknown mode
        self.case_3 = {
            "pre_mode" : "pre",
            "post_mode": "post",
            "unknown_mode": "unknown_mode",
            "expected": "mode = unknown_mode is not available, use instead 'pre' or 'post'."
        }

class TokenToIdxTestCases:
    def __init__(self):
        self.case_1 = {
            "tokens": [
                "Aku",
                "suka",
                "sama",
                "kamu",
                ",",
                "tetapi",
                "kamu",
                "tidak",
                "suka",
                "sama",
                "aku",
                "."
            ],
            "token_to_idx": {
                "Aku" : 0,
                "suka" : 1,
                "sama" : 2,
                "kamu" : 3,
                "," : 4,
                "tetapi" : 5,
                "kamu" : 6,
                "tidak" : 7,
                "suka" : 8,
                "sama" : 9,
                "aku": 10,
                ".": 11
            }
        }

class IdxToTokenTestCases:
    def __init__(self):
        self.case_1 = {
            "tokens": [
                "Matematika",
                "adalah",
                "ilmu",
                "yang",
                "menyenangkan",
                "."
            ],
            "idx_to_token": {
                0 : "Matematika",
                1 : "adalah",
                2 : "ilmu",
                3 : "yang",
                4 : "menyenangkan",
                5 : "."
            }
        }

class VocabsTestCases:
    def __init__(self):
        self.case_1 = {
            "tokens": [
                "Aku",
                "suka",
                "sama",
                "kamu",
                ",",
                "tetapi",
                "kamu",
                "tidak",
                "suka",
                "sama",
                "aku",
                "."
            ],
            "vocabs": [
                '.',
                'aku',
                'Aku',
                'tidak',
                'suka',
                'kamu',
                'sama',
                ',',
                'tetapi'
            ]
        }
class SplitOOVNgramsTestCases:
    def __init__(self):
        # Ada left context, oov context dan right context, 1 ngrams
        self.case_1 = {
            "ngrams": [
                [("Halo", False), (",", False), ("nama", True), ("saya", False), ("Apping", False), (".", False)]
            ],
            "expected": [(
                ["Halo", ","],
                ["n", "a", "m", "a"],
                ["saya", "Apping", "."]
            )]
        }

        # Ada left context, oov context dan right context, lebih dari 1 ngrams
        self.case_2 = {
            "ngrams": [
                [("Halo", False), (",", False), ("nama", True), ("saya", False), ("Apping", False), (".", False)],
                [("Makan", False), ("bakso", False), ("bersama", True), ("pacar", False), (".", False)]
            ],
            "expected": [
                (["Halo", ","],
                 ["n", "a", "m", "a"],
                 ["saya", "Apping", "."]),
                (["Makan", "bakso"],
                 ["b", "e", "r", "s", "a", "m", "a"],
                 ["pacar", "."])
            ]
        }

        # Tidak ada left context
        self.case_3 = {
            "ngrams": [
                [("Nama", True), ("saya", False), ("Apping", False), (".", False)],
                [("Bersama", True), ("pacar", False), (".", False)]
            ],
            "expected": [
                (
                    [],
                    ["n", "a", "m", "a"],
                    ["saya", "Apping", "."]
                ),
                (
                    [],
                    ["b", "e", "r", "s", "a", "m", "a"],
                    ["pacar", "."]
                )
            ]
        }

        # Tidak ada right context
        self.case_4 = {
            "ngrams": [
                [("Bakso", False), ("Mas", False), ("Gendut", True)],
                [("Makan", False), ("bakso", False), ("bersama", False), ("pacar", False), (".", True)]
            ],
            "expected": [
                (
                    ["Bakso", "Mas"],
                    ["g", "e", "n", "d", "u", "t"],
                    []
                ),
                (
                    ["Makan", "bakso", "bersama", "pacar"],
                    ["."],
                    []
                )
            ]
        }

        # Tidak ada left dan right context
        self.case_5 = {
            "ngrams": [
                [("Mas", True)],
                [("Bakso", True)]
            ],
            "expected": [
                (
                    [],
                    ["m", "a", "s"],
                    []
                ),
                (
                    [],
                    ["b", "a", "k", "s", "o"],
                    []
                )
            ]
        }
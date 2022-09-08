class ContextOOVNgramsTestCases:
    def __init__(self):
        # Left context
        self.case_1 = {
            "docs": [
                [("Aku", False), ("suka", False), ("sama", True), ("kamu", False), (".", False)],
                [("Makan", False), ("gado-gado", False), ("bersama", True), ("pacar", False), (".", False)],
                [("Bakso", False), ("adalah", False), ("makanan", False), ("favorit", True), ("saya", False), (".", False)]
            ],
            "expected": [
                ["Aku", "suka"],
                ["Makan", "gado-gado"],
                ["Bakso", "adalah", "makanan"]
            ]
        }

        # Right context
        self.case_2 = {
            "docs": [
                [("Aku", False), ("suka", False), ("sama", True), ("kamu", False), (".", False)],
                [("Makan", False), ("gado-gado", False), ("bersama", True), ("pacar", False), (".", False)],
                [("Bakso", False), ("adalah", False), ("makanan", False), ("favorit", True), ("saya", False), (".", False)]
            ],
            "expected": [
                ["kamu", "."],
                ["pacar", "."],
                ["saya", "."]
            ]
        }

        # OOV context
        self.case_3 = {
            "docs": [
                [("Aku", False), ("suka", False), ("sama", True), ("kamu", False), (".", False)],
                [("Makan", False), ("gado-gado", False), ("bersama", True), ("pacar", False), (".", False)],
                [("Bakso", False), ("adalah", False), ("makanan", False), ("favorit", True), ("saya", False), (".", False)]
            ],
            "expected": [
                ["s", "a", "m", "a"],
                ["b", "e", "r", "s", "a", "m", "a"],
                ["f", "a", "v", "o", "r", "i", "t"]
            ]
        }
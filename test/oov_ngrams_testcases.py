class OOVNgramsTestCases:
    def __init__(self):
        # Semua token dalam setiap dokumen adalah bukan OOV
        self.case_1 = {
            "docs": [
                [("Makan", False), ("bakso", False), ("bersama", False), ("pacar", False), (".", False)],
                [("Gado-gado", False), ("adalah", False), ("makanan", False), ("favorit", False), ("saya", False), (".", False)],
                [("Aku", False), ("suka", False), ("kamu", False), (".", False)]
            ],
            "expected": []
        }

        # Semua token dalam setiap dokumen adalah OOV
        self.case_2 = {
            "docs": [
                [("Hari", True), ("ini", True), ("cerah", True), (".", True)],
                [("Bakso", True), ("urat", True), (".", True)],
                [("Aku", True), ("suka", True), ("kamu", True), (".", True)]
            ],
            "expected": [
                [("Hari", True)],
                [("ini", True)],
                [("cerah", True)],
                [(".", True)],
                [("Bakso", True)],
                [("urat", True)],
                [(".", True)],
                [("Aku", True)],
                [("suka", True)],
                [("kamu", True)],
                [(".", True)]
            ]
        }

        # OOV in the beginning of doc
        self.case_3 = {
            "docs": [
                [("Pagi", True), ("hari", False), (".", False)],
                [("Bakso", True), ("urat", False), (".", False)],
                [("Aku", True), ("suka", False), (".", False)]
            ],
            "expected": [
                [("Pagi", True), ("hari", False), (".", False)],
                [("Bakso", True), ("urat", False), (".", False)],
                [("Aku", True), ("suka", False), (".", False)]
            ]
        }

        self.case_4 = {
            "docs": [
                [("Makan", True), ("bakso", False), ("bersama", False), ("pacar", False), (".", False)],
                [("Gado-gado", True), ("adalah", False), ("makanan", False), ("favorit", False), ("saya", False), (".", False)],
                [("Aku", True), ("suka", False), ("kamu", False), (".", False)]
            ],
            "expected": [
                [("Makan", True), ("bakso", False), ("bersama", False)],
                [("Gado-gado", True), ("adalah", False), ("makanan", False)],
                [("Aku", True), ("suka", False), ("kamu", False)]
            ]
        }

        self.case_5 = {
            "docs": [
                [("Pagi", True), ("hari", True), (".", False)],
                [("Bakso", True), ("urat", True), (".", False)],
                [("Aku", True), ("suka", True), (".", False)]
            ],
            "expected": [
                [("Pagi", True)], 
                [("hari", True), (".", False)],
                [("Bakso", True)],
                [("urat", True), (".", False)],
                [("Aku", True)],
                [("suka", True), (".", False)]
            ]
        }

        # OOV in the end of doc
        self.case_6 = {
            "docs": [
                [("Pagi", False), ("hari", False), (".", True)],
                [("Bakso", False), ("urat", False), (".", True)],
                [("Aku", False), ("suka", False), (".", True)]
            ],
            "expected": [
                [("Pagi", False), ("hari", False), (".", True)],
                [("Bakso", False), ("urat", False), (".", True)],
                [("Aku", False), ("suka", False), (".", True)]
            ]
        }

        self.case_7 = {
            "docs": [
                [("Makan", False), ("bakso", False), ("bersama", False), ("pacar", False), (".", True)],
                [("Gado-gado", False), ("adalah", False), ("makanan", False), ("favorit", False), ("saya", False), (".", True)],
                [("Aku", False), ("suka", False), ("kamu", False), (".", True)]
            ],
            "expected": [
                [("bersama", False), ("pacar", False), (".", True)],
                [("favorit", False), ("saya", False), (".", True)],
                [("suka", False), ("kamu", False), (".", True)]
            ]
        }

        self.case_8 = {
            "docs": [
                [("Pagi", False), ("hari", True), (".", True)],
                [("Bakso", False), ("urat", True), (".", True)],
                [("Aku", False), ("suka", True), (".", True)]
            ],
            "expected": [
                [("Pagi", False), ("hari", True)],
                [(".", True)],
                [("Bakso", False), ("urat", True)],
                [(".", True)],
                [("Aku", False), ("suka", True)],
                [(".", True)]
            ]
        }

        # OOV in the middle of doc
        self.case_9 = {
            "docs": [
                [("Makan", False), ("bakso", False), ("bersama", True), ("pacar", False), (".", False)],
                [("Gado-gado", False), ("adalah", True), ("makanan", False), ("favorit", False), ("saya", False), (".", False)],
                [("Aku", False), ("suka", False), ("kamu", True), (".", False)]
            ],
            "expected": [
                [("Makan", False), ("bakso", False), ("bersama", True), ("pacar", False), (".", False)],
                [("Gado-gado", False), ("adalah", True), ("makanan", False), ("favorit", False)],
                [("Aku", False), ("suka", False), ("kamu", True), (".", False)]
            ]
        }

        # OOV in anywhere :)
        self.case_10 = {
            "docs": [
                [("Makan", True), ("bakso", True), ("bersama", False), ("pacar", False), (".", False)],
                [("Gado-gado", False), ("adalah", False), ("makanan", True), ("favorit", True), ("saya", False), (".", False)],
                [("Aku", False), ("suka", False), ("kamu", True), (".", True)],
                [("Aku", True), ("suka", True), ("kamu", True), (".", True)]
            ],
            "expected": [
                [("Makan", True)],
                [("bakso", True), ("bersama", False), ("pacar", False), (".", False)],
                [("Gado-gado", False), ("adalah", False), ("makanan", True)],
                [("favorit", True), ("saya", False), (".", False)],
                [("Aku", False), ("suka", False), ("kamu", True)],
                [(".", True)],
                [("Aku", True)],
                [("suka", True)],
                [("kamu", True)],
                [(".", True)]
            ]
        }

        self.case_11 = {
            "docs": [
                [('Pemerintah', False), ('kota', False), ('Delhi', False), ('mengerahkan', False), ('monyet', False), ('untuk', False), ('mengusir', False), ('monyet-monyet', True), ('lain', False), ('yang', False), ('berbadan', False), ('lebih', False), ('kecil', False), ('dari', False), ('arena', False), ('Pesta Olahraga', True), ('Persemakmuran', False), ('.', False)],
                [('Pemerintah', True), ('kota', True), ('Delhi', False), ('mengerahkan', False), ('monyet', True), ('untuk', False), ('mengusir', False), ('monyet-monyet', True), ('lain', False), ('yang', False), ('berbadan', False), ('lebih', False), ('kecil', True), ('dari', False), ('arena', False), ('Pesta Olahraga', False), ('Persemakmuran', True), ('.', True)]
            ],
            "expected": [
                [('untuk', False), ('mengusir', False), ('monyet-monyet', True), ('lain', False), ('yang', False)],
                [('dari', False), ('arena', False), ('Pesta Olahraga', True), ('Persemakmuran', False), ('.', False)],
                [('Pemerintah', True)],
                [('kota', True), ('Delhi', False), ('mengerahkan', False)],
                [('Delhi', False), ('mengerahkan', False), ('monyet', True), ('untuk', False), ('mengusir', False)],
                [('untuk', False), ('mengusir', False), ('monyet-monyet', True), ('lain', False), ('yang', False)],
                [('berbadan', False), ('lebih', False), ('kecil', True), ('dari', False), ('arena', False)],
                [('arena', False), ('Pesta Olahraga', False), ('Persemakmuran', True)],
                [(".", True)]
            ]
        }
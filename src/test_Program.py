from unittest import TestCase
from src.Program import DataMasking as dm

class TestDataMasking(TestCase):
    def test_load_program(self):
        self.fail()

    def test_process_csv(self):
        self.fail()

    def test_average_invoiced(self):
        self.fail()

    def test_average(self):
        # 5 + 7 + 2.5 = 14.5 -> 14.5 / 3 = 4.83333
        expected = 4.833333333333333
        result = dm.average(self, 14.5, 3)
        assert result == expected

    def test_write_csv(self):
        self.fail()

    def test_replace_letters(self):
        self.fail()

    def test_read_file_csv(self):
        self.fail()

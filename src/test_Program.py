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

    def test_replace_letters_name(self):
        expected = "XXXXXX XXXX"
        nameTest = "Javier Cruz"
        self.check_letters(expected, nameTest)

    def test_replace_letters_email(self):
        expected = "XXXXXXX-XXXXXX@XXXX-XXXXXX.XXX"
        emailTest = "gerardo-puente@mail-sample.com"
        self.check_letters(expected, emailTest)

    def check_letters(self, expected, value):
        result = dm.replaceLetters(self, value)
        assert result == expected

    def test_read_file_csv(self):
        self.fail()

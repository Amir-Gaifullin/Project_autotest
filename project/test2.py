import unittest
import subprocess
import pycodestyle
class Autotest(unittest.TestCase):
    def test_input_output(self):
        input_for_test = b"3"
        output = subprocess.check_output(["python", "c:/Project_autotest/file_for_test/plus_ten.py"], 
                                         input = input_for_test, stderr = subprocess.STDOUT)
        str_output = output.decode('utf-8')
        str_output = str_output.replace("\r", "")
        correct_output = "13\n"
        self.assertEqual(str_output,correct_output)
    def test_code_for_pep8(self):
        pep8style = pycodestyle.StyleGuide(quiet = True)
        result = pep8style.check_files(["c:/Project_autotest/file_for_test/plus_ten.py"])   #['file1.py', 'file2.py']
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
if __name__ == '__main__':
    unittest.main()
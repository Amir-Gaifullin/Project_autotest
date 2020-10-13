import unittest
import subprocess
import pycodestyle
class Autotest(unittest.TestCase):
    '''
    def test_input_output_file_name(self):
        input_for_test = b"x" #вписать input в формате b"x" или b"x y z d\n" для последовательности символов
        output = subprocess.check_output(["python", "c:/Project_autotest/file_for_test/file_name.py"], #вписать путь к файлу
                                         input = input_for_test, stderr = subprocess.STDOUT)
        str_output = output.decode('utf-8')
        str_output = str_output.replace("\r", "")
        correct_output = "x\n" #вписать ожидаемый вывод в формате "x\n" или b"x y z d\n" для последовательности символов
        self.assertEqual(str_output,correct_output)
    def test_code_for_pep8_file_name(self):
        pep8style = pycodestyle.StyleGuide(quiet = True)
        result = pep8style.check_files(["c:/Project_autotest/file_for_test/file_name.py"])   #['file1.py', 'file2.py']
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
    '''
    def test_input_output_fibonachi(self):
        input_for_test1 = b"3" #вписать input в формате b"x"
        output1 = subprocess.check_output(["python", "c:/Project_autotest/file_for_test/hw_09-09-20/fibonachi.py"], #вписать путь к файлу
                                         input = input_for_test1, stderr = subprocess.STDOUT)
        input_for_test2 = b"7" #вписать input в формате b"x"
        output2 = subprocess.check_output(["python", "c:/Project_autotest/file_for_test/hw_09-09-20/fibonachi.py"], #вписать путь к файлу
                                         input = input_for_test2, stderr = subprocess.STDOUT)
        str_output1 = output1.decode('utf-8')
        str_output1 = str_output1.replace("\r", "")
        correct_output1 = "1\n" #вписать ожидаемый вывод в формате "x\n"
        self.assertEqual(str_output1,correct_output1)
        str_output2 = output2.decode('utf-8')
        str_output2 = str_output2.replace("\r", "")
        correct_output2 = "8\n" #вписать ожидаемый вывод в формате "x\n"
        self.assertEqual(str_output2,correct_output2)
    def test_code_for_pep8_fibonachi(self):
        pep8style = pycodestyle.StyleGuide(quiet = True)
        result = pep8style.check_files(["c:/Project_autotest/file_for_test/hw_09-09-20/fibonachi.py"])   #['file1.py', 'file2.py']
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
    def test_input_output_odd(self):
        input_for_test = b"6 7 9 32 47\n" #вписать input в формате b"x" или b"x y z d\n"
        output = subprocess.check_output(["python", "c:/Project_autotest/file_for_test/hw_09-09-20/odd.py"], #вписать путь к файлу
                                         input = input_for_test, stderr = subprocess.STDOUT)
        str_output = output.decode('utf-8')
        str_output = str_output.replace("\r", "")
        correct_output = "3\n" #вписать ожидаемый вывод в формате "x\n" или b"x y z d\n"
        self.assertEqual(str_output,correct_output)
    def test_code_for_pep8_odd(self):
        pep8style = pycodestyle.StyleGuide(quiet = True)
        result = pep8style.check_files(["c:/Project_autotest/file_for_test/hw_09-09-20/odd.py"])   #['file1.py', 'file2.py']
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
    def test_input_output_reverse(self):
        input_for_test = b"1 2 3 4 5\n" #вписать input в формате b"x" или b"x y z d\n"
        output = subprocess.check_output(["python", "c:/Project_autotest/file_for_test/hw_09-09-20/reverse.py"], #вписать путь к файлу
                                         input = input_for_test, stderr = subprocess.STDOUT)
        str_output = output.decode('utf-8')
        str_output = str_output.replace("\r", "")
        str_output = str_output.strip()
        correct_output = "5 4 3 2 1" #вписать ожидаемый вывод в формате "x\n"
        self.assertEqual(str_output,correct_output)
    def test_code_for_pep8_reverse(self):
        pep8style = pycodestyle.StyleGuide(quiet = True)
        result = pep8style.check_files(["c:/Project_autotest/file_for_test/hw_09-09-20/reverse.py"])   #['file1.py', 'file2.py']
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
    def test_input_output_yes_no(self):
        input_for_test = b"1 2 3 4 5" #вписать input в формате b"x" или b"x y z d\n"
        output = subprocess.check_output(["python", "c:/Project_autotest/file_for_test/hw_09-09-20/yes_no.py"], #вписать путь к файлу
                                         input = input_for_test, stderr = subprocess.STDOUT)
        str_output = output.decode('utf-8')
        str_output = str_output.replace("\r", "")
        correct_output = "no\n" #вписать ожидаемый вывод в формате "x\n"
        self.assertEqual(str_output,correct_output)
    def test_code_for_pep8_yes_no(self):
        pep8style = pycodestyle.StyleGuide(quiet = True)
        result = pep8style.check_files(["c:/Project_autotest/file_for_test/hw_09-09-20/yes_no.py"])   #['file1.py', 'file2.py']
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
    def test_input_output_formula(self):
        input_for_test = b"5679" #вписать input в формате b"x" или b"x y z d\n"
        output = subprocess.check_output(["python", "c:/Project_autotest/file_for_test/hw_09-09-20/formula.py"], #вписать путь к файлу
                                         input = input_for_test, stderr = subprocess.STDOUT)
        str_output = output.decode('utf-8')
        str_output = str_output.replace("\r", "")
        correct_output = "1.5707271850678795\n" #вписать ожидаемый вывод в формате "x\n"
        self.assertEqual(str_output,correct_output)
    def test_code_for_pep8_formula(self):
        pep8style = pycodestyle.StyleGuide(quiet = True) 
        result = pep8style.check_files(["c:/Project_autotest/file_for_test/hw_09-09-20/formula.py"])   #['file1.py', 'file2.py']
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
if __name__ == '__main__':
    unittest.main()

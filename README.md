# Project_autotest(SYP)
Проект был создан для проверки файлов на правильность вывода кода, а также на проверку по PEP8.
Создан простейшим функциями для понятности алгоритма работы программы.

**Инструкция к использыванию:**
1. Прежде чем начать делать необходимо скачать определённые библиотеки:
```
pip install unittest 
pip install subprocess
pip install pycodestyle
pip install cricket

```
2. Далее в корне репозитория заходим в папку с названием "file_for_test" и копируем туда файл типа "file_name.py" в котором находиться сам код для проверки.
```
 cd c:Project_autotest/file_for_test/file_name.py
 
```
3. Скопировав файлы в нужную папку, необходимо открыть test2.py, которая находиться в папке "project".
4. После открытия кода необходимо следовать шаблону для создания теста на каждую папку с кодом:
```
import unittest
import subprocess
import pycodestyle
class Autotest(unittest.TestCase):
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
if __name__ == '__main__':
    unittest.main()
```
5. Написав тесты по шаблону, можно приступить к самой работе програмыы, в Git Bash(консоль) необходимо вписать перечень команд в зависисмости от требований.
```
cd c:Project_autotest/project # команда которая заходить в файл "project"
python -m unittest -v test2.py # команда выведет результаты теста
cricket-unittest # команда откроет приложение cricket, для запуска тестов достаточно нажать на "Run all"
pycodestyle --first test.py # детальное проверка кода на pep8, с выводом ошибок в коде

```

## Примеры вывода программы:
- python -m unittest -v test2.py
```
$ python -m unittest -v test2.py
test_code_for_pep8_fibonachi (test2.Autotest) ... ok
test_code_for_pep8_formula (test2.Autotest) ... FAIL
test_code_for_pep8_odd (test2.Autotest) ... FAIL
test_code_for_pep8_reverse (test2.Autotest) ... ok
test_code_for_pep8_yes_no (test2.Autotest) ... ok
test_input_output_fibonachi (test2.Autotest) ... ok
test_input_output_formula (test2.Autotest) ... ERROR
test_input_output_odd (test2.Autotest) ... ok
test_input_output_reverse (test2.Autotest) ... ok
test_input_output_yes_no (test2.Autotest) ... FAIL

======================================================================
ERROR: test_input_output_formula (test2.Autotest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Project_autotest\project\test2.py", line 82, in test_input_output_formula
    output = subprocess.check_output(["python", "c:/Project_autotest/file_for_test/hw_09-09-20/formula.py"], #тяшёрЄ№ яєЄ№ ъ Їрщыє
  File "C:\Python385\lib\subprocess.py", line 411, in check_output
    return run(*popenargs, stdout=PIPE, timeout=timeout, check=True,
  File "C:\Python385\lib\subprocess.py", line 512, in run
    raise CalledProcessError(retcode, process.args,
subprocess.CalledProcessError: Command '['python', 'c:/Project_autotest/file_for_test/hw_09-09-20/formula.py']' returned non-zero exit status 1.

======================================================================
FAIL: test_code_for_pep8_formula (test2.Autotest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Project_autotest\project\test2.py", line 91, in test_code_for_pep8_formula
    self.assertEqual(result.total_errors, 0,
AssertionError: 5 != 0 : Found code style errors (and warnings).

======================================================================
FAIL: test_code_for_pep8_odd (test2.Autotest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Project_autotest\project\test2.py", line 51, in test_code_for_pep8_odd
    self.assertEqual(result.total_errors, 0,
AssertionError: 1 != 0 : Found code style errors (and warnings).

======================================================================
FAIL: test_input_output_yes_no (test2.Autotest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Project_autotest\project\test2.py", line 74, in test_input_output_yes_no
    self.assertEqual(str_output,correct_output)
AssertionError: 'yes\n' != 'no\n'
- yes
+ no


----------------------------------------------------------------------
Ran 10 tests in 0.320s

FAILED (failures=3, errors=1)

```
- pycodestyle --first test.py
```
$ pycodestyle --first formula.py
formula.py:16:5: E101 indentation contains mixed spaces and tabs
formula.py:16:5: W191 indentation contains tabs
formula.py:16:6: E113 unexpected indentation
formula.py:19:1: E265 block comment should start with '# '

```

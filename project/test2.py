import unittest
import pwd
from my_sum import sum
#from hamcrest import contains_string
#from prego import TestCase, Task

class TestSum(unittest.TestCase):
#    def test_output(self):
#        task = Task()
#        text = input()
#        cmd = task.command('1 2 3 4 5 6')   #<=='your_input'
#        task.assert_that(cmd.stdout.content, 
#                         contains_string(21)) # <=='your_expected_output'
# class TestSum(unittest.TestCase):
    def test_list_sum(self):
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

    def test_list_sum(self):
        data = [1, 2, 3, 4, 5, 6]
        result = sum(data)
        self.assertEqual(result, 21)
if __name__ == '__main__':
    unittest.main()
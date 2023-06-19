import unittest
from selenium import webdriver
import page

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
        self.driver.get("http://python.org")

    def test_example(self):
        print("Test")
        assert False 

    def test_example_2(self):
        assert True 

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
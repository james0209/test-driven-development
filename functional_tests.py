from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def tearDown(self):
        self.browser.quit

    def test_title(self):
        self.browser.get("http://localhost:8000")
        self.assertIn("install", self.browser.title)


if __name__ == "__main__":
    unittest.main()

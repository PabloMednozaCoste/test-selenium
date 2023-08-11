import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import page


def is_database_affected():
    import sqlite3
    conn = sqlite3.connect('python.db')
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM users")
        return False  # Table still exists, not affected
    except sqlite3.OperationalError:
        return True  # Table doesn't exist, affected
    finally:
        conn.close()

class PrhytonOrgSearch(unittest.TestCase):

    def setUp(self):
        PATH = r"C:\Program Files (x86)\chromedriver.exe"
        options = webdriver.ChromeOptions()
        service = Service(PATH)
        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.get("https://www.python.org/")

    def test_search_python(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matches()
        mainPage.search_text_element="pycon"
        mainPage.click_go_button()
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_results_found()

    def test_sql_injection(self):
        # Prepare malicious input
        malicious_input = "'; DROP TABLE users; --"

        mainPage = page.MainPage(self.driver)
        mainPage.search_text_element = malicious_input  # Try injecting malicious input
        mainPage.click_go_button()

        # Check if the database is affected
        assert is_database_affected()

    def tearDown(self):
        self.driver.close()

if __name__=="__main__":
    unittest.main()

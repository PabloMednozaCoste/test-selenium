from selenium.webdriver.common.by import By


class MainPageLocators(object):
    SEARCH_INPUT = (By.NAME, "q")  # Adjust this based on your actual locator
    GO_BUTTON = (By.ID, "submit")


class SearchResultsPageLocators(object):
    pass
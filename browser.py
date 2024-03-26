"""
Description:
This file contains a BrowserManager class that controls web browsers based on the provided 
browser name.

Classes:
- BrowserManager: Manages opening and closing web browsers like Chrome, Edge, and Firefox.
"""
from selenium import webdriver

class BrowserManager:
    """
    A class to manage different web browsers for opening files.

    Attributes:
    - driver: WebDriver instance for the browser.
    """
    def __init__(self):
        """
        Initialize the BrowserManager class.
        """
        self.driver = None

    def setup_browser(self, url, browser='chrome'):
        """
        Setup the specified browser and open the provided URL.

        Parameters:
        - url (str): The URL to open in the browser.
        - browser (str): The type of browser to use (default is 'chrome').
                        Supported values: 'chrome', 'edge', 'firefox'.
        """
        if browser.lower() == 'chrome':
            self.driver = webdriver.Chrome()
        elif browser.lower() == 'edge':
            self.driver = webdriver.Edge()
        elif browser.lower() == 'firefox':
            self.driver = webdriver.Firefox()
        else:
            raise ValueError("Unsupported browser type.")

        self.driver.get(url)

    def close_browser(self):
        """
        Close the browser if it is open.
        """
        if self.driver is not None:
            self.driver.quit()
           
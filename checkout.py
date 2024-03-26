"""
Description:
This script defines a CheckoutInfo class which is used to store information about the checkout
process such as user's name and pincode.

Classes:
- CheckoutInfo: A class to handle filling in personal information on the checkout page.

Functions/Methods:
- __init__: Initializes the CheckoutInfo class with browser_manager.
- personal_info: Handle filling in user's personal information on the checkout page.

Dependencies:
- selenium.webdriver.common.by.By: For locating elements on the web page.
"""
from selenium.webdriver.common.by import By

class Checkout:                         #pylint: disable=R0903
    """
    A class to handle filling in personal information on the checkout page.

    This class provides methods to interact with and fill in personal information fields
    such as first name, last name, and postal code on the checkout page.

    Attributes:
    browser_manager: An instance of the BrowserManager class for browser interaction.
    """
    def __init__(self,browser_manager):
        """
        Initialize the CheckoutInfo class with the browser manager.

        Args:
            browser_manager (BrowserManager): An instance of the BrowserManager class.
        """
        self.browser_manager = browser_manager

    def personal_info(self):
        """
        Fill in personal information fields on the checkout page.

        This method finds the first name, last name, and postal code fields on the checkout page
        and fills them with sample data for testing purposes.
        """
        first_name_field = self.browser_manager.driver.find_element(By.ID, "first-name")
        last_name_field = self.browser_manager.driver.find_element(By.ID, "last-name")
        postal_code_field = self.browser_manager.driver.find_element(By.ID, "postal-code")

        first_name_field.send_keys("John")
        last_name_field.send_keys("Doe")
        postal_code_field.send_keys("12345")
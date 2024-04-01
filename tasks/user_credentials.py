"""
Description:
This script defines a Credentials class to retrieve user credentials from a web page
and save them to an Excel file. It utilizes a BrowserManager instance to control the web browser
and extracts user IDs, names, and passwords from specific elements on the page.

Classes:
- Credentials: Manages the retrieval and storage of user credentials.

Functions/Methods:
- __init__: Initializes the Credentials class with URL, filename, and browser manager.
- user_credentials: Retrieves user credentials from the web page and saves them to an
Excel file.
"""
from selenium.webdriver.common.by import By
import openpyxl

class Credentials:
    """
    Initialize the Credentials class with the specified URL and filename for retrieving user credentials.

    Parameters:
    url (str): The URL of the website from which to retrieve credentials.
    filename (str): The name of the Excel file to save the credentials to.
    browser_manager: An instance of BrowserManager to control the web browser.
    """

    def __init__(self, url, filename, browser_manager):
        self.url = url
        self.filename = filename
        self.browser_manager = browser_manager

    def user_credentials(self):
        """This method retrieves user credentials from the specified website
        and saves them to the Excel file.
        """
        try:
            self.browser_manager.setup_browser(self.url)
            self.browser_manager.driver.implicitly_wait(3)
            users = self.browser_manager.driver.find_elements(By.CLASS_NAME, "login_credentials")
            passwords = self.browser_manager.driver.find_elements(By.CLASS_NAME, "login_password")

            workbook = openpyxl.Workbook()
            credentials_sheet = workbook.create_sheet("User credentials")
            credentials_sheet.append(["User ID", "User Name", "Password"])

            index = 1

            for user, password in zip(users, passwords):
                user_name = user.text.split("\n")
                user_pass = password.text.split("\n")
                for name, passs in zip(user_name[1:], user_pass[1:] * len(user_name[1:])):
                    credentials_sheet.append([index, name, passs])
                    index += 1

            workbook.save(self.filename)

        finally:
            self.browser_manager.driver.quit()
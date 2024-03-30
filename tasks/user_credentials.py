"""
The selenium package is used to automate web browser interaction.
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl

class Credentials:
      """
        Initialize the Credentials class with the specified URL and filename for retrieving user credentials.
        
        Parameters:
        url (str): The URL of the website from which to retrieve credentials.
        filename (str): The name of the Excel file to save the credentials to.
        """
      def __init__(self, url, filename):
        self.url = url
        self.filename = filename
        self.driver = webdriver.Chrome()

      def user_credentials(self):
        """This method retrieves user credentials from the specified website
           and saves them to the Excel file.
        """
        try:
            self.driver.get(self.url)

            users = self.driver.find_elements(By.CLASS_NAME, "login_credentials")
            passwords = self.driver.find_elements(By.CLASS_NAME, "login_password")

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
            self.driver.quit()
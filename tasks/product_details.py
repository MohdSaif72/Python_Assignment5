"""
Description:
The script defines a ProductDetails class to retrieve and store product details
from a web page after logging in. It captures the product details in the excel sheet

Classes:
-ProductDetails: Retrieves and stores product details from website.

Function/Methods:
-__init__: Initializes the ProductDetailsRetriever class with URL, filename, browser manager.
-product_details: Logs into the website using provided username and password.
"""
from selenium.webdriver.common.by import By
import openpyxl
from login import Login
from screenshot import Screenshot

class ProductDetails:
    """
    Initialize the ProductDetails class with the specified URL and filename for retrieving product details.

    Parameters:
    url (str): The URL of the website from which to retrieve product details.
    filename (str): The name of the Excel file to save the product details to.
    browser_manager: An instance of BrowserManager
    """
    user_id = "standard_user"
    password = "secret_sauce"

    def __init__(self, url, filename, browser_manager):
        self.url = url
        self.filename = filename
        self.browser_manager = browser_manager

    def product_details(self):
        """
        This method retrieves product details from the specified URL and saves them to the Excel file.
        """
        try:
            self.browser_manager.setup_browser(self.url)
            login_manager = Login(self.browser_manager, self.user_id, self.password)
            login_manager.login()
            self.browser_manager.driver.implicitly_wait(5)

            workbook = openpyxl.load_workbook(self.filename)
            products_sheet = workbook.create_sheet("Product Details")
            products_sheet.append(["Product ID", "Product Name", "Description", "Price"])
            products = self.browser_manager.driver.find_elements(By.CLASS_NAME, "inventory_item")
            screenshot_manager = Screenshot(self.browser_manager)
            screenshot_manager.capture()
            index = 1
            for product in products:
                product_info = product.text.split("\n")
                product_name = product_info[0]
                product_description = product_info[1]
                product_price = product_info[2]
                products_sheet.append([index, product_name, product_description, product_price])
                index += 1
            workbook.save(self.filename)

        finally:
            self.browser_manager.driver.quit()
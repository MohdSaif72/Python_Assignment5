"""
The selenium package is used to automate web browser interaction.
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl

class ProductDetails:
     """
        Initialize the ProductDetails class with the specified URL and filename for retrieving product details.
        
        Parameters:
        url (str): The URL of the website from which to retrieve product details.
        filename (str): The name of the Excel file to save the product details to.
        """
     def __init__(self, url, filename):
        self.url = url
        self.filename = filename
        self.driver = webdriver.Chrome()

     def product_details(self):
        """
        This method retrieves product details from the specified URL and saves them to the Excel file.
        """
        try:
            self.driver.get(self.url)
            username_field = self.driver.find_element(By.ID, "user-name")
            password_field = self.driver.find_element(By.ID, "password")
            login_button = self.driver.find_element(By.CLASS_NAME, "btn_action")

            username_field.send_keys("standard_user")
            password_field.send_keys("secret_sauce")
            login_button.click()
            self.driver.implicitly_wait(5)

            workbook = openpyxl.load_workbook(self.filename)
            products_sheet = workbook.create_sheet("Product Details")
            products_sheet.append(["Product ID", "Product Name", "Description", "Price"])
            products = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
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
            self.driver.quit()



# Selenium Assignment
## Swag Labs - Automation
This repository contains a Python script for web automation of a Saucedemo web page.

## Problem Statement

Using Selenium with Python please complete the following assignments.
--------------------------------------------------------------------------

1. Retrieve all the Users and password related information and store it in Sheet named "User credentials" in a excel file.
User ID, User Name, Password

2. Try login with all the Users provided on the website link https://www.saucedemo.com/v1/ and record any error messages 
displayed for a specific user. write this information to another sheet named "Login" in the same excel file as above 
in the following format.
User ID, Login Message
 
3. Login using the "standard_user" and retrieve all the product related information for every listed product. 
Write this information into a separate sheet named "Product Details" in the same excel file.
Product ID, Product Name, Description, Price

4. Manually create another sheet called "Order Details" in the same excel file and add Orders for 
the "standard_user" and "problem_user". Decide on the Columns on your own and try to represent this data. 
(review before you move to next one)

5. Using the above "Order Details" sheet try the place all the orders on the website one by one. Update a new column in the 
"Order Details" sheet called "Order Status" marking it as "Success/Failure".
Success criteria should be as follows.

   a. The correct number of items should be added to the Cart.

   b. The total amount at the end should be correct.

   c. Success message should be displayed for every order placed.

   d. No Items should be left over in the cart.

## Features
The script performs the following tasks:

- Retrieves user credentials from a web page.
- Logs in to the web page with the user credentials.
- Retrieves product details from the web page.
- Creates an order details file with the product details.
- Updates the order details file with a new column and check the success/failure according to criteria.
The script uses several classes and functions from different modules to accomplish these tasks.


## File Structure
- user_credentials: Contains the Credentials class to get the usernames and password from website.
- login_users: Contains the UserLogin class to log in to a web page with user credentials.
- product_details: Contains the ProductDetails class to retrieve product details from a web page.
- config: Contains the website url and excel filename which is to be created.
- main: It is the main file to automate the work and run all other functionalities together.
  
## Functions
- user_credentials: Retrieves user credentials from the web page and saves them to an Excel file.
- login_users: Logs in to the web page with user credentials.
- product_details: Logs in to the web page and retrieves product details.
- orders: Creates an order details file.


## Modules Required
- from selenium import webdriver
- from selenium.webdriver.common.by import By
- from selenium.webdriver.common.keys import Keys
- openpyxl
- time
- pandas


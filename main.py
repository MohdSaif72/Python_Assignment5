import config
from user_credentials import Credentials
from login_users import UserLogin
from product_details import ProductDetails

if __name__ == "__main__":
    credentials_data = Credentials(config.URL, config.FILENAME)
    credentials_data.user_credentials()

    login = UserLogin(config.URL, config.FILENAME)
    login.login_users()

    products = ProductDetails(config.URL, config.FILENAME)
    products.product_details()

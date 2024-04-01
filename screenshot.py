"""
Helps to interact with files and directories.
"""
import os
from datetime import datetime

class Screenshot:
    """
    A class to capture screenshots using a provided browser manager.

    Attributes:
    - browser: An instance of BrowserManager to control the web browser.
    """
    def __init__(self, browser):
        self.browser = browser

    def capture(self):
        """
        Capture a screenshot of the current web page.

        The screenshot is saved in a 'Screenshots' directory with a filename containing the
        current timestamp.

        Returns:
        - filepath (str): The path to the saved screenshot file.
        """
        if not os.path.exists('Screenshots'):
            os.makedirs("Screenshots")
        current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"screenshot_{current_time}.png"
        filepath = os.path.join('Screenshots', filename)
        self.browser.driver.get_screenshot_as_file(filepath)
   
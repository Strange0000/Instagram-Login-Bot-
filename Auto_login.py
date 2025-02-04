from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

def startBot(username, password, url):
    # Path to the ChromeDriver executable
    driver_path = "D:\\chromedriver-win64\\chromedriver.exe"

    # Set up the WebDriver
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service)

    try:
        # Open the URL in Chrome
        driver.get(url)
        time.sleep(2)  # Wait for the page to load

        # Find and fill in the username field
        driver.find_element(By.NAME, "username").send_keys(username)

        # Find and fill in the password field
        driver.find_element(By.NAME, "password").send_keys(password)

        # Submit the form
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        time.sleep(5)  # Wait for login to complete (adjust as needed)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the browser
        driver.quit()


# Driver Code
username = "sumit_jaiswal__"
password = "xxxxx"  # Replace with your password
url = "https://www.instagram.com/accounts/login/"

# Call the function
startBot(username, password, url)
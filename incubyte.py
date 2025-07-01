from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import re
pswrd = "abcdef@Abcdef"


chrome_options = Options()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 10)


def validate_mail_id_format():
    x = random.randint(1, 100)
    mail_id = f"js{x}@gmail.com"
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, mail_id):
        return True
    else:
        return False


def load_web_page():
    driver.get("https://magento.softwaretestingboard.com/")
    driver.refresh()
    return True


def account_creation():
# # Navigate to account creation
    try:
        x = random.randint(1, 100)
        mail_id = f"js{x}@gmail.com"
        driver.refresh()
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Create an Account"))).click()

    # # Fill form
        
        wait.until(EC.visibility_of_element_located((By.ID, "firstname"))).send_keys("Jyoti")
        driver.find_element(By.ID, "lastname").send_keys("Sharma")
        driver.find_element(By.ID, "email_address").send_keys(mail_id)
        print("Email:", mail_id)
        driver.find_element(By.ID, "password").send_keys(pswrd)
        driver.find_element(By.ID, "password-confirmation").send_keys(pswrd)

    # # Submit form
        driver.find_element(By.XPATH, '//*[@id="form-validate"]/div/div[1]/button/span').click()
    #  capture result
        driver.save_screenshot("account_created.png")
        print("Account creation completed.")
        return True
    except:
        print("Account creation failed, check logs for more details")
        return False

time.sleep(10)

driver.quit()


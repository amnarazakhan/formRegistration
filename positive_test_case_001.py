from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

registration_url = "https://abc.com"

valid_name = "Amna Raza Khan"
valid_email = "amnarazakhan02@gmail.com"
valid_password = "pass123456"
valid_date_of_birth = "05-04-2002"
valid_gender = "female"
subscription_to_newsletter = True


try:
    driver = webdriver.Chrome()
    driver.get(registration_url)

    name_field = driver.find_element(By.ID, "name_field")
    email_field = driver.find_element(By.ID, "email_field")
    password_field = driver.find_element(By.ID, "password_field")
    confirm_password_field = driver.find_element(By.ID, "confirm_password_field")
    date_of_birth_field = driver.find_element(By.ID, "date_of_birth_field")
    gender_radio_button = driver.find_element(By.ID, f"gender_{valid_gender.lower()}")
    newsletter_checkbox = driver.find_element(By.ID, "newsletter_subscribe") if subscription_to_newsletter else None

    name_field.send_keys(valid_name)
    email_field.send_keys(valid_email)
    password_field.send_keys(valid_password)
    confirm_password_field.send_keys(valid_password)
    date_of_birth_field.send_keys(valid_date_of_birth)
    gender_radio_button.click()
    if subscription_to_newsletter:
        newsletter_checkbox.click()

    submit_button = driver.find_element(By.ID, "submit_button")
    submit_button.click()

    try:
        confirmation_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "confirmation_message"))
        )
    except TimeoutException:
        print("Confirmation message not found within 10 seconds.")

    else:
        assert "Registration Successful!" in confirmation_message.text, ("Confirmation message doesn't match expected "
                                                                         "text.")

finally:
    driver.quit()

print("Test execution completed.")
